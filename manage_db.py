import sys, os, django
sys.path.append("/Users/om/Documents/CS50Web/project3") #here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizza.settings")
django.setup()
import inspect
from orders.models import PizzaOrder, PizzaPrice, Toppings, UserProfile, SubOrder,SubPrice,PastaOrder,PastaPrice,SaladOrder,SaladPrice,PlatterOrder,PlatterPrice
# sys.path.append('/Users/om/Documents/CS50Web/project3/')
# os.environ['DJANGO_SETTINGS_MODULE'] = 'pizza.settings'
# django.setup()


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

subs=["Garden Salad",
"Greek Salad",
"Antipasto",
"Baked Ziti",
"Meatball Parm",
"Chicken Parm",]

price=[60,
70,
70,
60,
70,
80,]

def main():
	for i in range(len(subs)):
		PlatterPrice(classification=subs[i],price=price[i], size="Large").save()
		print(f"{subs[i]}, {price[i]}")
	
def printL():
	for i in SubPrice.objects.all():
		print(i)


if __name__ == "__main__":
	main()
	#printL()
