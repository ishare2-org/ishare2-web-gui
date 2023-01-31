import csv
import requests

from .misc_utils import get_credentials


def get_bin_list():
    config = get_config()
    BIN_ID = config["credentials"]["bin_sheet_id"]
    GOOGLE_SHEETS_ID = config["credentials"]["google_sheet_id"]

    URL_BIN_FILE = f"https://docs.google.com/spreadsheets/d/e/{GOOGLE_SHEETS_ID}/pub?gid={BIN_ID}&single=true&output=csv"

    response = requests.get(URL_BIN_FILE)
    response_text = response.text

    csv_file = csv.reader(response_text.splitlines(), delimiter=',')
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
