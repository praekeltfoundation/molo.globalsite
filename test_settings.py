from .base import MIDDLEWARE_CLASSES # noqa
from os.path import abspath, dirname, join
from os import environ

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + [
    'molo.globalsite.middleware.CountrySiteRedirectMiddleware',
]

# Global site settings
GLOBAL_SITE_URL = environ.get('GLOBAL_SITE_URL', '')
GEOIP_PATH = join(dirname(dirname(abspath(__file__))), 'geoip_db')
