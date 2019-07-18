# -*- coding: utf-8 -*- #

from datetime import datetime

AUTHOR = 'Krishna Miriyala'
SITENAME = 'my blog'
SITETITLE = 'my blog'
SITEURL = 'http://localhost:8000' #'https://krishnamiriyala.github.io'
SITESUBTITLE ='Vitrualization | Cloud | Software Engineering'
SITEDESCRIPTION = "Vitrualization blog."

SITELOGO = 'https://ptyagicodecamp.github.io/images/profile.jpg'
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
        ('LinkedIn', 'https://www.linkedin.com/in/priyankatyagi'),
        ('GitHub', 'https://github.com/ptyagicodecamp'),
        ('Medium', 'https://medium.com/@ptyagicodecamp'),
        ('Twitter', 'https://twitter.com/ptyagi13'),
	)

SOCIAL = (
        ('LinkedIn', 'https://www.linkedin.com/in/priyankatyagi'),
        ('GitHub', 'https://github.com/ptyagicodecamp'),
        ('Medium', 'https://medium.com/@ptyagicodecamp'),
        ('Twitter', 'https://twitter.com/ptyagi13'),
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

#DISQUS_SITENAME = "ptyagicodecamp"
#ADD_THIS_ID = 'ra-5cf387135c8761da'

STATIC_PATHS = ['images']

CUSTOM_CSS = 'static/custom.css'

USE_LESS = True

GITHUB_CORNER_URL = 'https://github.com/krishnamiriyala'

GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-6359982310050489',
    'page_level_ads': True,
    'ads': {
        'aside': '8977779775',
        'main_menu': '8977779775',
        'index_top': '', #8977779775
        'index_bottom': '8977779775',
        'article_top': '6546879945',
        'article_bottom': '6546879945',
    }
}