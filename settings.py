"""
settings module for the app
"""

FIRMS_LIST = [111, 7821, 126396, 250204]

PUBLICATION_ID = 2

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
