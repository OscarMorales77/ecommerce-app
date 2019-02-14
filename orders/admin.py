from django.contrib import admin
from .models import PizzaOrder, PizzaPrice, Toppings,UserProfile

# Register your models here.
admin.site.register(PizzaOrder)
admin.site.register(PizzaPrice)
admin.site.register(Toppings)
admin.site.register(UserProfile)
