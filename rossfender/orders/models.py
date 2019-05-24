'''Definition of the models for the orders'''
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Ingredient(models.Model):
    '''Ingridient definition'''
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return f'{self.name}'


class Flavor(models.Model):
    '''Flavor definition'''
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True)
    ingredients = models.ManyToManyField('Ingredient')
    def __str__(self):
        return f'{self.name}'


class Shape(models.Model):
    '''Shape definition'''
    name = models.CharField(max_length=60, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return f'{self.name}'


class Measure(models.Model):
    """Measure definition"""
    IS = [
        ('g', 'gramos(s)'),
        ('kg', 'kilogramo(s)'),
    ]
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    cake = models.ForeignKey('Cake', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    units = models.CharField(max_length=3, choices=IS, default='g')
    def __str__(self):
        return f'{self.ingredient} - {self.quantity} {self.units}'
    class Meta:
        unique_together = ['cake', 'ingredient']


class Cake(models.Model):
    """Cake definition"""
    flavor = models.ForeignKey('Flavor', on_delete=models.CASCADE)
    shape = models.ForeignKey('Shape', on_delete=models.CASCADE)
    feeds = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return f'{self.shape} - {self.flavor}'
    class Meta:
        unique_together = ['shape', 'flavor']

class Order(models.Model):
    """Order definition"""
    cake = models.ForeignKey('Cake', on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17) # validators should be a list