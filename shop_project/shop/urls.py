from django.conf.urls import url

from shop_project.shop.views import get_products, get_product, delete_product, update_product, get_categories, \
    get_category, add_review, product_reviews

urlpatterns = [

    url(r'^products/$', get_products, name='get_products'),
    url(r'^product/(?P<product_id>\d+)/$', get_product, name='get_product'),
    url(r'^delete_product/(?P<product_id>\d+)/$', delete_product, name='delete_product'),
    url(r'^update_product/(?P<product_id>\d+)/$', update_product, name='update_product'),
    url(r'^categories/$', get_categories, name='get_categories'),
    url(r'^categories/(?P<category_slug>[a-z0-9\-]+)/$', get_category, name='get_category'),
    url(r'^create_review/$', add_review, name='add_review'),
    url(r'^product_reviews/(?P<product_id>\d+)/$', product_reviews, name='product_reviews'),



]