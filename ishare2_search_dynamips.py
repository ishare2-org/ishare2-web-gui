import requests
from pprint import pprint
import json


def get_credentials():
    with open('config.json', 'r') as f:
        return json.load(f)


def get_dynamips_list():
    config = get_credentials()
    DYNAMIPS_ID = config["credentials"]["dynamips_sheet_id"]
    GOOGLE_SHEETS_ID = config["credentials"]["google_sheet_id"]

    URL_DYNAMIPS_FILE = "https://docs.google.com/spreadsheets/d/e/" + GOOGLE_SHEETS_ID + "/pub?gid=" + str(DYNAMIPS_ID) + "&single=true&output=csv"

    response = requests.get(URL_DYNAMIPS_FILE)
    response_text = response.text

    data = response_text.split(",")
    data_no_headers = data[5:]
    data_list = [x.replace("\r\n","") for x in data_no_headers]

    a_list = data_list
    chunked_list = list()
    chunk_size = 4

    for i in range(0, len(a_list), chunk_size):
        chunked_list.append(a_list[i:i+chunk_size])

    dictionary = {}
    final_list = []
    for element in chunked_list:
        if len(element[3]) > 2:
            element[3] = element[3][:2]

        dictionary = {
            "name": element[0], 
            "link": element[1], 
            "size": float(element[2]), 
            "unit": element[3]
        }
        final_list.append(dictionary)
    return final_list