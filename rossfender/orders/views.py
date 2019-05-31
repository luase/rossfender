"""Views for orders"""
from .models import Order
from django.shortcuts import render
import datetime

def index_view(request):
    relevant_orders = Order.objects.filter(delivery_date__gt=datetime.date.today()).exclude(delivery_date__gte=datetime.date.today() + datetime.timedelta(days=8))
    todays_orders = Order.objects.filter(delivery_date=datetime.date.today())
    tomorrows_orders = Order.objects.filter(delivery_date=datetime.date.today() + datetime.timedelta(days=1))
    context = {
        'relevant_orders' : relevant_orders,
        'todays_orders' : todays_orders,
        'tomorrows_orders' : tomorrows_orders,
    }
    return render(request, 'orders/index.html', context)

def order_view(request):
    return 0

def create_order(request):
    return 0

def consult(request):
    return 0
