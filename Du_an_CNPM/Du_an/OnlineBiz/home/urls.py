from django.contrib import admin
from django.urls import include, path
from .import views 
urlpatterns = [
    path('', views.home, name='home'),
    path('product-add', views.add_product, name='product-add'),
    path('products', views.product_list, name='products'),
    path('client', views.client_list, name='client'),
    path('client-add', views.add_client, name='client-add'),
    path('order', views.order_list, name='order'),
    path('products', views.product_list, name='product-list'),

]

