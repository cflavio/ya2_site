#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Flavio Calva'
SITENAME = u'Ya2 indie game developer'
SITETITLE = 'Ya2'
SITESUBTITLE = 'indie game developer'
SITEURL = 'http://www.ya2.it'
SITEDESCRIPTION = "Ya2's games"
SITELOGO = SITEURL + '/images/logo.png'
FAVICON = SITEURL + '/images/favicon.ico'
ADD_THIS_ID = 'ya2at'
SUMMARY_MAX_LENGTH = 80
DEFAULT_CATEGORY = 'news'
PATH = 'content'
TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = u'en'
LOAD_CONTENT_CACHE = False
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
PAGE_ORDER_BY = 'sort'
PAGES_SORT_ATTRIBUTE = 'sort'
SOCIAL = (
    ('twitter', 'http://twitter.com/ya2tech'),
    ('facebook', 'http://www.facebook.com/Ya2Tech'),
    ('youtube', 'http://www.youtube.com/user/ya2games'),
    ('pinterest', 'http://www.pinterest.com/ya2tech'),
    ('tumblr', 'http://ya2tech.tumblr.com/'),
    ('rss', SITEURL + '/pages/feed-following.html'),
    ('github', 'https://github.com/cflavio'),)
DEFAULT_PAGINATION = 5
DEFAULT_DATE = 'fs'
RELATIVE_URLS = True
THEME = 'Flex'
STATIC_PATHS = ['images', 'scripts', 'ads.txt', 'yorg_version.txt']
ARTICLE_SAVE_AS = 'articles/{slug}.html'
ARTICLE_URL = 'articles/{slug}.html'
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''
PLUGIN_PATHS = ['.']
PLUGINS = ['thumbnailer']
IMAGE_PATH = 'images'
THUMBNAIL_DIR = 'thumbnails'
THUMBNAIL_SIZES = {
    'tn': '640x?',
    'tn_t': '?x640'}
