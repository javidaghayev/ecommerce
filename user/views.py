from django.shortcuts import render, redirect
from user.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            
            else:
                messages.error(request, "This user already exists")


    form = LoginForm()
    context = {
        'form': form
    }
    
    return render(request, 'user/login.html', context)
    



def logout_view(request):
    logout(request)
    return redirect('home')





def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]

            if User.objects.filter(username=username).exists():


                form.save()
                return redirect('home')
            
            else:
                return redirect('register_view')

        
    else:
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'user/register.html', context)
    


