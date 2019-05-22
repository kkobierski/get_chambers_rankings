"""
settings module for the app
"""

FIRMS_LIST = [111,7821, 126396, 250204]
FIRM_ID = FIRMS_LIST[0]
PUBLICATION_ID = 2


def get_url_firm():
    """
    returning proper url for company feed
    """
    return (
        f"https://api.chambers.com/api/organisations/{FIRM_ID}/"
        f"ranked-departments?publicationTypeId={PUBLICATION_ID}"
    )

def get_url_individual():
    """
    returning proper url for company feed
    """
    return (
        f"https://api.chambers.com/api/organisations/{FIRM_ID}/"
        f"ranked-lawyers?publicationTypeId={PUBLICATION_ID}"
    )
