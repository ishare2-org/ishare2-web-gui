from .misc_utils import get_config, get_version, iol_license, ishare2_cli_version, is_root
import requests


def add_context(context: dict, request, data: dict):
    config = get_config()
    URL_ISHARE2_VERSION = config["constants"]["ishare2_version"]
    context["data"] = data
    context["is_root"] = is_root()
    context["request"] = request
    context["ishare_version"] = requests.get(URL_ISHARE2_VERSION).text
    context["emulator_version"] = get_version()
    context["iol_license"] = iol_license()
    context["ishare2_cli_version"] = ishare2_cli_version()
    context["footer_title"] = config["footer"]["title"]
    context["footer_text"] = config["footer"]["text"]
    context["footer_company"] = config["footer"]["company"]
    context["footer_company_link"] = config["footer"]["company_link"]
    context["github_link"] = config["social_media"]["links"]["github"]
    context["github_icon"] = config["social_media"]["icons"]["github"]
    context["telegram_link"] = config["social_media"]["links"]["telegram"]
    context["telegram_icon"] = config["social_media"]["icons"]["telegram"]
    context["support_link"] = config["social_media"]["links"]["support"]
    context["support_icon"] = config["social_media"]["icons"]["support"]
    context["footer_menu"] = config["footer"]["menu"]
    context["navbar"] = config["navbar"]
    context["nav_items"] = context["navbar"]["menu"]
    context["dropdown"] = config["navbar"]["dropdown"]
    context["dropdown_menu"] = context["dropdown"]["menu"]
    context["dropdown_submenu"] = context["dropdown"]["sub_menu"]
    context["metatags"] = config["metatags"]

    return context
