import subprocess


def get_installed_docker_images():
    command = "ishare2 installed docker"
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    data = []
    for line in p.stdout:
        output = line.decode()
        data.append(output)
    
    if "0 docker images found in server" in output:
        final_list = []
        return final_list

    data = data[3:-2]

    my_list = []
    for sub in data:
        my_list.append(sub.replace("\n", ""))

    dictionary = {}
    final_list = []
    for element in my_list:
        image = element.split()
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