from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Toppings, PizzaPrice, SubPrice, PastaPrice, SaladPrice,PlatterPrice

#this function will handle all the logic pertaining to wether a user is authenticated
#will also render the correct "base template"
def auth_view(route, context, request):
    if request.user.is_authenticated:
        base_template="orders/layoutAuth.html"
        #update the context dictionary/map
        context["base_template"]=base_template
        return render(request, route,context)
          
    base_template="orders/layout.html"
    context["base_template"]=base_template  
    return render(request, route,context)


def index(request):
    route="orders/index.html"
    context={}
    return auth_view(route,context,request)

def pizza(request):
    route="orders/pizza.html"
    pizza_menu=PizzaPrice.objects.all()
    toppings=Toppings.objects.all()
    context={"toppings":toppings, "pizza_menu":pizza_menu}
    return auth_view(route,context,request)

def subs(request):
    route="orders/subs.html"
    sub_menu=SubPrice.objects.all()
    context={"sub_menu":sub_menu}
    return auth_view(route,context,request)

def pasta(request):
    route="orders/pasta.html"
    sub_menu=PastaPrice.objects.all()
    context={"sub_menu":sub_menu}
    return auth_view(route,context,request)

def salad(request):
    sub_menu=SaladPrice.objects.all()
    context={"sub_menu":sub_menu}
    route="orders/salads.html"
    return auth_view(route,context,request)

def platter(request):
    sub_menu=PlatterPrice.objects.all()
    context={"sub_menu":sub_menu}
    route="orders/platters.html"
    return auth_view(route,context,request)

def register(request):
    if request.method == 'POST':
        submmited_form=UserCreationForm(request.POST)
        if submmited_form.is_valid():
            submmited_form.save()
            return HttpResponseRedirect(reverse("index")) 
        #render a html with the data already submitted by the user that does not meet the criteria
        return render(request, "orders/register.html", {"form":submmited_form})   
            
    form= UserCreationForm()
    context={"form":form}
    return render(request, "orders/register.html", context)

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) #this is were the request gets assigned the user
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid credentials."})

    return render(request, "orders/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))