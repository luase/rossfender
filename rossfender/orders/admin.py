from django.contrib import admin

from orders.models import Ingredient, Flavor, Shape, Measure, Cake, Order, Client

admin.site.register(Ingredient)
admin.site.register(Flavor)
admin.site.register(Shape)
admin.site.register(Measure)
admin.site.register(Cake)
admin.site.register(Order)
admin.site.register(Client)