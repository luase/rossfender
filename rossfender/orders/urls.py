"""url configuration for orders"""
from django.urls import path
from . import views


app_name = 'orders'
urlpatterns = [
path('', views.index_view, name='index'),
]
