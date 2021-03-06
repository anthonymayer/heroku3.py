# -*- coding: utf-8 -*-

"""
heroku3.core
~~~~~~~~~~~

This module provides the base entrypoint for heroku3.py.
"""

import requests

from .api import Heroku


def from_key(api_key, session=None, **kwargs):
    """Returns an authenticated Heroku instance, via API Key."""
    if not session:
        session = requests.session()
    # If I'm being passed an API key then I should use only this api key
    # if trust_env=True then Heroku will silently fallback to netrc authentication

    session.trust_env = False
    h = Heroku(session=session, **kwargs)

    # Login.
    h.authenticate(api_key)

    return h
