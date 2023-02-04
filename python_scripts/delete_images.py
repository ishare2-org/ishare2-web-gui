from .command_utils import _run_command

NOT_FOUND_MSG = "The image has not been found in the system."
DELETED_SUCCESS_MSG = "The image has been deleted successfully from the system."
UNETLAB_PATH = "/opt/unetlab/addons"


def delete_image(id, image_type):
    match image_type:
        case "bin":
            CHECK_FILE_EXISTS_COMMAND = f'ls {UNETLAB_PATH}/addons/iol/bin | grep {id}'
            DELETE_COMMAND = f'rm {UNETLAB_PATH}/iol/bin/{id}'
        case "dynamips":
            CHECK_FILE_EXISTS_COMMAND = f'ls {UNETLAB_PATH}/dynamips | grep {id}'
            DELETE_COMMAND = f'rm {UNETLAB_PATH}/dynamips/{id}'
        case "qemu":
            CHECK_FILE_EXISTS_COMMAND = f'ls {UNETLAB_PATH}/qemu | grep {id}'
            DELETE_COMMAND = f'rm {UNETLAB_PATH}/qemu/{id}'
        case "docker":
            CHECK_FILE_EXISTS_COMMAND = f'docker images | grep {id}'
            DELETE_COMMAND = f'docker rmi {id}'

    retcode, stdout, stderr = _run_command(CHECK_FILE_EXISTS_COMMAND)
    if retcode != 0:
        return {
            "name": id,
            "status": 0,
            "message": NOT_FOUND_MSG
        }

    retcode, stdout, stderr = _run_command(DELETE_COMMAND)
    if retcode == 0:
        return {
            "name": id,
            "status": 1,
            "message": DELETED_SUCCESS_MSG
        }
    else:
        return {
            "name": id,
            "status": 0,
            "message": stderr
        }
