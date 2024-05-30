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
                messages.error(request, 'Usr yoxdu')

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
                return redirect('home')

        
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)
    



def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
        
    form = ProfileForm(instance=request.user)
    return render(request, 'user/profile.html', {'form': form})




# def profile_view(request, pk):
#     user = UserProfile.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('profile_view', kwargs={'pk': user.pk})
        
#     form = ProfileForm(instance=request.user)
#     return render(request, 'user/profile.html', {'form': form})
