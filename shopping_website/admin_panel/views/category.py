from django.views.generic import (CreateView, ListView)
from django.apps import apps
# from shopping_website.product.models import Category

category = apps.get_model('product', 'Category')
class CategoryCreateView(CreateView):
    """To create the new category by admin"""
    model = category
    fields = ['name', 'sub_category']


class CategoryListView(ListView):
    """To view the category that are there in the db
    created by the admin of the system"""
    model = category
    context_object_name = 'categories'

    