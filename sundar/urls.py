from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.base import RedirectView
admin.autodiscover()

import backend.urls
import mobile.urls
import web.urls

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/web', permanent=False)),
    url(r'^api/', include(backend.urls)),
    url(r'^mobile/', include(mobile.urls)),
    url(r'^web/', include(web.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next two lines to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

