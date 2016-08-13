#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ben Sledge'
SITENAME = u'Ben Sledge | 3D Technical Artist'
SITEURL = 'http://0.0.0.0:8000'

PLUGIN_PATH = ['../pelican-plugins']
PLUGINS = ['sitemap',
           # 'thumbnailer',
           'liquid_tags.img',
           'liquid_tags.youtube',
           'liquid_tags.vimeo',
           ]

MD_EXTENSIONS = ["codehilite(css_class=highlight)", "extra", "toc"]

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = u'en'

# Theme stuff
THEME = '../Flex'
SITELOGO = '/images/bensledge.jpg'
SITETITLE = 'Ben Sledge'
SITESUBTITLE = 'Rigging and Technical Artist'
COPYRIGHT_YEAR = '2010 - 2016'
MAIN_MENU = True
MENUITEMS = (('Archive', '/archive.html'),
             ('Sitemap', '/sitemap.xml'),)
LINKS = (('Projects', '/category/projects.html#projects'),
         ('Tags', '/tags.html#tags'),
         ('Email Me', 'mailto:bensledge3d@gmail.com'),)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
# USE_LESS = True

# sitemap settings
SITEMAP = {
        'format': 'xml'}

# thumbnailer settings


# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/bensledge3d/'),
          ('film', 'http://www.imdb.com/name/nm5492561/'),
          ('vimeo', 'https://vimeo.com/bensledge3d'),
          ('github', 'https://github.com/bensledge'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
