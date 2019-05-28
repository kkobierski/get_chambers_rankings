import csv

import requests

import settings as settings
from libs.translate_chambers_json import (translate_chambers_json_firm,
                                          translate_chambers_json_individual)

from libs.translate_chambers_json import translate_json_data

FIRMS_LIST = settings.FIRMS_LIST


def fetching_results_from_api(url):
    data = ""
    try:
        data = requests.get(url).json()
    except Exception:
        pass
    return data


def save_json_to_file(file_name, data):
    with open(file_name, 'w') as file_obj:
        csv_writer = csv.writer(file_obj)

        for row in translate_chambers_json_firm(data):
            csv_writer.writerow(row)


def get_api_data(firm_id, for_firm=True):
    level = 'firm' if for_firm else 'lawyers'
    url = settings.get_url(firm_id, for_firm)
    api_data = fetching_results_from_api(url)

    if api_data:
        save_json_to_file(f"data/{level}_{firm_id}.csv", api_data)


for firm in FIRMS_LIST:
    get_api_data(firm)
