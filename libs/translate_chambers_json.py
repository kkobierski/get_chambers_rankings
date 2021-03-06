import settings as settings


def translate_chambers_json_individual(data, firm_id):
    _cur_desc = data["description"]
    _cur_firm_id = firm_id
    _cur_publication_id = settings.PUBLICATION_ID
    for group in data["groups"]:
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
                        _cur_practice_id,
                        _cur_practice_desc,
                        _cur_loc_id,
                        _cur_loc_desc,
                        _cur_person_id,
                        _cur_person_name,
                        _cur_rank_desc,
                        _cur_publication_id,
                        _cur_firm_id
                        ]


def translate_chambers_json_firm(data):
    _cur_desc = data["description"]
    for location in data["locations"]:
        _cur_loc_desc = location["description"]
        _cur_loc_id = location["id"]
        for firm in location["rankedEntities"]:
            _cur_firm_id = firm["organisationId"]
            _cur_practice_id = firm["practiceAreaId"]
            _cur_practice_desc = firm["displayName"]
            _cur_publication_id = firm["publicationTypeId"]
            for ranking in firm["rankings"]:
                _cur_rank_desc = ranking["rankingDescription"]

            yield [
                _cur_desc,
                _cur_practice_id,
                _cur_practice_desc,
                _cur_loc_id,
                _cur_loc_desc,
                _cur_rank_desc,
                _cur_publication_id,
                _cur_firm_id
                ]


def translate_json_data(for_firm, data):
    if for_firm:
        transalte_chambers_json_firm(data)
    else:
        transalte_chambers_json_firm(data)
