from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'task/index.html')

def login(request):
    return render(request, 'task/login.html')

def innerpage(request):
    return render(request, 'task/innerpage.html')