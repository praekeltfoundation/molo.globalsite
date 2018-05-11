Molo Global Site
==================

.. image:: https://travis-ci.org/praekeltfoundation/molo.globalsite.svg?branch=develop
    :target: https://travis-ci.org/praekeltfoundation/molo.globalsite
    :alt: Continuous Integration

.. image:: https://coveralls.io/repos/github/praekeltfoundation/molo.globalsite/badge.svg?branch=develop
    :target: https://coveralls.io/github/praekeltfoundation/molo.globalsite?branch=develop
    :alt: Code Coverage

Provides code to help with creating a global site and redirecting the users to the country of their choice using the Molo code base.


Installation::

   pip install molo.globalsite


In your app settings::

   INSTALLED_APPS = (
      'molo.globalsite',
   )

   MIDDLEWARE = (
      'molo.globalsite.middleware.CountrySiteRedirectMiddleware'
   )

In your app urls.py::

   urlpatterns += patterns('',
        url(r'^globalsite/', include('molo.globalsite.urls', namespace='molo.globalsite', app_name='molo.globalsite')),
   )
