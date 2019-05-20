"""
settings module for the app
"""

FIRM_ID = 111
PUBLICATION_ID = 2


def get_url_firm():
    """
    returning proper url for company feed
    """
    return (
        f"https://api.chambers.com/api/organisations/{FIRM_ID}/"
        f"ranked-departments?publicationTypeId={PUBLICATION_ID}"
    )
