from django.conf.urls import patterns, include, url
from mobile.mobile_backend import *
from backend.supplier_api import login_supplier, create_supplier

urlpatterns = patterns('',
    url(r'^$', login),
    url(r'^login', login),
    url(r'^create_user', create_supplier),
    url(r'^edit_product', render_edit_product, name="edit_product"),
    url(r'^product_list', render_product_list),
    url(r'^sign_up', render_sign_up),
    url(r'^example', example),
    url(r'^camera', camera),

)

