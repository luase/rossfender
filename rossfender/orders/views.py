"""Views for orders"""
from .models import Order
from django.shortcuts import render
import datetime

def index_view(request):
    orders_for_today = Order.objects.filter(delivery_date__lte=datetime.date.today())
    context = {
        'orders_for_today' : orders_for_today,
    }
    return render(request, 'orders/index.html', context)

def create_order(request):
    return 0

def consult(request):
    return 0
