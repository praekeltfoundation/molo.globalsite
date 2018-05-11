import pytest
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from wagtail.wagtailcore.models import Site
from molo.core.tests.base import MoloTestCaseMixin
from molo.globalsite.models import CountrySite, GlobalSiteSettings, Region


@pytest.mark.django_db
class TestGlobalSiteViews(TestCase, MoloTestCaseMixin):

    def setUp(self):
        self.mk_main()
        self.mk_main2()

        africa = Region.objects.create(name='Africa')
        asia = Region.objects.create(name='Asia')

        CountrySite.objects.create(
            name='South Africa', code='za',
            site_url='http://za.site.org', region=africa)
        CountrySite.objects.create(
            name='Iran', code='ir',
            site_url='http://ir.site.org', region=asia)

        default_site = Site.objects.get(is_default_site=True)
        self.setting = GlobalSiteSettings.objects.create(site=default_site)
        self.setting.is_globalsite = True
        self.setting.description = 'Welcome To Global Site'
        self.setting.save()

    def test_global_site_is_activated(self):
        response = self.client.get('/')
        self.assertRedirects(
            response, reverse('molo.globalsite:country_selection'))
        self.setting.is_globalsite = False
        self.setting.save()
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_country_listing(self):
        response = self.client.get('/', follow=True)
        self.assertContains(response, 'Welcome To Global Site')
        self.assertContains(response, 'Africa')
        self.assertContains(response, 'South Africa')
        self.assertContains(response, 'Asia')
        self.assertContains(response, 'Iran')

    def test_country_redirect(self):
            response = self.client.get(
                reverse('molo.globalsite:set_country', args=('za',)))
            self.assertEquals(response.url, 'http://za.site.org')

    def test_auto_redirect(self):
        self.client.get(
            reverse('molo.globalsite:set_country', args=('za',)))
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.client.get(
            reverse('molo.globalsite:set_country', args=('za',)))
        self.setting.autoredirect = True
        self.setting.save()
        response = self.client.get('/')
        self.assertEquals(response.status_code, 302)

    def test_changing_country(self):
        with self.settings(GLOBAL_SITE_URL=self.site.root_url):
            client = Client(HTTP_HOST=self.site2.hostname)
            url = self.site2.root_url + '/globalsite/changecountry/'
            response = client.get(url)
            self.assertEquals(
                response.url,
                'http://main-1.localhost:8000/globalsite/countries/')
            response = client.get(url, follow=True)
            self.assertContains(response, 'South Africa')

    def test_settings_globalsite_ignore_path(self):
        excl = ['/search/']
        response = self.client.get(excl[0])
        self.assertEquals(response.status_code, 302)
        with self.settings(GLOBAL_SITE_IGNORE_PATH=excl):
            response = self.client.get(excl[0])
            self.assertEquals(response.status_code, 200)
