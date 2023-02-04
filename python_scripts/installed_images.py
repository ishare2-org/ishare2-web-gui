import os
from .command_utils import _run_command


def get_installed_images(image_type):
    if image_type == "bin":
        COMMAND = "ls -l /opt/unetlab/addons/iol/bin/ | awk '{ print $9 }'"
    elif image_type == "dynamips":
        COMMAND = "ls -l /opt/unetlab/addons/dynamips/ | awk '{ print $9 }'"
    elif image_type == "qemu":
        COMMAND = "ls -l /opt/unetlab/addons/qemu/ | awk '{ print $9 }'"
    elif image_type == "docker":
        COMMAND = "ishare2 installed docker"
    else:
        return [None, "Error: Invalid image type provided."]

    retcode, stdout, stderr = _run_command(COMMAND)
    if retcode != 0:
        return []

    if image_type != "docker":
        result = []
        files = stdout.strip().split("\n")
        for file_name in files:
            result.append({"name": file_name})
        return result

    data = stdout.strip().split("\n")
    if "0 docker images found in server" in data[-1]:
        return []
    data = data[3:-2]
    final_list = []
    for sub in data:
        image = sub.split()
        dictionary = {
            "repository_name": image[0],
            "tag": image[1],
            "image_id": image[2],
            "created": image[3] + " " + image[4] + " " + image[5],
            "size": image[6][:-2],
            "unit": image[6][-2:]
        }
        final_list.append(dictionary)
    return [final_list]


def is_valid_file(file_name):
    return file_name.endswith((".image", ".bin")) or os.path.isdir(file_name)
