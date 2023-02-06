from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from python_scripts.add_context import add_context
from python_scripts.get_images import get_images
from python_scripts.get_images import get_qemu_list
import os

router = APIRouter()

templates = Jinja2Templates(
    directory=os.getenv("TEMPLATES_DIR", "web_app/src"))

IMAGE_TYPES = ["bin", "dynamips", "qemu", "docker"]


for image_type in IMAGE_TYPES:
    @router.get(f"/download/{image_type}", tags=["download"])
    async def get_image_type(request: Request, image_type=image_type):
        data = {
            "title": f"{image_type} images - ishare2",
            "command": get_images(image_type),
            "type": image_type
        }
        context = {}
        context = add_context(context, request, data)
        return templates.TemplateResponse("pages/download.html", context)


@router.get("/devices/", tags=["download"])
async def get_devices(request: Request):
    data = {
        "title": "Devices - ishare2",
    }
    context = {}
    context = add_context(context, request, data)
    return templates.TemplateResponse("pages/devices.html", context)
