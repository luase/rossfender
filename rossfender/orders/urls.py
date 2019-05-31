"""url configuration for orders"""
from django.urls import path
from . import views


app_name = 'orders'
urlpatterns = [
path('', views.index_view, name='index'),
path('create/', views.create_order, name='create_order'),
path('consult/', views.consult, name='consult'),
path('order/<int:pk>/', views.order_view, name='order'),
]
