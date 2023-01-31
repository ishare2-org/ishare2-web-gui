from .command_utils import _run_command


def download_dynamips_image(id):
    command = f'ishare2 pull dynamips {id}'
    output = _run_command(command)

    if "Fix permissions command has been applied" in output:
        return {
            "id": id,
            "status": 1,
            "message": "Image has been downloaded successfully.",
            "type": "dynamips"
        }

    if "already exists in server" in output:
        return {
            "id": id,
            "status": 0,
            "message": "Image already exists in server and cannot be downloaded twice.",
            "type": "dynamips"
        }
    else:
        return {
            "id": id,
            "status": -1,
            "message": f"Image could not be downloaded. Error: {output}",
            "type": "bin"
        }
