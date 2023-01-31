from .command_utils import _run_command


def get_installed_bin_images():
    command = "ls -l /opt/unetlab/addons/iol/bin/ | awk '{ print $9 }'"
    retcode, stdout, stderr = _run_command(command)
    if retcode != 0:
        return []

    data = stdout.strip().split("\n")[1:]
    data = [d for d in data if "CiscoIOUKeygen.py" not in d and "iourc" not in d and "keepalive.pl" not in d]
    return [{"name": d} for d in data]
