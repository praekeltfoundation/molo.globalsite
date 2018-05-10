from .base import MIDDLEWARE_CLASSES # noqa

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + [
    'molo.globalsite.middleware.CountrySiteRedirectMiddleware',
]
