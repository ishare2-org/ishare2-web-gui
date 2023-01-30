import requests
from pprint import pprint
import json


def get_credentials():
    with open('config.json', 'r') as f:
        return json.load(f)


def get_qemu_list():
    config = get_credentials()
    QEMU_ID = config["credentials"]["qemu_sheet_id"]
    GOOGLE_SHEETS_ID = config["credentials"]["google_sheet_id"]

    URL_QEMU_FILE = "https://docs.google.com/spreadsheets/d/e/" + GOOGLE_SHEETS_ID + "/pub?gid=" + str(QEMU_ID) + "&single=true&output=csv"

    response = requests.get(URL_QEMU_FILE)
    response_text = response.text

    clean = response_text.replace(',,,', '')

    data = response_text.split(",")
    data_no_headers = data[18:]
    data_list = [x.replace("\r\n","") for x in data_no_headers]

    a_list = data_list
    chunked_list = list()
    chunk_size = 18

    for i in range(0, len(a_list), chunk_size):
        chunked_list.append(a_list[i:i+chunk_size])

    new_list = []
    for element in chunked_list:
        element_modified = element[:-2]
        new_list.append(element_modified)

    del new_list[-1]

    dictionary = {}
    final_list = []
    for element in new_list:
        dictionary = {
            "foldername": element[1], 
            "size": float(element[2]), 
            "unit": element[3],
            "filename1": element[4],
            "filelink1": element[5],
            "filename2": element[6],
            "filelink2": element[7],
            "filename3": element[8],
            "filelink3": element[9],
            "filename4": element[10],
            "filelink4": element[11],
            "filename5": element[12],
            "filelink5": element[13],
            "filename6": element[14],
            "filelink6": element[15],
        }
        final_list.append(dictionary)
    return final_list