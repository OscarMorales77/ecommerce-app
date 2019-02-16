from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from .models import Toppings, PizzaPrice
# Create your views here.
def index(request):
    pizza_menu=PizzaPrice.objects.all()
    toppings=Toppings.objects.all()
    print(toppings)
    context={"toppings":toppings, "pizza_menu":pizza_menu}
    return render(request, "orders/index.html", context)