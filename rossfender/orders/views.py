"""Views for orders"""
from .models import Order
from django.shortcuts import render
import datetime
from .forms import OrderForm

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

def order_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OrderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = OrderForm()

    return render(request, 'orders/order_form.html', {'form': form})

def order_create(request):
    a = []

def consult(request):
    return 0
