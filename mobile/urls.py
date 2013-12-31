from django.conf.urls import patterns, include, url
from mobile.mobile_backend import index


urlpatterns = patterns('',
    url(r'^$', index),
)

