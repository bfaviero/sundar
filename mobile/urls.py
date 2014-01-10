from django.conf.urls import patterns, include, url
from mobile.mobile_backend import render_login, render_edit_product, render_product_list, render_sign_up, example, camera
from backend.supplier_api import login_supplier, create_supplier

urlpatterns = patterns('',
    url(r'^$', render_login),
    url(r'^login', login_supplier),
    url(r'^create_user', create_supplier),
    url(r'^edit_product', render_edit_product),
    url(r'^product_list', render_product_list),
    url(r'^sign_up', render_sign_up),
    url(r'^example', example),
    url(r'^camera', camera),

)

