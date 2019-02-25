from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals


# Create your models here.
class PizzaPrice(models.Model):
    classification = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    num_toppings = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"ID: {self.id},  {self.classification}, {self.size}, {self.num_toppings}, ${self.price}"

    class Meta:
        verbose_name_plural = "Pizza Price"


class Toppings(models.Model):
    topping = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.topping}"

    class Meta:
        verbose_name_plural = "Pizza Toppings"


class PizzaOrder(models.Model):
    # UserProfile or User could work
    customer = models.ForeignKey(
        'UserProfile', related_name="pizzaOrder", on_delete=models.CASCADE)
    topping = models.ManyToManyField(Toppings, blank=True)
    price = models.ForeignKey(
        PizzaPrice, on_delete=models.CASCADE, related_name="pizzaOrder")

    def __str__(self):
        return f"{self.id}- {self.customer}- ${self.price.price}"

    class Meta:
        verbose_name_plural = "Pizza Order"


class UserProfile(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.customer}"

# create a user profile
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(customer=instance)


# if a user is created, create a user profile automatically
signals.post_save.connect(create_profile, sender=User, weak=False, dispatch_uid='models.create_profile')




class SubPrice(models.Model):
    classification = models.CharField(max_length=30)
    size = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.classification}, {self.size},  ${self.price}"

    class Meta:
        verbose_name_plural = "Sub Price"


class SubOrder(models.Model):
    # UserProfile or User could work
    customer = models.ForeignKey(
        'UserProfile', related_name="subOrder", on_delete=models.CASCADE)
    price = models.ForeignKey(
        SubPrice, on_delete=models.CASCADE, related_name="subOrder")

    def __str__(self):
        return f"{self.customer}- ${self.price.classification}"

    class Meta:
        verbose_name_plural = "Sub Order"


class PastaPrice(models.Model):
    classification = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return f"{self.classification},  ${self.price}"
    class Meta:
        verbose_name_plural = "Pasta Price"


class PastaOrder(models.Model):
    # UserProfile or User could work
    customer = models.ForeignKey(
        'UserProfile', related_name="pastaOrder", on_delete=models.CASCADE)
    price = models.ForeignKey(
        PastaPrice, on_delete=models.CASCADE, related_name="pastaOrder")

    def __str__(self):
        return f"{self.customer} - {self.price.classification}"

    class Meta:
        verbose_name_plural = "Pasta Order"


class SaladPrice(models.Model):
    classification = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return f"{self.classification},  ${self.price}"
    class Meta:
        verbose_name_plural = "Salad Price"


class SaladOrder(models.Model):
    # UserProfile or User could work
    customer = models.ForeignKey(
        'UserProfile', related_name="saladOrder", on_delete=models.CASCADE)
    price = models.ForeignKey(
        SaladPrice, on_delete=models.CASCADE, related_name="saladOrder")

    def __str__(self):
        return f"{self.customer}- ${self.price.classification}"

    class Meta:
        verbose_name_plural = "Salad Order"


class PlatterPrice(models.Model):
    classification = models.CharField(max_length=30)
    size = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.classification},  {self.size},   ${self.price}"
    class Meta:
        verbose_name_plural = "Platter Price"


class PlatterOrder(models.Model):
    # UserProfile or User could work
    customer = models.ForeignKey(
        'UserProfile', related_name="platterOrder", on_delete=models.CASCADE)
    price = models.ForeignKey(
        PlatterPrice, on_delete=models.CASCADE, related_name="platterOrder")

    def __str__(self):
        return f"{self.customer}- ${self.price.classification}"

    class Meta:
        verbose_name_plural = "Platter Order"

class ShoppingCartOrders(models.Model):
    customer = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    pizza_order = models.ManyToManyField(PizzaOrder, blank=True)
    sub_order = models.ManyToManyField('SubOrder', blank=True)
    pasta_order = models.ManyToManyField('PastaOrder', blank=True)
    salad_order = models.ManyToManyField('SaladOrder', blank=True)
    platter_order = models.ManyToManyField('PlatterOrder', blank=True)

    def __str__(self):
        return f" Shopping Cart for : {self.customer}"

    class Meta:
        verbose_name_plural = "Shopping Cart"
    
    
class PendingOrders(models.Model):
    customer = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    pizza_order = models.ManyToManyField(PizzaOrder, blank=True)
    sub_order = models.ManyToManyField('SubOrder', blank=True)
    pasta_order = models.ManyToManyField('PastaOrder', blank=True)
    salad_order = models.ManyToManyField('SaladOrder', blank=True)
    platter_order = models.ManyToManyField('PlatterOrder', blank=True)   

    def __str__(self):
        return f"Pending Orders for : {self.customer}"

    class Meta:
        verbose_name_plural = "Pending Orders"

#create pending and shoppign cart order when a user is created
def create_order_profile(sender, instance, created, **kwargs):
    if created:
        ShoppingCartOrders.objects.create(customer=instance)
        PendingOrders.objects.create(customer=instance)

signals.post_save.connect(create_order_profile, sender=UserProfile, weak=False, dispatch_uid='models.create_order_profile')