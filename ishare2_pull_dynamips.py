import subprocess


def download_dynamips_image(id):
    command = f'ishare2 pull dynamips {id}'
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout:
        output = line.decode()
        print(output)
    
    if "Fix permissions command has been applied" in output:
        return {
            "id": id,
            "status": 1,
            "message": "Image has been downloaded successfully",
            "type": "Dynamips"
        } 

    if "already exists in server" in output:
        return {
            "id": id,
            "status": 0,
            "message": "Image already exists in server and cannot be downloaded twice",
            "type": "Dynamips"
        }
