A simple wrapper around the ORCID.org API.

Example
=======

Here's a quick snippet to get info on `John Wilbanks`_. ::

    import orcid

    #retrieve john's profile from his ORCID
    author = orcid.get('0000-0002-4510-0385')
    print author.family_name

    #do a simple author search for john
    authors = orcid.search('john wilbanks')
    print authors[0].family_name

Enjoy!

.. _John Wilbanks: http://en.wikipedia.org/wiki/John_Wilbanks