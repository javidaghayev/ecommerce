from django.shortcuts import render, redirect
from product.forms import ProductForm


def create_product(request):
    form = ProductForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('home')
        
    return render(request, 'product/create_product.html', {'form': form}) 