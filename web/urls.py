from django.conf.urls import patterns, include, url
from web.views import *
from django.views.generic import TemplateView

urlpatterns = patterns('login',
    url(r'^$', market),
    url(r'^login', login, name='login'),
    url(r'^logout', logout, name='logout'),

)
urlpatterns += patterns('items',
	url(r'^market', market, name="market"),
	url(r'^inbox', messages, name="inbox"),
	url(r'^items/(?P<item_id>\d+)', item, name="item"),
	url(r'^users/(?P<user_id>\d+)', user, name="user"),
	url(r'^message/', message, name="message"),
)
