from fastapi import APIRouter
from python_scripts.delete_images import delete_image

router = APIRouter()
IMAGE_TYPES = ["bin", "dynamips", "qemu", "docker"]

for image_type in IMAGE_TYPES:
    @router.get(f"/delete/{image_type}/{{id}}", tags=["Delete images"])
    async def delete_image_type(id, image_type=image_type):
        result = delete_image(id, image_type)
        return result
