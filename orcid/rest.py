import requests

from .exceptions import NotFoundException
from .constants import ORCID_PUBLIC_BASE_URL 

BASE_HEADERS = {'Accept':'application/orcid+json'}

class Author(dict):
    @property
    def orcid(self):
        """
        An author's ORCID profile identifier, or None if not found in the
        backing dict.
        """
        return self.get('orcid-profile',{}).get('orcid',{}).get('value', None)

def get(orcid_id):
    """
    Get an author based on an ORCID identifier.
    """
    resp = requests.get(ORCID_PUBLIC_BASE_URL + unicode(orcid_id),
                        headers=BASE_HEADERS)
    json_body = resp.json
    return Author(json_body)

def search(query):
    resp = requests.get(ORCID_PUBLIC_BASE_URL + 'search/orcid-bio',
                        params={'q':unicode(query)}, headers=BASE_HEADERS)
    json_body = resp.json
    return (Author(res) for res in json_body.get('orcid-search-results', {})\
            .get('orcid-search-result'))
