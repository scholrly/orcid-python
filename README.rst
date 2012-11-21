orcid-python
============

A simple wrapper around the ORCID.org API.

Example
-------

    import orcid

    #retrieve an author
    author = orcid.get('0000-0002-4510-0385')
    print author['orcid-bio']['personal-details']['family-name']['value']

    #do a simple author search
    authors = orcid.search('john wilbanks')
    print authors[0]['orcid-bio']['personal-details']['family-name']['value']

Enjoy!
