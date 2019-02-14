from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PizzaPrice(models.Model):
    classification = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    num_toppings = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        verbose_name_plural = "Pizza Price"


class Toppings(models.Model):
    topping = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Toppings"


class PizzaOrder(models.Model):
    author = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    topping = models.ManyToManyField(Toppings)
    price = models.ForeignKey(PizzaPrice, on_delete=models.Case, related_name="orders")

    class Meta:
        verbose_name_plural = "Pizza Order"
