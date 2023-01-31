from python_scripts.misc_utils import get_help_content
from python_scripts.misc_utils import get_changelog_gui_content
from python_scripts.misc_utils import get_changelog_content
from python_scripts.misc_utils import relicense
from python_scripts.live_search_form import live_search_qemu_image
from python_scripts.live_search_form import live_search_dynamips_image
from python_scripts.live_search_form import live_search_bin_image
from python_scripts.delete_images import delete_docker_image
from python_scripts.delete_images import delete_qemu_image
from python_scripts.delete_images import delete_dynamips_image
from python_scripts.delete_images import delete_bin_image
from python_scripts.ishare2_installed_docker import get_installed_docker_images
from python_scripts.ishare2_installed_qemu import get_installed_qemu_images
from python_scripts.ishare2_installed_dynamips import get_installed_dynamips_images
from python_scripts.ishare2_installed_bin import get_installed_bin_images
from python_scripts.ishare2_pull_qemu import download_qemu_image
from python_scripts.ishare2_pull_dynamips import download_dynamips_image
from python_scripts.ishare2_pull_bin import download_bin_image
from python_scripts.ishare2_search_qemu import get_qemu_list
from python_scripts.ishare2_search_dynamips import get_dynamips_list
from python_scripts.ishare2_search_bin import get_bin_list
from python_scripts.misc_utils import get_credentials
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
import json
import uvicorn
import requests


app = FastAPI(
    title="ishare2 API",
    version="0.0.1"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/images", StaticFiles(directory="./web_app/static/images"), name="images")


app.mount("/styles.css",
          StaticFiles(directory="./web_app/static/styles"), name="styles")


templates = Jinja2Templates(directory="./web_app/src")


@app.get("/", response_class=HTMLResponse, tags=["Root"])
async def root(request: Request):
    config = get_credentials()
    URL_ISHARE2_VERSION = config["constants"]["ishare2_version"]

    ishare2_version = requests.get(URL_ISHARE2_VERSION).text

    data = {
        "version": ishare2_version,
        "title": "Homepage - ishare2",
    }
    # return data
    return templates.TemplateResponse("/pages/index.html", {"request": request, "data": data})


@app.get("/lists/bin", tags=["Get lists"])
async def get_list_of_bin_images(request: Request):
    data = {
        "title": "Bin images - ishare2",
        "command": get_bin_list()
    }
    # return data
    return templates.TemplateResponse("pages/lists/bin_list.html", {"request": request, "data": data})


@app.get("/lists/dynamips", tags=["Get lists"])
async def get_list_of_dynamips_images(request: Request):
    data = {
        "title": "Dynamips images - ishare2",
        "command": get_dynamips_list()
    }
    # return data
    return templates.TemplateResponse("pages/lists/dynamips_list.html", {"request": request, "data": data})


@app.get("/lists/qemu", tags=["Get lists"])
async def get_list_of_qemu_images(request: Request):
    data = {
        "title": "Qemu images - ishare2",
        "command": get_qemu_list()
    }
    # return data
    return templates.TemplateResponse("pages/lists/qemu_list.html", {"request": request, "data": data})


@app.get("/download/bin/{id}", tags=["Download images"])
async def download_bin(id, request: Request):
    data = {
        "title": "Download bin image - ishare2",
        "command": download_bin_image(id)
    }
    # return data
    return templates.TemplateResponse("confirmation/after_download_bin.html", {"request": request, "data": data})


@app.get("/delete/bin/{name}", tags=["Delete images"])
async def delete_bin(name, request: Request):
    data = {
        "title": "Delete bin image - ishare2",
        "command": delete_bin_image(name)
    }
    # return data
    return templates.TemplateResponse("confirmation/after_delete_bin.html", {"request": request, "data": data})


@app.get("/download/dynamips/{id}", tags=["Download images"])
async def download_dynamips(id, request: Request):
    data = {
        "title": "Download dynamips image - ishare2",
        "command": download_dynamips_image(id)
    }
    # return data
    return templates.TemplateResponse("confirmation/after_download_dynamips.html", {"request": request, "data": data})


@app.get("/delete/dynamips/{name}", tags=["Delete images"])
async def delete_dynamips(name, request: Request):
    data = {
        "title": "Delete dynamips image - ishare2",
        "command": delete_dynamips_image(name)
    }
    # return data
    return templates.TemplateResponse("confirmation/after_delete_dynamips.html", {"request": request, "data": data})


@app.get("/download/qemu/{id}", tags=["Download images"])
async def download_qemu(id, request: Request):
    data = {
        "title": "Download qemu image - ishare2",
        "command": download_qemu_image(id)
    }
    # return data
    return templates.TemplateResponse("confirmation/after_download_qemu.html", {"request": request, "data": data})


@app.get("/delete/qemu/{foldername}", tags=["Delete images"])
async def delete_qemu(foldername, request: Request):
    data = {
        "title": "Delete qemu image - ishare2",
        "command": delete_qemu_image(foldername)
    }
    # return data
    return templates.TemplateResponse("confirmation/after_delete_qemu.html", {"request": request, "data": data})


@app.get("/delete/docker/{image_id}", tags=["Delete images"])
async def delete_docker(image_id, request: Request):
    data = {
        "title": "Delete docker image - ishare2",
        "command": delete_docker_image(image_id)
    }
    # return data
    return templates.TemplateResponse("confirmation/after_delete_docker.html", {"request": request, "data": data})


@app.get("/installed/bin", tags=["Get installed images"])
async def get_installed_bin(request: Request):
    data = {
        "title": "Installed bin images - ishare2",
        "command": get_installed_bin_images()
    }
    # return data
    return templates.TemplateResponse("components/utils/display_installed/installed_bin_images.html", {"request": request, "data": data})


@app.get("/installed/dynamips", tags=["Get installed images"])
async def get_installed_dynamips(request: Request):
    data = {
        "title": "Installed dynamips images - ishare2",
        "command": get_installed_dynamips_images()
    }
    # return data
    return templates.TemplateResponse("components/utils/display_installed/installed_dynamips_images.html", {"request": request, "data": data})


@app.get("/installed/qemu", tags=["Get installed images"])
async def get_installed_qemu(request: Request):
    data = {
        "title": "Installed qemu images - ishare2",
        "command": get_installed_qemu_images()
    }
    # return data
    return templates.TemplateResponse("components/utils/display_installed/installed_qemu_images.html", {"request": request, "data": data})


@app.get("/installed/docker", tags=["Get installed images"])
async def get_installed_docker(request: Request):
    data = {
        "title": "Installed docker images - ishare2",
        "command": get_installed_docker_images()
    }
    # return data
    return templates.TemplateResponse("components/utils/display_installed/installed_docker_images.html", {"request": request, "data": data})


@app.get("/live_search/bin", tags=["Live search"])
async def live_search_bin(q, request: Request):
    data = {
        "title": "Live search bin images - ishare2",
        "command": live_search_bin_image(q)
    }
    # return data
    return templates.TemplateResponse("live_search/live_search_bin.html", {"request": request, "data": data})


@app.get("/live_search/dynamips", tags=["Live search"])
async def live_search_dynamips(q, request: Request):
    data = {
        "title": "Live search dynamips images - ishare2",
        "command": live_search_dynamips_image(q)
    }
    # return data
    return templates.TemplateResponse("live_search/live_search_dynamips.html", {"request": request, "data": data})


@app.get("/live_search/qemu", tags=["Live search"])
async def live_search_qemu(q, request: Request):
    data = {
        "title": "Live search qemu images - ishare2",
        "command": live_search_qemu_image(q)
    }
    # return data
    return templates.TemplateResponse("live_search/live_search_qemu.html", {"request": request, "data": data})


@app.get("/relicense", tags=["Extras"])
async def get_relicensed(request: Request):
    data = {
        "title": "Relicense - ishare2",
        "command": relicense()
    }
    # return data
    return templates.TemplateResponse("confirmation/after_relicense.html", {"request": request, "data": data})


@app.get("/changelogs/ishare2", tags=["Changelogs"])
async def get_changelog_file(request: Request):
    data = {
        "title": "Changelog - ishare2",
        "command": get_changelog_content()
    }
    # return data
    return templates.TemplateResponse("pages/changelog_ishare2.html", {"request": request, "data": data})


@app.get("/changelogs/gui", tags=["Changelogs"])
async def get_changelog_gui_file(request: Request):
    data = {
        "title": "Changelog - ishare2",
        "command": get_changelog_gui_content()
    }
    # return data
    return templates.TemplateResponse("pages/changelog.html", {"request": request, "data": data})


@app.get("/help", tags=["Extras"])
async def get_help_file(request: Request):
    data = get_help_content()
    # return data
    return templates.TemplateResponse("pages/help.html", {"request": request, "data": data})


if __name__ == "__main__":
    config = get_credentials()
    HOST = config["api"]["host"]
    PORT = config["api"]["port"]

    uvicorn.run(
        "main:app",
        host=HOST,
        port=PORT,
        reload=True,
        workers=4,
    )
