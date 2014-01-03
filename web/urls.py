from django.conf.urls import patterns, include, url
from web.web_backend import login, search, validate_login

urlpatterns = patterns('',
    url(r'^$', login),
    url(r'^login', login),
    url(r'^market', search),
    url(r'^validate_login', validate_login),
)

