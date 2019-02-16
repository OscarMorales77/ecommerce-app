from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/pizza/", views.pizza, name="pizza")
    # path("menu/subs", views.subs, name="subs"),  
    # path("menu/pasta", views.pasta, name="pasta"),  
    # path("menu/salad", views.salad, name="salad"), 
    # path("menu/platters", views.platters, name="platter"),     
]
