import csv
import requests

from collections import defaultdict
from .misc_utils import get_config


def get_qemu_list():
    config = get_config()
    QEMU_ID = config["credentials"]["qemu_sheet_id"]
    GOOGLE_SHEETS_ID = config["credentials"]["google_sheet_id"]

    URL_QEMU_FILE = "https://docs.google.com/spreadsheets/d/e/" + \
        GOOGLE_SHEETS_ID + "/pub?gid=" + \
        str(QEMU_ID) + "&single=true&output=csv"

    response = requests.get(URL_QEMU_FILE)
    response_text = response.text

    reader = csv.reader(response_text.splitlines())
    header = next(reader)
    data_no_headers = list(reader)

    final_list = []
    for element in data_no_headers:
        d = defaultdict(str)
        d["foldername"] = element[1]
        d["size"] = float(element[2])
        d["unit"] = element[3]
        d["filename1"] = element[4]
        d["filelink1"] = element[5]
        d["filename2"] = element[6]
        d["filelink2"] = element[7]
        d["filename3"] = element[8]
        d["filelink3"] = element[9]
        d["filename4"] = element[10]
        d["filelink4"] = element[11]
        d["filename5"] = element[12]
        d["filelink5"] = element[13]
        d["filename6"] = element[14]
        d["filelink6"] = element[15]
        final_list.append(d)
    return final_list
