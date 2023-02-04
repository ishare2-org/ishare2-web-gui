import os.path
import csv
from python_scripts.download_csv import download_csv
from collections import defaultdict
from .misc_utils import get_config


def get_qemu_list():
    config = get_config()
    CSV_PATH = config["credentials"]["csv_path"]
    QEMU_CSV = os.path.join(CSV_PATH, "qemu.csv")

    if not os.path.exists(QEMU_CSV):
        download_csv()

    with open(QEMU_CSV, "r") as f:
        csv_file = csv.reader(f, delimiter=',')
        header = next(csv_file)
        data_no_headers = list(csv_file)

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
