#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'p371k9'
SITENAME = 'Northwind Traders'
SITEURL = ""
FAVICON = 'images/favicon.ico'

PATH = 'content'
OUTPUT_PATH = 'output/'
STATIC_PATHS = [
    'images', 
    'robots.txt'
]

TIMEZONE = 'Europe/Budapest'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

"""
#INDEX_SAVE_AS = None
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''

#AUTHOR_SAVE_AS = ''
#CATEGORY_SAVE_AS = ''
"""

DIRECT_TEMPLATES = ['index', 'categories', 'search']


# Blogroll
LINKS = (('Microsoft Learn', 'https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/northwind-install'),
         ('Wiki','https://en.wikiversity.org/wiki/Database_Examples/Northwind'),
         ('Pelican', 'http://getpelican.com/'),)

# Social widget


SOCIAL = (('facebook', 'https://www.facebook.com/MicrosoftAccessProducts/posts/pfbid0RL6Tn6wuZrQvVpyLzaLFTpUSpX2WuAyY3RS7fwoJqgjzNUcwgEg3FaNZLVGphbkhl'),
            ('youtube','https://www.youtube.com/watch?v=i4mQ_7tj_gk'),
            ('linkedin', 'https://www.linkedin.com/posts/adam-wilbert_announcing-new-templates-for-microsoft-access-activity-7057179242425417729-fzIV'),
            ('github', 'https://github.com/p371k9/northwind'),)
            
DISPLAY_CATEGORIES_ON_MENU = True            
DISPLAY_PAGES_ON_MENU = True   
# sajnos nem emeli ki az aktuális oldal címét  MENUITEMS = (('Products by category', SITEURL+'/category/prodcat.html'),('Employees', SITEURL+'/category/employee.html'),('About', SITEURL+'/pages/about.html'))            

BOOTSTRAP_NAVBAR_INVERSE = True
#BOOTSTRAP_THEME = 'slate'

HIDE_SITENAME = True

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


THEME = "/home/pp/pelican-themes/pelican-bootstrap3"
THEME_TEMPLATES_OVERRIDES = ["themes/pelican-bootstrap3-overrides"]
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

PLUGIN_PATHS = ['/home/pp/pelican-plugins', "./plugins"]		# "/srv/pelican/plugins" , '/home/pp/pelican-plugins/tipue_search/pelican/plugins']
PLUGINS =["i18n_subsites", "nw", "sitemap"]	# ["tipue_search"]	# ["assets", "liquid_tags", "sitemap"]

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}
