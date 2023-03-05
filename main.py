from routers import downloads, request_delete, request_download, installed, changelogs
from python_scripts.download_csv import download_csv
from python_scripts.misc_utils import get_help_content, get_version, relicense, get_config, install_ishare2
from python_scripts.command_utils import _run_command
from python_scripts.add_context import add_context
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
import uvicorn
import os

download_csv()

app = FastAPI(
    title="ishare2 API",
    version=os.getenv("API_VERSION", "0.0.1")
)

origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/images", StaticFiles(directory=os.getenv("IMAGES_DIR",
          "./web_app/src/static/images")), name="images")
app.mount("/styles.css",
          StaticFiles(directory=os.getenv("STYLES_DIR", "./web_app/src/static/styles")), name="styles")
app.mount(
    "/scripts", StaticFiles(directory=os.getenv("SCRIPTS_DIR", "./web_app/src/static/scripts")), name="scripts")

templates = Jinja2Templates(
    directory=os.getenv("TEMPLATES_DIR", "./web_app/src"))

routes = [downloads, request_delete, request_download,
          installed, changelogs]

for route in routes:
    app.include_router(route.router)

@app.get("/", response_class=HTMLResponse, tags=["Root"])
async def root(request: Request):
    data = {
        "title": "Homepage - ishare2",
    }
    context = {}
    context = add_context(context, request, data)
    return templates.TemplateResponse("/pages/index.html", context)


@ app.get("/relicense", tags=["Extras"])
async def get_relicensed(request: Request):
    return relicense()


@ app.get("/install/ishare2", tags=["Extras"])
async def get_install_ishare2(request: Request):
    return install_ishare2()


@ app.get("/help", tags=["Help"])
async def get_help_file(request: Request):
    data = {
        "title": "Help - ishare2",
        "url": get_help_content()
    }
    context = {}
    context = add_context(context, request, data)
    return templates.TemplateResponse("pages/help.html", context)


if __name__ == "__main__":
    config = get_config()
    HOST = config["api"]["host"]
    PORT = config["api"]["port"]

    uvicorn.run(
        "main:app",
        host=HOST,
        port=PORT,
        reload=True,
        workers=4,
    )
