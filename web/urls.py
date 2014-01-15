from django.conf.urls import patterns, include, url
from web.views import *
from django.views.generic import TemplateView

urlpatterns = patterns('login',
    url(r'^$', login),
    url(r'^login', 'django.contrib.auth.views.login', name='login'),
)
urlpatterns += patterns('items',
	url(r'^market', market, name="market"),
	url(r'^item/(?P<item_id>\d+)', item, name="item"),
)

urlpatterns += patterns('users',
	url(r'^market', market, name="market"),
	url(r'^item/(?P<item_id>\d+)', item, name="item"),
)