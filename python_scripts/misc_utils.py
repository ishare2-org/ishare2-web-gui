import requests
import json
from .command_utils import _run_command


def is_root():
    retcode, stdout, stderr = _run_command("whoami")
    if retcode == 0 and stdout == "root":
        return "root"
    else:
        return stdout


def relicense():
    command = "ishare2 relicense"
    retcode, stdout, stderr = _run_command(command)
    if retcode == 0 and "Done" in stdout:
        command = "cat /opt/unetlab/addons/iol/bin/iourc"
        retcode, stdout, stderr = _run_command(command)
        if retcode == 0:
            license_value = stdout[10:-2]
            return {
                "status": 0,
                "message": "Relicense command has been applied successfully",
                "license_value": license_value
            }
        else:
            return {
                "status": 1,
                "message": "Failed to retrieve license value: {}".format(stderr),
            }
    else:
        return {
            "status": 1,
            "message": "Relicense command failed: {}".format(stderr),
        }


def get_config():
    with open('config.json', 'r') as f:
        return json.load(f)


def get_version():
    retcode, stdout, stderr = _run_command(
        "dpkg -l | grep pnetlab | head -n 1")
    if retcode == 0 and stdout != "":
        return "v{}".format(stdout.split()[2])
    else:
        return "N/A"


def ishare2_cli_version():
    retcode, stdout, stderr = _run_command(
        "cat /usr/sbin/ishare2_version")
    if retcode == 0 and stdout != "":
        return "{}".format(stdout)
    else:
        return "N/A"


def iol_license():
    retcode, stdout, stderr = _run_command(
        "cat /opt/unetlab/addons/iol/bin/iourc")
    if retcode == 0 and stdout != "":
        return stdout
    else:
        return "N/A"


def install_ishare2():
    command = "curl -o /usr/sbin/ishare2 https://raw.githubusercontent.com/pnetlabrepo/ishare2/main/ishare2 > /dev/null 2>&1 && chmod +x /usr/sbin/ishare2 && ishare2"
    retcode, stdout, stderr = _run_command(command)
    if retcode == 0 and "Done" in stdout:
        return {
            "status": 0,
            "message": "ishare2 has been installed successfully",
        }
    else:
        return {
            "status": 1,
            "message": "ishare2 installation failed: {}. {}".format(stderr, stdout),
        }


def get_changelog_content(changelog_type):
    if changelog_type == "ishare2-cli":
        return get_config()["constants"]["changelog_md_file"]
    elif changelog_type == "ishare2-gui":
        return get_config()["constants"]["changelog_gui_md_file"]
    else:
        raise Exception("Invalid changelog type", changelog_type)


def get_help_content():
    return get_config()["constants"]["help_md_file"]


def get_social_content():
    return get_config()["social"]


def downloader(url, file_name):
    with open(file_name, "wb") as file:
        response = requests.get(url)
        file.write(response.content)
