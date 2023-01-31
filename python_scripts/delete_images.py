from .command_utils import _run_command

NOT_FOUND_MSG = "The image has not been found in the system"
DELETED_SUCCESS_MSG = "The image has been deleted successfully from the system"


def delete_bin_image(name):
    check_file_exists_command = f'ls /opt/unetlab/addons/iol/bin | grep {name}'
    retcode, stdout, stderr = _run_command(check_file_exists_command)
    if retcode != 0:
        return {
            "name": name,
            "status": 0,
            "message": NOT_FOUND_MSG
        }

    command = f'rm /opt/unetlab/addons/iol/bin/{name}'
    retcode, stdout, stderr = _run_command(command)
    if retcode == 0:
        return {
            "name": name,
            "status": 1,
            "message": DELETED_SUCCESS_MSG
        }
    else:
        return {
            "name": name,
            "status": 0,
            "message": stderr
        }


def delete_dynamips_image(name):
    check_file_exists_command = f'ls /opt/unetlab/addons/dynamips | grep {name}'
    retcode, stdout, stderr = _run_command(check_file_exists_command)
    if retcode != 0:
        return {
            "name": name,
            "status": 0,
            "message": NOT_FOUND_MSG
        }

    command = f'rm /opt/unetlab/addons/dynamips/{name}'
    retcode, stdout, stderr = _run_command(command)
    if retcode == 0:
        return {
            "name": name,
            "status": 1,
            "message": DELETED_SUCCESS_MSG
        }
    else:
        return {
            "name": name,
            "status": 0,
            "message": stderr
        }


def delete_qemu_image(foldername):
    check_folder_exists_command = f'ls /opt/unetlab/addons/qemu | grep {foldername}'
    retcode, stdout, stderr = _run_command(check_folder_exists_command)
    if retcode != 0:
        return {
            "name": foldername,
            "status": 0,
            "message": NOT_FOUND_MSG
        }

    command = f'rm -rf /opt/unetlab/addons/qemu/{foldername}'
    retcode, stdout, stderr = _run_command(command)
    if retcode == 0:
        return {
            "name": foldername,
            "status": 1,
            "message": DELETED_SUCCESS_MSG
        }
    else:
        return {
            "name": foldername,
            "status": 0,
            "message": stderr
        }


def delete_docker_image(image_id):
    command = f'docker rmi {image_id}'
    retcode, stdout, stderr = _run_command(command)
    if retcode == 0:
        return {
            "image_id": image_id,
            "status": 1,
            "message": DELETED_SUCCESS_MSG
        }
    else:
        return {
            "image_id": image_id,
            "status": 0,
            "message": stderr
        }
