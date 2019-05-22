import csv

import requests

import settings as settings
from libs.translate_chambers_json import (translate_chambers_json_firm,
                                          translate_chambers_json_individual)

FIRMS_LIST = settings.FIRMS_LIST

for firm in FIRMS_LIST:
    FIRM_ID = firm
    URL_FIRM = settings.get_url_firm()
    URL_INDIVIDUAL = settings.get_url_individual()
    
    if __name__ == '__main__':
        try:
            data = requests.get(URL_INDIVIDUAL).json()
        except Exception:
            raise SystemExit('**Something** went wrong, debug it fool!')
    
        with open('data/individuals_{}.csv'.format(FIRM_ID), 'w') as file_obj:
            csv_writer = csv.writer(file_obj)
    
            for row in translate_chambers_json_individual(data):
                csv_writer.writerow(row)
    
        try:
            data = requests.get(URL_FIRM).json()
        except Exception:
            raise SystemExit('**Something** went wrong, debug it fool!')
    
        with open('data/firm_{}.csv'.format(FIRM_ID), 'w') as file_obj:
            csv_writer = csv.writer(file_obj)
    
            for row in translate_chambers_json_firm(data):
                csv_writer.writerow(row)
