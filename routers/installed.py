import os
from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates
from python_scripts.installed_images import get_installed_images
from python_scripts.add_context import add_context

router = APIRouter()

templates = Jinja2Templates(
    directory=os.getenv("TEMPLATES_DIR", "web_app/src"))

IMAGE_TYPES = ["bin", "dynamips", "qemu", "docker"]
for image_type in IMAGE_TYPES:
    @router.get(f"/installed/{image_type}", tags=["Get installed images"])
    async def get_installed_image_type(request: Request, image_type=image_type):
        data = {
            "title": f"Installed {image_type} images - ishare2",
            "command": get_installed_images(image_type),
            "type": image_type
        }
        context = {}
        context = add_context(context, request, data)
        return templates.TemplateResponse("components/utils/display_installed/installed.html", context)
