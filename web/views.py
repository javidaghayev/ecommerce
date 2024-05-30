from django.shortcuts import render
from product.models import Product
from product.models import Blog
# from django.http import HttpResponse



def home(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')

        data = Blog(name=name, image=image)
        data.save()

    count = Blog.objects.all().count()
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
            
    return render(request, 'web/home.html', context)
    # products = Product.objects.all()
    # return render(request, 'web/home.html', {'products': products})




def calc_view(request):
    result = ''
    print("ssssssssssssssssss")
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    if num1 and num2:
        result = int(num1)+int(num2)
    
    context = {
        'result': result
    }

    return render(request, 'web/calc.html', context)




