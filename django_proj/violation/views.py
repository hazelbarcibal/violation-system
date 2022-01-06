from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import addViolation, CreateUserForm
from .forms import Records

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'task/index.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect('violation-innerpage')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('violation-innerpage')
            else:
                messages.info(request, 'Invalid credentials. Please try again.')
            
        return render(request, 'task/login.html')

def logoutUser(request):
    logout(request)
    return redirect('violation-signin')

def register(request):
    if request.user.is_authenticated:
        return redirect('violation-innerpage')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('violation-signin')
            else:
                messages.warning(request, form.errors)

        context = {
            'form':form,
        }
        return render(request, 'task/register.html', context)

@login_required(login_url='violation-signin')
def innerpage(request):
    return render(request, 'task/innerpage.html')

@login_required(login_url='violation-signin')
def scan(request):
    return render(request, 'task/scan.html')

#def v_table(request):
    #return render(request, 'task/v_table.html')

@login_required(login_url='violation-signin')
def create(request):
    return render(request, 'task/create.html')   

@login_required(login_url='violation-signin')
def add(request):
    if request.user.is_authenticated and request.user.is_superuser:
        form = addViolation()
        if request.method == 'POST':
            form = addViolation(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/table')

        context = {
            'form': form,
        }
        return render(request, 'task/add.html', context)
    else:
        return HttpResponse('You are restricted to access this page. Please go back again.')

@login_required(login_url='violation-signin')
def table(request):
    num = ''
    result = ''
    info = Records.objects.all()[:3]
    if 'changeViolation' in request.POST:
        num = request.POST['changeViolation']
        if num == '':
            result = 'Invalid student ID. Please enter a valid one.'
            info = []
        else:
            info = Records.objects.filter(studentID = num)
            if info.count() == 0:
                result = 'Student ID not found. Please try again.'
            else:
                print(info[0].pk)

    context = {
        'info': info,
        'result': result,
    }

    return render(request, 'task/table.html', context)

@login_required(login_url='violation-signin')
def edit(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        data = Records.objects.get(id=pk)
        form = addViolation(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('violation-table')
        
        context = {
            'data': data,
            'form': form,
        }
        return render(request, 'task/edit.html', context)
    else:
        return HttpResponse('You are restricted to access this page. Please go back again.')