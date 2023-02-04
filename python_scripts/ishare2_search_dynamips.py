import os.path
import csv
from .misc_utils import get_config
from python_scripts.download_csv import download_csv


def get_dynamips_list():
    config = get_config()
    CSV_PATH = config["credentials"]["csv_path"]
    DYNAMIPS_CSV = os.path.join(CSV_PATH, "dynamips.csv")

    if not os.path.exists(DYNAMIPS_CSV):
        download_csv()

    with open(DYNAMIPS_CSV, "r") as f:
        csv_file = csv.reader(f, delimiter=',')
        next(csv_file)

        final_list = []
        for row in csv_file:
            unit = row[3][:2] if len(row[3]) > 2 else row[3]
            final_list.append({
                "name": row[1],
                "link": row[2],
                "size": float(row[3]),
                "unit": unit
            })
    return final_list
