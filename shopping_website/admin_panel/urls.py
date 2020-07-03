from django.urls import path
from .views import views, category
from django.conf.urls import url

urlpatterns = [
    # url('$', views.index),
    url('create-category/$', category.CategoryCreateView.as_view(),
        name='create-category'),
    url('category-list/$', category.CategoryListView.as_view(), name='category-list'),
]
