"""
settings module for the app
"""

FIRMS_LIST = [111, 2692, 22401592, 7489, 257, 309, 130, 83]

PUBLICATION_ID = 1

COL_NAMES_CSV = ["desc", "practice_id", "practice_desc", "loc_id", "loc_desc", "person_id", "person_name", "rank_desc", "publication_id", "firm_id"]

#
#def get_url_firm(firm_id):
#    """
#    returning proper url for company feed
#    """
#    return (
#        f"https://api.chambers.com/api/organisations/{firm_id}/"
#        f"ranked-departments?publicationTypeId={PUBLICATION_ID}"
#    )
#
#
#def get_url_individual(firm_id):
#    """
#    returning proper url for company feed
#    """
#    return (
#        f"https://api.chambers.com/api/organisations/{firm_id}/"
#        f"ranked-lawyers?publicationTypeId={PUBLICATION_ID}"
#    )


def get_url(firm_id, is_firm=True):
    if is_firm:
        level = "departments"
    else:
        level = "lawyers"
    return (
        f"https://api.chambers.com/api/organisations/{firm_id}/"
        f"ranked-{level}?publicationTypeId={PUBLICATION_ID}"
    )
