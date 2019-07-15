from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact-us.html')

def catalog(request):
    return render(request, 'catalog-page.html')

def login(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration.html')

def product(request):
    return render(request, 'product-page.html')
