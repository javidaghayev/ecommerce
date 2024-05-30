from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from product.forms import ProductForm
from product.models import Product


def create_product(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('home')
        
    return render(request, 'product/create_product.html', {'form': form}) 



def update_product(request, id):
    # product = Product.objects.filter(id=id).first()
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('home')
    return render(request, 'product/update_product.html', {'form': form})


def detail_product(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product/detail_product.html', {'product': product})


def delete_product(request, id):
    product = Product.objects.filter(id=id, user=request.user).first()
    if product is None:
        return HttpResponse('GET ISINLE MESQUL OL')
    product.delete()
    return redirect('home')
    