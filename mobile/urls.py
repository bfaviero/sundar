from django.conf.urls import patterns, include, url
from mobile.mobile_backend import login, render_edit_product, render_product_list, render_sign_up, example, camera


urlpatterns = patterns('',
    url(r'^$', login),
    url(r'^edit_product', render_edit_product),
    url(r'^product_list', render_product_list),
    url(r'^sign_up', render_sign_up),
    url(r'^example', example),
    url(r'^camera', camera),

)

