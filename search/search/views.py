#!/usr/bin/python
# -*- coding: utf-8 -*-
""" Cornice services.
"""

import json
import logging
#import colander
#from cornice import Service
#from pyramid.response import Response
#from blog.app import app
#from blog.utility.exceptions import BlogException
#from blog.utility.functions import sanitize_payload


from pyramid.view import (
    view_config,
    view_defaults
    )
from apps import search_keywords 

@view_defaults()
class SearchViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home',renderer='/templates/home.jinja2')
    def home(self):
        return {'status': 'Home View'}

    @view_config(route_name='search',renderer='/templates/search.jinja2')
    def search(self):
        params = self.request.GET
        if 'keywords' in params:
            return search_keywords(params['keywords'])
        else:
            return {'status':400, 'msg':'keywords are missing'}