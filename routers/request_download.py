from fastapi import APIRouter
from python_scripts.download_images import download_image

router = APIRouter()

IMAGE_TYPES = ["bin", "dynamips", "qemu", "docker"]


for image_type in IMAGE_TYPES:
    @router.get(f"/download/{image_type}/{{id}}", tags=["Download images"])
    async def download_image_type(id, image_type=image_type):
        result = download_image(id, image_type)
        return result
