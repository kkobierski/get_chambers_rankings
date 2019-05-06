import csv

import requests

URL_T2 = 'https://api.chambers.com/api/organisations/250204/ranked-lawyers?publicationTypeId=2'
URL_T7 = 'https://api.chambers.com/api/organisations/111/ranked-lawyers?publicationTypeId=7'



def translate_chambers_json(data):
    _cur_desc = data["description"]

for i in data:
    row_array = []
    
    row_array.append(data["description"])


                        _cur_rank_desc = ranking["rankingDescription"]

                    yield [
                        _cur_desc,
                        _cur_type,
                        _cur_practice_id,
                        _cur_practice_desc,
                        _cur_loc_id,
                        _cur_loc_desc,
                        _cur_person_id,
                        _cur_person_name,
                        _cur_rank_desc
                    ]


if __name__ == '__main__':
    try:
        data = requests.get(URL_T7).json()
    except Exception:
        raise SystemExit('**Something** went wrong, debug it fool!')

    with open('data.csv', 'w') as file_obj:
        csv_writer = csv.writer(file_obj)

        for row in translate_chambers_json(data):
            csv_writer.writerow(row)
