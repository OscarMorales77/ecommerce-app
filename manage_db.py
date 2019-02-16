import sys, os, django
sys.path.append("/Users/om/Documents/CS50Web/project3") #here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizza.settings")
django.setup()
import inspect
from orders.models import *
# sys.path.append('/Users/om/Documents/CS50Web/project3/')
# os.environ['DJANGO_SETTINGS_MODULE'] = 'pizza.settings'
# django.setup()

price= [37.70,
39.70,
41.70,
43.70,
44.70]
def mainOld():
    i=0
    for p in price:
        if i==4:
            i=5
        PizzaPrice(classification="Sicilian", size="Large",num_toppings=i,price=p).save()
        i+=1
    
    
def mainOld2():
    for p in PizzaPrice.objects.all():
        print(p)




if __name__ == "__main__":
    main()
