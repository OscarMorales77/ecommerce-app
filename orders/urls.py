from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/pizza", views.pizza, name="pizza"),
    path("menu/subs", views.subs, name="subs"),  
    path("menu/pasta", views.pasta, name="pasta"),  
    path("menu/salad", views.salad, name="salad"), 
    path("menu/platters", views.platter, name="platter"), 
    path("register", views.register, name="register"), 
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("private", views.process_order, name="private")          
]
