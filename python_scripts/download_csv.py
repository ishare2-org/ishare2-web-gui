import requests
import os.path
from .misc_utils import get_config


def downloader(url, file_name):
    with open(file_name, "wb") as file:
        response = requests.get(url)
        file.write(response.content)


def download_csv():
    config = get_config()
    CSV_PATH = config["credentials"]["csv_path"]
    GOOGLE_SHEETS_ID = config["credentials"]["google_sheet_id"]
    BIN_ID = config["credentials"]["bin_sheet_id"]
    QEMU_ID = config["credentials"]["qemu_sheet_id"]
    DYNAMIPS_ID = config["credentials"]["dynamips_sheet_id"]

    URL_BIN_FILE = f"https://docs.google.com/spreadsheets/d/e/{GOOGLE_SHEETS_ID}/pub?gid={BIN_ID}&single=true&output=csv"
    URL_QEMU_FILE = f"https://docs.google.com/spreadsheets/d/e/{GOOGLE_SHEETS_ID}/pub?gid={QEMU_ID}&single=true&output=csv"
    URL_DYNAMIPS_FILE = f"https://docs.google.com/spreadsheets/d/e/{GOOGLE_SHEETS_ID}/pub?gid={DYNAMIPS_ID}&single=true&output=csv"

    BIN_CSV = os.path.join(CSV_PATH, "bin.csv")
    QEMU_CSV = os.path.join(CSV_PATH, "qemu.csv")
    DYNAMIPS_CSV = os.path.join(CSV_PATH, "dynamips.csv")

    if not os.path.exists(CSV_PATH):
        os.makedirs(CSV_PATH)

    downloader(URL_BIN_FILE, BIN_CSV)
    downloader(URL_QEMU_FILE, QEMU_CSV)
    downloader(URL_DYNAMIPS_FILE, DYNAMIPS_CSV)