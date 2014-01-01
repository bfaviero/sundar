from django.conf.urls import patterns, include, url
from web.web_backend import login, search

urlpatterns = patterns('',
    url(r'^$', login),
    url(r'^login', login),
    url(r'^search', search),
)

