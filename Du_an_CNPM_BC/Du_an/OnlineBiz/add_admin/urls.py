from django.urls import path
from . import views  # Đảm bảo đúng import

urlpatterns = [
    path('', views.index, name='index'),  # Đảm bảo views.index tồn tại
]
