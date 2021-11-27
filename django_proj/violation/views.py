from django.shortcuts import render, redirect
from .forms import Violation


# Create your views here.

def home(request):
    return render(request, 'task/index.html')

def login(request):
    return render(request, 'task/login.html')

def innerpage(request):
    return render(request, 'task/innerpage.html')

def scan(request):
    form = Violation()
    if request.method == 'POST':
        form = Violation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/v_table')

    context = {'form': form}
    return render(request, 'task/scan.html', context)

def v_table(request):
    return render(request, 'task/v_table.html')

def create(request):
    return render(request, 'task/create.html')   