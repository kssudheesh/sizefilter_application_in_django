from django.shortcuts import render
from .models import Product, Product_Variants

def index(request):
    if request.method == 'POST':
        l = request.POST.getlist('size')
        item_list = Product_Variants.objects.filter(size__in=l)
    else:
        item_list = Product_Variants.objects.all()
    
    return render(request, 'sizefilter/index.html', {'items': item_list})

