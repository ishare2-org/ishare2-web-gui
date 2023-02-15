import os.path
import csv
from collections import defaultdict
from .misc_utils import get_config
from python_scripts.download_csv import download_csv


def get_images(image_type):
    config = get_config()
    CSV_PATH = config["credentials"]["csv_path"]

    if image_type == "bin":
        CSV_FILE = os.path.join(CSV_PATH, "bin.csv")

    elif image_type == "dynamips":
        CSV_FILE = os.path.join(CSV_PATH, "dynamips.csv")
    elif image_type == "qemu":
        CSV_FILE = os.path.join(CSV_PATH, "qemu.csv")
        return get_qemu_list(CSV_FILE)
    else:
        # handle an invalid image_type value here
        raise ValueError("Invalid image_type specified")

    if not os.path.exists(CSV_FILE):
        download_csv()
    with open(CSV_FILE, "r") as f:
        csv_file = csv.reader(f, delimiter=',')
        next(csv_file)

        final_list = []
        for row in csv_file:
            unit = row[3][:2] if len(row[3]) > 2 else row[3]
            final_list.append({
                "name": row[1],
                "link": row[2],
                "size": float(row[3]),
                "unit": row[4],
                "type": image_type
            })
        return final_list


def get_qemu_list(qemu_csv):
    QEMU_CSV = qemu_csv

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
            d["type"] = "qemu"
            final_list.append(d)
        return final_list
