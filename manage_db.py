import sys, os, django

sys.path.append("/Users/om/Documents/CS50Web/project3")  # here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizza.settings")
django.setup()

from django.contrib.auth.models import User
from orders.models import PizzaOrder, PizzaPrice, Toppings, UserProfile, SubOrder, SubPrice, PastaOrder, PastaPrice, \
    SaladOrder, SaladPrice, PlatterOrder, PlatterPrice


# sys.path.append('/Users/om/Documents/CS50Web/project3/')
# os.environ['DJANGO_SETTINGS_MODULE'] = 'pizza.settings'
# django.setup()


def mainOld():
    i = 0
    for p in price:
        if i == 4:
            i = 5
        PizzaPrice(classification="Sicilian", size="Large", num_toppings=i, price=p).save()
        i += 1


def mainOld2():
    for p in PizzaPrice.objects.all():
        print(p)


subs = [0,
1,
2,
3,
5]

price = [37.7,
39.7,
41.7,
43.7,
44.7]

tops=['Pepperoni',
'Sausage',
'Mushrooms',
'Onions',
'Ham',
'Canadian Bacon',
'Pineapple',
'Eggplant',
'Tomato & Basil',
'Green Peppers',
'Hamburger',
'Spinach',
'Artichoke',
'Buffalo Chicken',
'Barbecue Chicken',
'Anchovies',
'Black Olives',
'Fresh Garlic',
'Zucchini',]

def mainKKSXS():
    for i in range(len(tops)):
        PizzaPrice(classification="Sicilian", price=price[i], size="Large", num_toppings=subs[i]).save()
        print(f"{subs[i]}, {price[i]}")

def main():
    for i in range(len(tops)):
        Toppings(topping=tops[i]).save()
        print(f"{tops[i]}")

def printL():
    for i in SubPrice.objects.all():
        print(i)


def testQuery():
    p = User.objects.get(username='test123')
    userProfile = UserProfile.objects.get(customer=p)
    # print(userProfile.pasta_order.all())
    for p in userProfile.pasta_order.all():
        print(p.price.price)  # multiple level processing


if __name__ == "__main__":
    # testQuery()
    main()
# printL()
