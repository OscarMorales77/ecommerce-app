from django.contrib import admin
from .models import PizzaOrder, PizzaPrice, Toppings, UserProfile, SubOrder,SubPrice,PastaOrder,PastaPrice,SaladOrder,SaladPrice,PlatterOrder,PlatterPrice, ShoppingCartOrders,PendingOrders

# Register your models here.
admin.site.register(PizzaOrder)
admin.site.register(PizzaPrice)
admin.site.register(Toppings)
admin.site.register(UserProfile)
admin.site.register(SubOrder)
admin.site.register(SubPrice)
admin.site.register(PastaOrder)
admin.site.register(PastaPrice)
admin.site.register(SaladOrder)
admin.site.register(SaladPrice)
admin.site.register(PlatterPrice)
admin.site.register(PlatterOrder)
admin.site.register(ShoppingCartOrders)
admin.site.register(PendingOrders)


