import requests
import time
import os.path
from .misc_utils import get_config, downloader


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

    # Check if the files exist
    if os.path.exists(BIN_CSV) and os.path.exists(QEMU_CSV) and os.path.exists(DYNAMIPS_CSV):
        # Check if files are older than 30 minutes
        if os.path.getmtime(BIN_CSV) < time.time() - 1800:
            downloader(URL_BIN_FILE, BIN_CSV)
        if os.path.getmtime(QEMU_CSV) < time.time() - 1800:
            downloader(URL_QEMU_FILE, QEMU_CSV)
        if os.path.getmtime(DYNAMIPS_CSV) < time.time() - 1800:
            downloader(URL_DYNAMIPS_FILE, DYNAMIPS_CSV)
    # If files don't exist, download them
    else:
        downloader(URL_BIN_FILE, BIN_CSV)
        downloader(URL_QEMU_FILE, QEMU_CSV)
        downloader(URL_DYNAMIPS_FILE, DYNAMIPS_CSV)
