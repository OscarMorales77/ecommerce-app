from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Toppings, PizzaPrice, SubPrice, PastaPrice, PastaOrder, SaladPrice, PlatterPrice, UserProfile

# user is a class/model/table so i can pass

# this function will handle all the logic pertaining to wether a user is authenticated
# will also render the correct "base template"


def auth_view(route, context, request):
    # if the user is authenticated render different options
    context['user'] = request.user
    if request.user.is_authenticated:
        base_template = "orders/layoutAuth.html"
        # update the context dictionary/map
        context["base_template"] = base_template
        user_profile = UserProfile.objects.get(customer=request.user)
        print(f"----------------> {user_profile}")
        return render(request, route, context)

    base_template = "orders/layout.html"
    context["base_template"] = base_template
    print(request.user)  # PRINT AnonymousUser
    return render(request, route, context)


def index(request):
    route = "orders/index.html"
    context = {}
    return auth_view(route, context, request)


def pizza(request):
    route = "orders/pizza.html"
    pizza_menu = PizzaPrice.objects.all()
    toppings = Toppings.objects.all()
    context = {"toppings": toppings, "pizza_menu": pizza_menu}
    return auth_view(route, context, request)


def subs(request):
    route = "orders/subs.html"
    sub_menu = SubPrice.objects.all()
    context = {"sub_menu": sub_menu}
    return auth_view(route, context, request)


def pasta(request):
    route = "orders/pasta.html"
    sub_menu = PastaPrice.objects.all()
    context = {"sub_menu": sub_menu}
    return auth_view(route, context, request)


def salad(request):
    sub_menu = SaladPrice.objects.all()
    context = {"sub_menu": sub_menu}
    route = "orders/salads.html"
    return auth_view(route, context, request)


def platter(request):
    sub_menu = PlatterPrice.objects.all()
    context = {"sub_menu": sub_menu}
    route = "orders/platters.html"
    return auth_view(route, context, request)


def register(request):
    if request.method == 'POST':
        submmited_form = UserCreationForm(request.POST)
        if submmited_form.is_valid():
            submmited_form.save()
            return HttpResponseRedirect(reverse("index"))
        # render a html with the data already submitted by the user that does not meet the criteria
        return render(request, "orders/register.html", {"form": submmited_form})

    form = UserCreationForm()
    context = {"form": form}
    return render(request, "orders/register.html", context)


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # this is were the request gets assigned the user
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid credentials."})

    return render(request, "orders/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def process_order(request):
    order_type = request.POST["orderType"]
    price_id = request.POST["id"]
    user_profile = UserProfile.objects.get(customer=request.user)
    if order_type == 'pasta':
        price_model=PastaPrice.objects.get(pk=price_id) #retrieve this price model from databasse
        order=PastaOrder(customer=user_profile, price=price_model) #create this particular order and save to DB
        print(f'------------>{order.price.id}')
        #order.save()
        #user_profile.pasta_order.add(order) #add order to customer profile
        print("worked")

    return HttpResponse(status=204)
