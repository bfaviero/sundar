from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/', include('backend.urls')),
    url(r'^mobile/', include('mobile.urls')),
)
