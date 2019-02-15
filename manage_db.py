import sys, os, django
sys.path.append("/Users/om/Documents/CS50Web/project3") #here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizza.settings")
django.setup()
from orders.models import Toppings
# sys.path.append('/Users/om/Documents/CS50Web/project3/')
# os.environ['DJANGO_SETTINGS_MODULE'] = 'pizza.settings'
# django.setup()

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    return print("Hello World")


if __name__ == "__main__":
    main()
