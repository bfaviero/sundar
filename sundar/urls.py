from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from mobile.mobile_backend import index

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^api/', include('backend.urls')),
    url(r'^mobile/', include('mobile.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next two lines to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)