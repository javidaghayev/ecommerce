from django.shortcuts import render
from product.models import Product
# from django.http import HttpResponse



def home(request):
    products = Product.objects.all()
    return render(request, 'web/home.html', {'products': products})



