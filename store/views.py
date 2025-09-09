from urllib import request
from django.shortcuts import render, redirect
from .models import Category, Product, Order, Customer, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  
from django import forms 
from .forms import SignUpForm, UpdateUsrForm, ChangePasswordForm, UserInfoForm


def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = UserInfoForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your information has been updated successfully!")
            return redirect('home')
        return render(request, 'update_info.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to access that page!")
        return redirect('home')

def update_password(request):  
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
           form = ChangePasswordForm(current_user, request.POST)
           if form.is_valid():
               form.save()
               messages.success(request, "Password updated successfully!")
               login(request, current_user)
               return redirect('update_user')
           else:
               for error in list(form.errors.values()):
                   messages.error(request, error)
                   return redirect('update_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, 'update_password.html', {'form': form})
    else:
        messages.error(request, "You must be logged in to access that page!")
        return redirect('login')


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUsrForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, "Profile updated successfully!")
            return redirect('home')
        return render(request, 'update_user.html', {'user_form': user_form})
    else:
        messages.success(request, "You must be logged in to access that page!")
        return redirect('home')


def category_summary(request):
    categories = Category.objects.all()

    return render(request, 'category_summary.html', {"categories": categories})

def category(request, foo):
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except:
        messages.error(request, "Category not found.")
        return redirect('home')
    
    
    
    


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('home')
        else:
            messages.error(request, "There was an error, Please try again.")
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user (request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home') 


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # login user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Username created, please fill out your user info Below!")
            return redirect('update_info')
        else:
            messages.error(request, "There was an error, Please try again.")
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})