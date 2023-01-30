import json
import uvicorn
import requests

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from ishare2_search_bin import get_bin_list
from ishare2_search_dynamips import get_dynamips_list
from ishare2_search_qemu import get_qemu_list

from ishare2_pull_bin import download_bin_image
from ishare2_pull_dynamips import download_dynamips_image
from ishare2_pull_qemu import download_qemu_image

from ishare2_installed_bin import get_installed_bin_images
from ishare2_installed_dynamips import get_installed_dynamips_images
from ishare2_installed_qemu import get_installed_qemu_images
from ishare2_installed_docker import get_installed_docker_images

from delete_images import delete_bin_image
from delete_images import delete_dynamips_image
from delete_images import delete_qemu_image
from delete_images import delete_docker_image

from live_search_form import live_search_bin_image
from live_search_form import live_search_dynamips_image
from live_search_form import live_search_qemu_image

from extra_functions import relicense
from extra_functions import get_changelog_content
from extra_functions import get_changelog_gui_content
from extra_functions import get_help_content

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

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


def get_credentials():
    with open('config.json', 'r') as f:
        return json.load(f)


@app.get("/", response_class=HTMLResponse, tags=["Root"])
async def root(request: Request):
    config = get_credentials()
    URL_ISHARE2_VERSION = config["constants"]["ishare2_version"]

    ishare2_version = requests.get(URL_ISHARE2_VERSION).text

    data = {
        "version": ishare2_version,
        "extras1": "Field #1 to add more info",
        "extras2": "Field #2 to add more info",
        "extras3": "Field #3 to add more info"
    }
    # return data
    return templates.TemplateResponse("home.html", {"request": request, "data": data})


@app.get("/lists/bin", tags=["Get lists"])
async def get_list_of_bin_images(request: Request):
    data = get_bin_list()
    # return data
    return templates.TemplateResponse("lists/bin_list.html", {"request": request, "data": data})


@app.get("/lists/dynamips", tags=["Get lists"])
async def get_list_of_dynamips_images(request: Request):
    data = get_dynamips_list()
    # return data
    return templates.TemplateResponse("lists/dynamips_list.html", {"request": request, "data": data})


@app.get("/lists/qemu", tags=["Get lists"])
async def get_list_of_qemu_images(request: Request):
    data = get_qemu_list()
    # return data
    return templates.TemplateResponse("lists/qemu_list.html", {"request": request, "data": data})


@app.get("/download/bin/{id}", tags=["Download images"])
async def download_bin(id, request: Request):
    data = download_bin_image(id)
    # return data
    return templates.TemplateResponse("after/after_download_bin.html", {"request": request, "data": data})


@app.get("/delete/bin/{name}", tags=["Delete images"])
async def delete_bin(name, request: Request):
    data = delete_bin_image(name)
    # return data
    return templates.TemplateResponse("after/after_delete_bin.html", {"request": request, "data": data})


@app.get("/download/dynamips/{id}", tags=["Download images"])
async def download_dynamips(id, request: Request):
    data = download_dynamips_image(id)
    # return data
    return templates.TemplateResponse("after/after_download_dynamips.html", {"request": request, "data": data})


@app.get("/delete/dynamips/{name}", tags=["Delete images"])
async def delete_dynamips(name, request: Request):
    data = delete_dynamips_image(name)
    # return data
    return templates.TemplateResponse("after/after_delete_dynamips.html", {"request": request, "data": data})


@app.get("/download/qemu/{id}", tags=["Download images"])
async def download_qemu(id, request: Request):
    data = download_qemu_image(id)
    # return data
    return templates.TemplateResponse("after/after_download_qemu.html", {"request": request, "data": data})


@app.get("/delete/qemu/{foldername}", tags=["Delete images"])
async def delete_qemu(foldername, request: Request):
    data = delete_qemu_image(foldername)
    # return data
    return templates.TemplateResponse("after/after_delete_qemu.html", {"request": request, "data": data})


@app.get("/delete/docker/{image_id}", tags=["Delete images"])
async def delete_docker(image_id, request: Request):
    data = delete_docker_image(image_id)
    # return data
    return templates.TemplateResponse("after/after_delete_docker.html", {"request": request, "data": data})


@app.get("/installed/bin", tags=["Get installed images"])
async def get_installed_bin(request: Request):
    data = get_installed_bin_images()
    # return data
    return templates.TemplateResponse("installed/installed_bin_images.html", {"request": request, "data": data})


@app.get("/installed/dynamips", tags=["Get installed images"])
async def get_installed_dynamips(request: Request):
    data = get_installed_dynamips_images()
    # return data
    return templates.TemplateResponse("installed/installed_dynamips_images.html", {"request": request, "data": data})


@app.get("/installed/qemu", tags=["Get installed images"])
async def get_installed_qemu(request: Request):
    data = get_installed_qemu_images()
    # return data
    return templates.TemplateResponse("installed/installed_qemu_images.html", {"request": request, "data": data})


@app.get("/installed/docker", tags=["Get installed images"])
async def get_installed_docker(request: Request):
    data = get_installed_docker_images()
    # return data
    return templates.TemplateResponse("installed/installed_docker_images.html", {"request": request, "data": data})


@app.get("/live_search/bin", tags=["Live search"])
async def live_search_bin(q, request: Request):
    data = live_search_bin_image(q)
    # return data
    return templates.TemplateResponse("live_search/live_search_bin.html", {"request": request, "data": data})


@app.get("/live_search/dynamips", tags=["Live search"])
async def live_search_dynamips(q, request: Request):
    data = live_search_dynamips_image(q)
    # return data
    return templates.TemplateResponse("live_search/live_search_dynamips.html", {"request": request, "data": data})


@app.get("/live_search/qemu", tags=["Live search"])
async def live_search_qemu(q, request: Request):
    data = live_search_qemu_image(q)
    # return data
    return templates.TemplateResponse("live_search/live_search_qemu.html", {"request": request, "data": data})


@app.get("/relicense", tags=["Extras"])
async def get_relicensed(request: Request):
    data = relicense()
    # return data
    return templates.TemplateResponse("after/after_relicense.html", {"request": request, "data": data})


@app.get("/changelogs/ishare2", tags=["Changelogs"])
async def get_changelog_file(request: Request):
    data = get_changelog_content()
    # return data
    return templates.TemplateResponse("extras/changelog_ishare2.html", {"request": request, "data": data})


@app.get("/changelogs/gui", tags=["Changelogs"])
async def get_changelog_gui_file(request: Request):
    data = get_changelog_gui_content()
    # return data
    return templates.TemplateResponse("extras/changelog_gui.html", {"request": request, "data": data})


@app.get("/help", tags=["Extras"])
async def get_help_file(request: Request):
    data = get_help_content()
    # return data
    return templates.TemplateResponse("extras/help.html", {"request": request, "data": data})


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
