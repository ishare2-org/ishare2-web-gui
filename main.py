import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from python_scripts.add_context import add_context
from python_scripts.command_utils import _run_command
from python_scripts.download_csv import download_csv
from python_scripts.misc_utils import (
    get_config,
    get_help_content,
    get_version,
    install_ishare2,
    relicense,
)

from routers import (
    changelogs,
    downloads,
    installed,
    request_delete,
    request_download,
)

download_csv()

app = FastAPI(
    title="ishare2 API",
    version=os.getenv("API_VERSION", "0.0.1"),
    debug=False, #Change to False in production
)

origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(
    "/images", StaticFiles(directory=os.getenv("IMAGES_DIR", "./web_app/src/static/images")), name="images"
)
app.mount(
    "/styles.css",
    StaticFiles(directory=os.getenv(
        "STYLES_DIR", "./web_app/src/static/styles")),
    name="styles",
)
app.mount(
    "/scripts",
    StaticFiles(directory=os.getenv(
        "SCRIPTS_DIR", "./web_app/src/static/scripts")),
    name="scripts",
)


templates = Jinja2Templates(
    directory=os.getenv("TEMPLATES_DIR", "./web_app/src"))

routes = [downloads, request_delete, request_download, installed, changelogs]

for route in routes:
    app.include_router(route.router)


@app.get("/", response_class=HTMLResponse, tags=["Root"])
async def root(request: Request):
    data = {
        "title": "Homepage - ishare2",
    }
    context = add_context({}, request, data)
    return templates.TemplateResponse("/pages/index.html", context)


@app.get("/relicense", tags=["Extras"])
async def get_relicensed(request: Request):
    return relicense()


@app.get("/install/ishare2", tags=["Extras"])
async def get_install_ishare2(request: Request):
    return install_ishare2()


if __name__ == "__main__":
    config = get_config()
    HOST = config["api"]["host"]
    PORT = config["api"]["port"]

    uvicorn.run(
        "main:app",
        host=HOST,
        port=PORT,
        reload=False,  # Change to False in production
        workers=4,
    )
