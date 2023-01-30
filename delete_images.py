import subprocess


def delete_bin_image(name):
    check_file_exists_command = f'ls /opt/unetlab/addons/iol/bin | grep {name}'
    p = subprocess.Popen(check_file_exists_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = []
    for line in p.stdout:
        output = line.decode()
    if not output:
        return {
            "name": name,
            "status": 0,
            "message": "Image has not been found in server"
        }

    command = f'rm /opt/unetlab/addons/iol/bin/{name}'
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = [] 
    for line in p.stdout:
        output = line.decode()
    if not output:
        return {
            "name": name,
            "status": 1,
            "message": "Image has been deleted successfully"
        }

def delete_dynamips_image(name):
    check_file_exists_command = f'ls /opt/unetlab/addons/dynamips | grep {name}'
    p = subprocess.Popen(check_file_exists_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = []
    for line in p.stdout:
        output = line.decode()

    if not output:
        check_file_exists_command = f'ls /opt/unetlab/addons/dynamips | grep -v {name}'
        p = subprocess.Popen(check_file_exists_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = []
        flag = 0
        for line in p.stdout:
            output = line.decode()
            flag = 1

    if not output:
        return {
            "name": name,
            "status": 0,
            "message": "Image has not been found in server"
        }

    command = f'rm /opt/unetlab/addons/dynamips/{name}'
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = []
    for line in p.stdout:
        output = line.decode()
    if not output:
        return {
            "name": name,
            "status": 1,
            "message": "Image has been deleted successfully"
        }

def delete_qemu_image(foldername):
    check_folder_exists_command = f'ls /opt/unetlab/addons/qemu | grep {foldername}'
    p = subprocess.Popen(check_folder_exists_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = []
    for line in p.stdout:
        output = line.decode()
    if not output:
        return {
            "name": foldername,
            "status": 0,
            "message": "Image has not been found in server"
        }

    command = f'rm -rf /opt/unetlab/addons/qemu/{foldername}'
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = []
    for line in p.stdout:
        output = line.decode()
    if not output:
        return {
            "name": foldername,
            "status": 1,
            "message": "Image has been deleted successfully"
        }

def delete_docker_image(image_id):
    command = f'docker rmi {image_id}'
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = [] 
    for line in p.stdout:
        output = line.decode()

    if "No such image" in output:
        return {
            "status": 0,
            "image_id": image_id,
            "message": "Image not found in server"
        }        

    if output:
        return {
            "status": 1,
            "image_id": image_id,
            "message": "Image has been deleted successfully"
        }
