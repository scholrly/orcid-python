A simple wrapper around the ORCID.org API.

Example
=======

Here's a quick snippet to get info on `John Wilbanks`_. ::

    import orcid

    #retrieve john's profile from his ORCID
    author = orcid.get('0000-0002-4510-0385')
    print author.family_name

If you'd rather search for authors, try ORCID's search functionality::

    >>> #do a simple author search for john
    >>> authors = orcid.search('john wilbanks')
    >>> print next(authors).family_name
    'wilbanks'

More Complicated Searches
=========================

You can also accomplish more complex queries using `Q` objects::

    >>> from orcid import Q
    >>> authors = orcid.search(Q('given-name','john') & Q('family-name', 'wilbanks'))
    >>> print next(authors).family_name
    'wilbanks'

Enjoy!

.. _John Wilbanks: http://en.wikipedia.org/wiki/John_Wilbanks