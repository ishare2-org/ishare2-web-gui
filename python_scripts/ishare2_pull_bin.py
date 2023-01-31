from .command_utils import _run_command


def download_bin_image(id):
    command = f'ishare2 pull bin {id}'
    output = _run_command(command)
    if "Fix permissions command has been applied" in output:
        return {
            "id": id,
            "status": 1,
            "message": "Image has been downloaded successfully.",
            "type": "bin"
        }

    if "already exists in server" in output:
        return {
            "id": id,
            "status": 0,
            "message": "Image already exists in the server and cannot be downloaded twice.",
            "type": "bin"
        }
    else:
        return {
            "id": id,
            "status": -1,
            "message": f"Image could not be downloaded. Error: {output}",
            "type": "bin"
        }
