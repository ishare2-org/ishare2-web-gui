import subprocess


def get_installed_dynamips_images():
    command = "ls -l /opt/unetlab/addons/dynamips/ | awk '{ print $9 }'"
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    data = []
    for line in p.stdout:
        output = line.decode()
        data.append(output)
    
    data = data[1:]

    my_list = []
    for sub in data:
        my_list.append(sub.replace("\n", ""))

    dictionary = {}
    final_list = []
    for element in my_list:
        dictionary = {
            "name": element, 
        }
        final_list.append(dictionary)
    return final_list