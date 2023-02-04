from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from python_scripts.add_context import add_context
from python_scripts.ishare2_search_bin import get_bin_list
from python_scripts.ishare2_search_dynamips import get_dynamips_list
from python_scripts.ishare2_search_qemu import get_qemu_list
import os

router = APIRouter()

templates = Jinja2Templates(
    directory=os.getenv("TEMPLATES_DIR", "web_app/src"))


@router.get("/download/bin", tags=["download"])
async def get_list_of_bin_images(request: Request):
    data = {
        "title": "Bin images - ishare2",
        "command": get_bin_list()
    }
    context = {}
    context = add_context(context, request, data)
    return templates.TemplateResponse("pages/lists/bin_list.html", context)


@router.get("/download/dynamips", tags=["download"])
async def get_list_of_dynamips_images(request: Request):
    data = {
        "title": "Dynamips images - ishare2",
        "command": get_dynamips_list()
    }
    context = {}
    context = add_context(context, request, data)
    return templates.TemplateResponse("pages/lists/dynamips_list.html", context)


@router.get("/download/qemu", tags=["download"])
async def get_list_of_qemu_images(request: Request):
    data = {
        "title": "Qemu images - ishare2",
        "command": get_qemu_list()
    }
    context = {}
    context = add_context(context, request, data)
    return templates.TemplateResponse("pages/lists/qemu_list.html", context)
