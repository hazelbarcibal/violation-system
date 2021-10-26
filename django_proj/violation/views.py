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

<<<<<<< HEAD
def v_table(request):
    return render(request, 'task/v_table.html')
=======
def create(request):
    return render(request, 'task/create.html')    
>>>>>>> 21a99974e26b021aba6ce6adf7a901ea15d58675
