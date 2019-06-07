"""url configuration for orders"""
from django.urls import path
from . import views


app_name = 'orders'
urlpatterns = [
path('', views.index_view, name='index'),
path('order/list/', views.order_list, name='order_list'),
path('order/form/', views.order_form, name='order_form'),
# path('order/create/', views.order_create, name='create'),
# path('consult/', views.consult, name='consult'),
path('order/<int:pk>/', views.order_view.as_view(), name='order_detail'),
]
