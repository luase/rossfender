from django import forms
from django.forms import ModelForm

from .models import Order, Client, Payment

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['delivery_date', 'flavor', 'shape', 'description', 'client', 'price']
    
class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['order', 'ammount']

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['first_names', 'last_names', 'phone_number', 'description', 'birth_date']