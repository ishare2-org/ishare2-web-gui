from .ishare2_search_bin import get_bin_list
from .ishare2_search_dynamips import get_dynamips_list
from .ishare2_search_qemu import get_qemu_list


def live_search(q):
    results = []

    results += live_search_bin_image(q)
    results += live_search_dynamips_image(q)
    results += live_search_qemu_image(q)

    return results


def live_search_bin_image(q):
    data = get_bin_list()
    return [
        {
            "name": value["name"],
            "size": value["size"],
            "unit": value["unit"]
            "id": value["id"],
        } for value in data if q in value["name"]
    ]


def live_search_dynamips_image(q):
    data = get_dynamips_list()
    return [
        {
            "name": value["name"],
            "size": value["size"],
            "unit": value["unit"]
            "id": value["id"],
        } for value in data if q in value["name"]
    ]


def live_search_qemu_image(q):
    data = get_qemu_list()
    return [
        {
            "name": value["foldername"],
            "size": value["size"],
            "unit": value["unit"],
            "id": value["id"],
        } for value in data if q in value["foldername"]
    ]
