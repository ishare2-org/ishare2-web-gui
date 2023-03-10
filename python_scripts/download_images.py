from .command_utils import _run_command
PERMISSIONS_APPLIED = "Fix permissions command has been applied"
ALREADY_EXISTS = "already exists in server"
NOT_FOUND_MSG = "The image has not been found in the system."


def download_image(id, image_type):
    if image_type == "bin":
        COMMAND = f'ishare2 pull bin {id}'

    elif image_type == "dynamips":
        COMMAND = f'ishare2 pull dynamips {id}'
    elif image_type == "qemu":
        COMMAND = f'ishare2 pull qemu {id}'
    elif image_type == "docker":
        COMMAND = f'docker pull {id}'
    else:
        # handle an invalid image_type value here
        raise ValueError("Invalid image_type specified")

    retcode, stdout, stderr = _run_command(COMMAND)
    if PERMISSIONS_APPLIED in stdout:
        return {
            "id": id,
            "status": retcode,
            "message": "Image has been downloaded successfully.",
            "type": image_type
        }
    if ALREADY_EXISTS in stdout:
        return {
            "id": id,
            "status": retcode,
            "message": "Image already exists in the server and cannot be downloaded twice.",
            "type": image_type
        }
    if retcode != 0:
        return {
            "id": id,
            "status": retcode,
            "message": f"Image could not be downloaded. Error: {stderr}",
            "type": image_type
        }
