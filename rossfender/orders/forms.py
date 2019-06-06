from django import forms
from django.forms import ModelForm

from .models import Order, Client

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['delivery_date', 'flavor', 'shape', 'description', 'client', 'price']