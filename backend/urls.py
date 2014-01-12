from django.conf.urls import patterns, include, url
from item_api import get_item, set_item, delete_item, get_items
from supplier_api import create_supplier, update_supplier, delete_supplier, login_supplier
from designer_api import create_designer, update_designer, delete_designer, login_designer

urlpatterns = patterns('',
    url(r'^get_item$', get_item),
    url(r'^set_item$', set_item),
    url(r'^delete_item$', delete_item),
    url(r'^get_items$', get_items),

)