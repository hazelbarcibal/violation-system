from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'task/index.html')

def login(request):
    return render(request, 'task/login.html')

def innerpage(request):
    return render(request, 'task/innerpage.html')

def scan(request):
    return render(request, 'task/scan.html')

def v_table(request):
    return render(request, 'task/v_table.html')