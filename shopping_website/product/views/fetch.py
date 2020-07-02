from django.shortcuts import render
from collections import OrderedDict

from .. import models
#fectching  prodct data from db
def fetch_products(request):
    product_list = models.Product.objects.all()
    return render(request, 'product/product_list.html', {'product_list' : product_list})
