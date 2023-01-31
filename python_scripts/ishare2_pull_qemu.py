from .command_utils import _run_command


def download_qemu_image(id):
    command = f'ishare2 pull qemu {id}'
    output = _run_command(command)

    if "Fix permissions command has been applied" in output:
        return {
            "id": id,
            "status": 1,
            "message": "Image has been downloaded successfully.",
            "type": "qemu"
        }
    elif "already exists in server" in output:
        return {
            "id": id,
            "status": 0,
            "message": "Image already exists in server and cannot be downloaded twice.",
            "type": "qemu"
        }
    else:
        return {
            "id": id,
            "status": -1,
            "message": f"Failed to download image with error: {output}",
            "type": "qemu"
        }
