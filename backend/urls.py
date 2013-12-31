from django.conf.urls import patterns, include, url
from item_api import get_item, update_item, delete_item, get_items
from supplier_api import create_supplier, update_supplier, delete_supplier, login_supplier
from designer_api import create_designer, update_designer, delete_designer, login_designer

urlpatterns = patterns('',
    url(r'^get_item$', get_item),
    url(r'^update_item$', update_item),
    url(r'^delete_item$', delete_item),
    url(r'^create_supplier$', create_supplier),
    url(r'^update_supplier$', update_supplier),
    url(r'^delete_supplier$', delete_supplier),
    url(r'^login_supplier$', login_supplier),
    url(r'^create_designer$', create_designer),
    url(r'^update_designer$', update_designer),
    url(r'^delete_designer$', delete_designer),
    url(r'^login_designer$', login_designer),
    url(r'^get_items$', get_items),

)