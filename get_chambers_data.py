import csv
import requests
from libs.translate_chambers_json import translate_chambers_json_individual
from libs.translate_chambers_json import translate_chambers_json_firm

firm_id = 111
publication_id = 2


url_firm = 'https://api.chambers.com/api/organisations/{}/ranked-departments?publicationTypeId={}'.format(firm_id,publication_id)
url_individual = 'https://api.chambers.com/api/organisations/{}/ranked-lawyers?publicationTypeId={}'.format(firm_id,publication_id)


if __name__ == '__main__':
    try:
        data = requests.get(url_individual).json()
    except Exception:
        raise SystemExit('**Something** went wrong, debug it fool!')

    with open('data/individuals_{}.csv'.format(firm_id), 'w') as file_obj:
        csv_writer = csv.writer(file_obj)

        for row in translate_chambers_json_individual(data):
            csv_writer.writerow(row)
   
    
    
    try:
        data = requests.get(url_firm).json()
    except Exception:
        raise SystemExit('**Something** went wrong, debug it fool!')


    with open('data/firm_{}.csv'.format(firm_id), 'w') as file_obj:
            csv_writer = csv.writer(file_obj)
    
            for row in translate_chambers_json_firm(data):
                csv_writer.writerow(row)