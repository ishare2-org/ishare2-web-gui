from .command_utils import _run_command


def get_installed_docker_images():
    command = "ishare2 installed docker"
    returncode, stdout, stderr = _run_command(command)
    if returncode != 0:
        return []
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
    return final_list
