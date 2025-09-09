from urllib import request
from django.shortcuts import render, redirect
from .models import Category, Product, Order, Customer
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  
from django import forms 
from .forms import SignUpForm








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
            messages.success(request, "You have registered successfully!")
            return redirect('home')
        else:
            messages.error(request, "There was an error, Please try again.")
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})