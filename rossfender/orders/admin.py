from django.contrib import admin

from orders.models import Ingredient, Flavor, Shape, Measure, RecommendedPrice, Order, Payment, Client

admin.site.register(Ingredient)
admin.site.register(Flavor)
admin.site.register(Shape)
admin.site.register(Measure)
admin.site.register(RecommendedPrice)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Client)