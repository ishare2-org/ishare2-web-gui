from .command_utils import _run_command


def get_installed_dynamips_images():
    command = "ls -l /opt/unetlab/addons/dynamips/ | awk '{ print $9 }'"
    retcode, stdout, stderr = _run_command(command)
    if retcode != 0:
        return []

    data = stdout.strip().split("\n")[1:]
    return [{"name": d} for d in data]
