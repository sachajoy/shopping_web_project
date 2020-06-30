from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'product/shop-grid.html')

 #   def index(request):
  #  return render(request, 'admin_panel/index.html')