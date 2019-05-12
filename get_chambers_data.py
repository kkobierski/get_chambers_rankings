import csv
import requests

firm_id = 250204
ranking_id = 2


url_firm = 'https://api.chambers.com/api/organisations/{}/ranked-lawyers?publicationTypeId={}'.format(firm_id,ranking_id)
url_individual = 'https://api.chambers.com/api/organisations/{}/ranked-departments?publicationTypeId={}'.format(firm_id,ranking_id)



def translate_chambers_json(data):
    _cur_desc = data["description"]
    for group in data["groups"]:
        _cur_type = group["type"]
        for practice in group["practiceAreas"]:
            _cur_practice_id = practice["id"]
            _cur_practice_desc = practice["description"]
            for location in practice["individualsInLocations"]:
                _cur_loc_id = location["id"]
                _cur_loc_desc = location["description"]
                for person in location["rankedEntities"]:
                    _cur_person_id = person["personOrganisationId"]
                    _cur_person_name = person["displayName"]
                    for ranking in person["rankings"]:
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
        data = requests.get(url_firm).json()
    except Exception:
        raise SystemExit('**Something** went wrong, debug it fool!')

    with open('firm.csv', 'w') as file_obj:
        csv_writer = csv.writer(file_obj)

        for row in translate_chambers_json(data):
            csv_writer.writerow(row)
