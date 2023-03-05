from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from python_scripts.misc_utils import get_changelog_content
from python_scripts.add_context import add_context
import os

router = APIRouter()

templates = Jinja2Templates(
    directory=os.getenv("TEMPLATES_DIR", "web_app/src"))

CHANGELOGS = ["ishare2-cli", "ishare2-gui"]

for changelog in CHANGELOGS:
    @router.get(f"/changelogs/{changelog}/", tags=["changelogs"])
    async def changelogs(request: Request, chagelog=changelog):
        data = {
            "title": f"Changelog - {changelog}",
            "url": get_changelog_content(chagelog)
        }
        context = {}
        context = add_context(context, request, data)
        return templates.TemplateResponse("pages/changelogs.html", context)
