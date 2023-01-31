from .command_utils import _run_command
import json


def relicense():
    command = "ishare2 relicense"
    retcode, stdout, stderr = _run_command(command)
    if retcode == 0 and "Done" in stdout:
        command = "cat /opt/unetlab/addons/iol/bin/iourc"
        retcode, stdout, stderr = _run_command(command)
        if retcode == 0:
            license_value = stdout[10:-2]
            return {
                "status": 1,
                "message": "Relicense command has been applied successfully",
                "license_value": license_value
            }
        else:
            return {
                "status": 0,
                "message": "Failed to retrieve license value: {}".format(stderr),
            }
    else:
        return {
            "status": 0,
            "message": "Relicense command failed: {}".format(stderr),
        }


def get_credentials():
    with open('config.json', 'r') as f:
        return json.load(f)


def get_changelog_content():
    return {
        "url": get_credentials()["constants"]["changelog_md_file"]
    }


def get_changelog_gui_content():
    return {
        "url": get_credentials()["constants"]["changelog_gui_md_file"]
    }


def get_help_content():
    return {
        "url": get_credentials()["constants"]["help_md_file"]
    }
