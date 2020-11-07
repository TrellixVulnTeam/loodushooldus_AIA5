#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'siim juuse'
SITENAME = 'loodushooldus'
SITEURL = ''

PATH = 'content'
STATIC_PATH = 'images'


TIMEZONE = 'Europe/Tallinn'

DEFAULT_LANG = 'en'

THEME = 'notmyidea'

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Avaleht'
DISPLAY_PAGES_ON_MENU = True



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# LINKS FOR WEBSITES
#LINKS = (('Pelican', 'https://getpelican.com/'),


# Social media
#SOCIAL = (('You can add links in your config file', '#'),
#('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True