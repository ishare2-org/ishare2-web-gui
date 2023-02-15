from .command_utils import _run_command

NOT_FOUND_MSG = "The image has not been found in the system."
DELETED_SUCCESS_MSG = "The image has been deleted successfully from the system."
UNETLAB_PATH = "/opt/unetlab/addons"


def delete_image(id, image_type):
    if image_type == "bin":
        CHECK_FILE_EXISTS_COMMAND = f'ls {UNETLAB_PATH}/iol/bin/{id}'
        DELETE_COMMAND = f'rm -rf {UNETLAB_PATH}/iol/bin/{id}'

    elif image_type == "dynamips":
        CHECK_FILE_EXISTS_COMMAND = f'ls {UNETLAB_PATH}/dynamips/{id}'
        DELETE_COMMAND = f'rm -rf {UNETLAB_PATH}/dynamips/{id}'
    elif image_type == "qemu":
        CHECK_FILE_EXISTS_COMMAND = f'ls {UNETLAB_PATH}/qemu/{id}'
        DELETE_COMMAND = f'rm -rf {UNETLAB_PATH}/qemu/{id}'
    elif image_type == "docker":
        CHECK_FILE_EXISTS_COMMAND = f'docker images | grep {id}'
        DELETE_COMMAND = f'docker rmi {id}'
    else:
        # handle an invalid image_type value here
        raise ValueError("Invalid image_type specified")

    retcode, stdout, stderr = _run_command(CHECK_FILE_EXISTS_COMMAND)
    if retcode != 0:
        return {
            "name": id,
            "status": 1,
            "message": NOT_FOUND_MSG
        }

    retcode, stdout, stderr = _run_command(DELETE_COMMAND)
    if retcode == 0:
        return {
            "name": id,
            "status": 0,
            "message": DELETED_SUCCESS_MSG
        }
    else:
        return {
            "name": id,
            "status": 1,
            "message": stderr
        }
