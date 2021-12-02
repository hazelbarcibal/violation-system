from django.forms.widgets import NumberInput
from django.shortcuts import render, redirect
from .forms import addViolation
from .forms import Records


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

def create(request):
    return render(request, 'task/create.html')   

def add(request):
    form = addViolation()
    if request.method == 'POST':
        form = addViolation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/table')

    return render(request, 'task/add.html', {'form':form})

def table(request):
    info = Records.objects.all()
    context = {
        'info': info,    
    }

    return render(request, 'task/table.html', context)