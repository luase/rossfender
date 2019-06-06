"""url configuration for orders"""
from django.urls import path
from . import views


app_name = 'orders'
urlpatterns = [
path('', views.index_view, name='index'),
path('order/form/', views.order_form, name='form'),
path('order/create/', views.order_create, name='create'),
# path('consult/', views.consult, name='consult'),
path('order/<int:pk>/', views.order_view, name='detail'),
]
