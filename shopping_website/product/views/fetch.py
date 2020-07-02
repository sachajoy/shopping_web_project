from django.shortcuts import render
from collections import OrderedDict


from peewee import *
from product/models import *
#fectching  prodct data from db
# Create your views here.
db = SqliteDatabase('db.sqlite3')

def fetch(request):
    product_list = Product.object.all()
    return render(request, 'product/display_products.html', {'product_list' : product_list})
