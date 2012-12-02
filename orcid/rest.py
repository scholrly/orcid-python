import requests

from .constants import ORCID_PUBLIC_BASE_URL
from .utils import dictmapper, MappingRule as to

from .exceptions import NotFoundException

BASE_HEADERS = {'Accept':'application/orcid+json'}

BIO_PATH = ['orcid-profile','orcid-bio']
PERSONAL_DETAILS_PATH = BIO_PATH + ['personal-details']

def _parse_keywords(d):
    # XXX yes, splitting on commas is bad- but a bug in ORCID
    # (https://github.com/ORCID/ORCID-Parent/issues/27) makes this the  best
    # way. will fix when they do
    if d is not None:
        return d.get('keyword',[{}])[0].get('value','').split(',')
    return []

AuthorBase = dictmapper('AuthorBase', {
    'orcid':['orcid-profile','orcid','value'],
    'family_name':PERSONAL_DETAILS_PATH + ['family-name','value'],
    'given_name':PERSONAL_DETAILS_PATH + ['given-names','value'],
    'biography':BIO_PATH + ['biography',],
    'keywords':to(BIO_PATH + ['keywords'], _parse_keywords)
})

class Author(AuthorBase):
    pass

Citation = dictmapper('Citation', {
    'citation':['citation'],
    'citation_type':['work-citation-type']
})

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
