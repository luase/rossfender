"""Views for orders"""
from .models import Order, Payment
from django.shortcuts import render, get_object_or_404
import datetime
from .forms import OrderForm, PaymentForm, ClientForm
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect

def index_view(request):
    todays_orders = Order.objects.filter(delivery_date=datetime.date.today())
    tomorrows_orders = Order.objects.filter(delivery_date=datetime.date.today() + datetime.timedelta(days=1))
    context = {
        'todays_orders' : todays_orders,
        'tomorrows_orders' : tomorrows_orders,
    }
    return render(request, 'orders/index.html', context)

class order_view(generic.DetailView):
    model = Order
    template_name = 'orders/order_detail.html'

def order_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OrderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('orders:index'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = OrderForm()

    return render(request, 'orders/order_form.html', {'form': form})

def client_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ClientForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('orders:index'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ClientForm()

    return render(request, 'orders/client_form.html', {'form': form})

def add_payment(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        payment = Payment(order=order.id, ammount=request.POST['ammount'])
        form = PaymentForm(instance=payment)
        print(form)
        print(payment)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('orders:order_detail', args=(order.id,)))

    return render(request, 'orders/anticipo.html', {'order' : order})

# def consult(request):
#     return 0

def order_list(request):
    relevant_orders = Order.objects.filter(delivery_date__gte=datetime.date.today())
    # exclude(delivery_date__gte=datetime.date.today() + datetime.timedelta(days=8))
    context = {
        'order_list' : relevant_orders,
    }
    return render(request, 'orders/order_list.html', context)
