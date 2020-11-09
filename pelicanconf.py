#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'siim juuse'
SITENAME = 'LOODUSHOOLDUS OÜ'
SITEURL = ''

PATH = 'content'
STATIC_PATH = 'images'
OUTPUT_PATH = 'docs/'

TIMEZONE = 'Europe/Tallinn'

DEFAULT_LANG = 'en'

THEME = 'themes/loodushooldus'

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Avaleht'

#PAGINATION

DEFAULT_PAGINATION = 10



#MENU

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Avaleht', '/pages/avaleht.html'),
    ('Teenused', '/pages/teenused.html'),
    ('Hinnakiri', '/pages/hinnakiri.html'),
    ('Kontakt', '/pages/kontakt.html')
    )
LOAD_CONTENT_CACHE = False  #WTF SEE SIIN TEEB <----

#JINJA_ENVIRONMENT = {'trim_blocks': True, 'lstrip_blocks': True}




# Feed generation is usually not desired when developing
FEED_ALL_ATOM = False
FEED_ALL_RSS = False
AUTHOR_FEED_RSS = False
RSS_FEED_SUMMARY_ONLY = False

# LINKS FOR WEBSITES
#LINKS = (('AHVID', 'www.ahvidonpuuotsas.ee'))


# Social media
#SOCIAL = (('You can add links in your config file', '#'),
#('Another social link', '#'),)


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True