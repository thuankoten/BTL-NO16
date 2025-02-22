from django.contrib import admin
from django.urls import include, path
from home.views import login_view
from home.views import register_view
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product-add', views.add_product, name='product-add'),
    path('products', views.product_list, name='products'),
    path('client', views.client_list, name='client'),
    path('client-add', views.add_client, name='client-add'),
    path('order', views.order_list, name='order'),
    path('product-list', views.product_list, name='product-list'),
    path('login.html', login_view, name='login.html'),
    path("register.html", register_view, name="register.html"),
]

