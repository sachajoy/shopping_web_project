from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'website/shop-grid.html')

 #   def index(request):
  #  return render(request, 'admin_panel/index.html')