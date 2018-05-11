from django.shortcuts import redirect
from django.conf import settings
from django.core.urlresolvers import reverse
from models import GlobalSiteSettings


class CountrySiteRedirectMiddleware(object):
    def process_request(self, request):
        globalsite_settings = GlobalSiteSettings.for_site(request.site)

        exclude = [
            settings.MEDIA_URL,
            settings.STATIC_URL,
            reverse('health'),
            reverse('versions'),
            '/globalsite/',
            '/admin/',
            'django-admin/',
            '/import/',
            '/locale/',
            '/favicon.ico',
            '/robots.txt',
            '/metrics',
            '/api/',
            '/serviceworker.js'
        ]
        if hasattr(settings, 'GLOBAL_SITE_IGNORE_PATH'):
            exclude += settings.GLOBAL_SITE_IGNORE_PATH
        if any([p for p in exclude if request.path.startswith(p)]):
            return None

        if 'GLOBALSITE_COUNTRY_SELECTION' not in request.session and \
                globalsite_settings.is_globalsite:
            return redirect(reverse('molo.globalsite:country_selection'))

        if 'GLOBALSITE_COUNTRY_SELECTION' in request.session and \
                globalsite_settings.autoredirect:
            return redirect(
                request.session.get('GLOBALSITE_COUNTRY_SELECTION')
            )