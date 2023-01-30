import subprocess
import json


def relicense():
    command = "ishare2 relicense"
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    data = []
    for line in p.stdout:
        output = line.decode()

    if "Done" in output:
        command = "cat /opt/unetlab/addons/iol/bin/iourc"
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        data = []
        for line in p.stdout:
            output2 = line.decode()
        license_value = output2[10:-2]
        
        return {
            "status": 1,
            "message": "Relicense command has been applied successfully",
            "license_value": license_value
        }
    else:
        return {
            "status": 0,
            "message": "Something went wrong",
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