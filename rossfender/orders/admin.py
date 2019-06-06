from django.contrib import admin
from django.utils import timezone
import datetime
from orders.models import Ingredient, Flavor, Shape, Measure, RecommendedPrice, Order, Payment, Client



class PaymentInLine(admin.TabularInline):
    model = Payment
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Cliente: ',               {'fields': ['client']}),
        ('Detalles del pastel: ',   {'fields': ['flavor','shape']}),
        ('Precio: ',                {'fields': ['price']}),
        ('Fecha de entrega: ',      {'fields': ['delivery_date'], 'classes': ['collapse']}),
    ]
    list_display = ('pastel','cliente','fecha_entrega','fecha_pedido','estado')

    def pastel(self, obj):
        return ("SABOR: %s, FORMA: %s" % (obj.flavor, obj.shape))
    pastel.short_description = 'Pastel:'

    def cliente(self, obj):
        return ("%s" % (obj.client))
    cliente.short_description = 'Nombre del cliente:'

    def fecha_entrega(self, obj):
        return ("%s" % (obj.delivery_date))
    fecha_entrega.short_description = 'Fecha de entrega:'

    def fecha_pedido(self, obj):
        return ("%s" % (obj.creation_date.date()))
    fecha_pedido.short_description = 'Fecha de pedido:'

    def estado(self, obj):
        now = datetime.date.today()
        if obj.delivery_date >= now:
            return 'Pendiente'
        else:
            return 'Entregado'
        return
    estado.short_description = 'Estado de orden:'

    list_filter = ['client','delivery_date']
    inlines = [PaymentInLine]
    search_fields = ['delivery_date','client','creation_date']



class OrderInLine(admin.TabularInline):
    model = Order
    extra = 1
    
class ClientAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nombre: ',                {'fields': ['first_names','last_names']}),
        ('Detalles del cliente: ',  {'fields': ['description']}),
        ('Fecha de Nacimiento: ',   {'fields': ['birth_date']}),
        ('Teléfono: ',              {'fields': ['phone_number'], 'classes': ['collapse']}),
    ]
    #list_display = ('first_names','last_names','phone_number')
    list_display = ('nombre_mayusculas', 'telefono')

    def nombre_mayusculas(self, obj):
        return ("%s %s" % (obj.first_names, obj.last_names)).upper()
    nombre_mayusculas.short_description = 'Nombre'

    def telefono(self, obj):
        return ("%s" % (obj.phone_number)).upper()
    telefono.short_description = 'Teléfono'

    list_filter = ['birth_date']
    inlines = [OrderInLine]
    search_fields = ['first_names','last_names','phone_number']



class IngredientAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Ingrediente: ',               {'fields': ['name','description','units']}),
    ]
    list_display = ('ingrediente','unidades')

    def ingrediente(self, obj):
        return ("%s" % (obj.name))
    ingrediente.short_description = 'Ingrediente:'

    def unidades(self, obj):
        return ("%s" % (obj.units))
    unidades.short_description = 'Unidades:'

    search_fields = ['name']

class MeasureAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Ingrediente: ',               {'fields': ['ingredient']}),
        ('Forma y medida: ',            {'fields': ['shape','quantity']}),
    ]
    list_display = ('ingrediente','medidas')

    def ingrediente(self, obj):
        return ("%s" % (obj.ingredient))
    ingrediente.short_description = 'Ingrediente:'

    def medidas(self, obj):
        return ("FORMA: %s , CANTIDAD: %s" % (obj.shape, obj.quantity))
    medidas.short_description = 'Medidas:'

    search_fields = ['ingredient','shapes','quantity']

class FlavorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Sabor: ',               {'fields': ['name','description','ingredients']}),
    ]
    list_display = ('sabor','descripcion')

    def sabor(self, obj):
        return ("%s" % (obj.name))
    sabor.short_description = 'Sabor:'

    def descripcion(self, obj):
        return ("%s" % (obj.description))
    descripcion.short_description = 'Descripción:'

    search_fields = ['name']



class ShapeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Forma: ',               {'fields': ['name','feeds','description']}),
    ]
    list_display = ('forma','descripcion')

    def forma(self, obj):
        return ("%s" % (obj.name))
    forma.short_description = 'Forma:'

    def descripcion(self, obj):
        return ("%s" % (obj.description))
    descripcion.short_description = 'Descripción:'



class PaymentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Adelanto: ',               {'fields': ['order','ammount']}),
    ]
    list_display = ('adelanto','orden','fecha_pago')

    def adelanto(self, obj):
        return ("$ %s" % (obj.ammount))
    adelanto.short_description = 'Adelanto:'

    def orden(self, obj):
        return ("%s" % (obj.order))
    orden.short_description = 'Orden:'

    def fecha_pago(self, obj):
        return ("%s" % (obj.creation_date.date()))
    fecha_pago.short_description = 'Fecha de pago:'



class RecommendedPriceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Caracteristicas: ',               {'fields': ['flavor','shape']}),
        ('Precio recomendado: ',               {'fields': ['price']}),
    ]
    list_display = ('caracteristicas','precio')

    def caracteristicas(self, obj):
        return ("Pastel de %s %s" % (obj.flavor, obj.shape))
    caracteristicas.short_description = 'Caracteristicas:'

    def precio(self, obj):
        return ("$%s" % (obj.price))
    precio.short_description = 'Precio recomendado:'

    

admin.site.register(Order, OrderAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Flavor, FlavorAdmin)
admin.site.register(Shape, ShapeAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Measure, MeasureAdmin)
admin.site.register(RecommendedPrice, RecommendedPriceAdmin)