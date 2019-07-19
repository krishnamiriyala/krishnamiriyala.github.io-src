# -*- coding: utf-8 -*- #

from datetime import datetime

AUTHOR = 'Krishna Miriyala'
SITENAME = 'my blog'
SITETITLE = 'my blog'
SITEURL = 'http://localhost:8000' #'https://krishnamiriyala.github.io'
SITESUBTITLE ='Vitrualization | Cloud | Software Engineering'
SITEDESCRIPTION = "Vitrualization blog."

SITELOGO = 'https://krishnamiriyala.github.io/images/profile.jpg'
FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

THEME = '/Users/ptyagi/Developer/ptyagicodecamp/pelican-themes/Flex'
PATH = 'content/'
OUTPUT_PATH = 'blog/'
TIMEZONE = 'America/New_York'

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

LINKS = (
        ('LinkedIn', 'https://www.linkedin.com/in/krishnamiriyala'),
        ('GitHub', 'https://github.com/krishnamiriyala'),
	)

SOCIAL = (
        ('LinkedIn', 'https://www.linkedin.com/in/krishnamiriyala'),
        ('GitHub', 'https://github.com/krishnamiriyala'),
        #('rss', '/blog/feeds/all.atom.xml'),
	)

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10

#DISQUS_SITENAME = "krishnamiriyala"
#ADD_THIS_ID = ''

STATIC_PATHS = ['images']

CUSTOM_CSS = 'static/custom.css'

USE_LESS = True

GITHUB_CORNER_URL = 'https://github.com/krishnamiriyala'

GOOGLE_ADSENSE = {
    'ca_id': '',
    'page_level_ads': True,
    'ads': {
        'aside': '',
        'main_menu': '',
        'index_top': '', 
        'index_bottom': '',
        'article_top': '',
        'article_bottom': '',
    }
}
