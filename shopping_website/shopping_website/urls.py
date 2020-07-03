from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^product/', include(('product.urls', 'product'), namespace='products')),
    url(r'^admin_panel/', include(('admin_panel.urls','admin_panel'), namespace='admin_panel')),
]
