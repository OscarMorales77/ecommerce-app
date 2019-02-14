from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals




# Create your models here.
class PizzaPrice(models.Model):
    classification = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    num_toppings = models.IntegerField( default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name_plural = "Pizza Price"


class Toppings(models.Model):
    topping = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Toppings"
        


class PizzaOrder(models.Model): 
    author = models.ForeignKey('UserProfile', related_name="orders", on_delete=models.CASCADE)
    topping = models.ManyToManyField(Toppings, blank=True)
    price = models.ForeignKey(PizzaPrice, on_delete=models.CASCADE, related_name="orders")

    class Meta:
        verbose_name_plural = "Pizza Order"

class UserProfile(models.Model):
    author=models.OneToOneField(User,on_delete=models.CASCADE)
    #a user can have more than one Pizza Order, hence the many-to-many realtionship
    pizza_order=models.ManyToManyField(PizzaOrder, blank=True)

#create a user profile
def create_profile(sender, instance, created, **kwargs):  
    if created:
        UserProfile.objects.create(author=instance)
#if a user is created, create a user profile automatically 
signals.post_save.connect(create_profile, sender=User, weak=False, dispatch_uid='models.create_profile')
