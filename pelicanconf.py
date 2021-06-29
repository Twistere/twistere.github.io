#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from os import environ 

AUTHOR = 'Lucas Antunes'
SITENAME = 'Lucas blog'

if environ.get("BLOG_DEV") == "yes":
    SITEURL = 'http://localhost:8000'
    RELATIVE_URLS = True
elif environ.get("BLOG_DEV") == "no":
    SITEURL = 'https://twistere.github.io'
    RELATIVE_URLS = False
else:
    raise Exception(
        "On doit mettre BLOG_DEV à YES ou NO"
    )

PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5 