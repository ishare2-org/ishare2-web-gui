from ishare2_search_bin import get_bin_list
from ishare2_search_dynamips import get_dynamips_list
from ishare2_search_qemu import get_qemu_list


def live_search_bin_image(q):
    data = get_bin_list()

    dictionary = {}
    final_list = []
    for value in data:
        if q in value["name"]:
            dictionary = {
                "name": value["name"], 
                "size": value["size"], 
                "unit": value["unit"]
            }
            final_list.append(dictionary)
    return final_list


def live_search_dynamips_image(q):
    data = get_dynamips_list()
    
    dictionary = {}
    final_list = []
    for value in data:
        if q in value["name"]:
            dictionary = {
                "name": value["name"], 
                "size": value["size"], 
                "unit": value["unit"]
            }
            final_list.append(dictionary)
    return final_list


def live_search_qemu_image(q):
    data = get_qemu_list()

    dictionary = {}
    final_list = []
    for value in data:
        if q in value["foldername"]:
            dictionary = {
                "name": value["foldername"], 
                "size": value["size"], 
                "unit": value["unit"]
            }
            final_list.append(dictionary)
    return final_list