from django import forms
from django.shortcuts import render, redirect
from .forms import addViolation, CreateUserForm
from .forms import Records, customUser

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def home(request):
    return render(request, 'task/index.html')

def signin(request):
    if request.user.is_authenticated and request.user.is_department:
        return redirect('violation-innerpage')
    elif request.user.is_authenticated and request.user.is_student:
        return redirect('violation-studentHome')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if (user is not None and user.is_superuser) or \
                (user is not None and user.is_department):
                login(request, user)
                messages.success(request, 'Hello ' + username + '!')
                return redirect('violation-innerpage')

            elif (user is not None and user.is_superuser) or \
                (user is not None and user.is_student):
                login(request, user)
                messages.success(request, 'Hello ' + username + '!')
                return redirect('violation-studentHome')

            else:
                messages.info(request, 'Invalid credentials. Please try again.')

        return render(request, 'task/login.html')

def logoutUser(request):
    logout(request)
    return redirect('violation-signin')


def signup(request):
    if request.user.is_authenticated and request.user.department:
        return redirect('violation-innerpage')
    elif request.user.is_authenticated and request.user.is_student:
        return redirect('violation-studentHome')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                userType = form.cleaned_data.get('userType')

                if userType == 'department':
                    form.instance.is_department = True
                else:
                    form.instance.is_student = True

                form.save()
                un = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + un)
                return redirect('violation-signin')
            else:
                messages.warning(request, form.errors)

        context = {
            'form':form,
        }
        return render(request,'task/signupUsers.html', context)

@login_required(login_url='violation-signin')
def innerpage(request):
    if (request.user.is_authenticated and request.user.is_superuser) or (request.user.is_authenticated and request.user.is_department):
        return render(request, 'task/innerpage.html')
    else:
        return redirect('violation-signin')

#@login_required(login_url='violation-signin')
#def scan(request):
    return render(request, 'task/scan.html')

@login_required(login_url='violation-signin')
def scanQR(request):
    if (request.user.is_authenticated and request.user.is_superuser) or (request.user.is_authenticated and request.user.is_department):
        return render(request, 'task/scanQR.html')
    else:
        return redirect('violation-signin')

#student homepage
@login_required(login_url='violation-signin')
def studentHome(request):
    if (request.user.is_authenticated and request.user.is_superuser) or (request.user.is_authenticated and request.user.is_student):
        return render(request, 'task/student-home.html')
    else:
        return redirect('violation-signin')


# student about
@login_required(login_url='violation-signin')
def studentAbout(request):
    if (request.user.is_authenticated and request.user.is_superuser) or (request.user.is_authenticated and request.user.is_student):
        return render(request, 'task/student-about.html')
    else:
        return redirect('violation-signin')


#student view violation list
@login_required(login_url='violation-signin')
def studentViolation(request):
    if (request.user.is_authenticated and request.user.is_superuser) or (request.user.is_authenticated and request.user.is_student):
        num = ''
        result = ''
        info = ''
        if 'viewViolation' in request.GET:
            num = request.GET['viewViolation']
            if num == '':
                messages.info(request, 'Invalid student ID. Please enter a valid one.')
                info = []
                
            else:
                info = Records.objects.filter(studentID = num)
                if info.count() == 0:
                    messages.info(request, 'Student ID not found. Please try again.')
                else:
                    print(info[0])

        context = {
            'info': info,
            'result': result,
        }
        return render(request, 'task/student-violation-list.html', context)
    else:
        return redirect('violation-signin')





@login_required(login_url='violation-signin')
def createQR(request):
    if (request.user.is_authenticated and request.user.is_superuser) or (request.user.is_authenticated and request.user.is_department):
        return render(request, 'task/createQR.html') 
    else:
        return redirect('violation-signin')  

@login_required(login_url='violation-signin')
def add(request):
    if (request.user.is_authenticated and request.user.is_superuser) or (request.user.is_authenticated and request.user.is_department):
        form = addViolation()
        if request.method == 'POST':
            form = addViolation(request.POST)
            if form.is_valid():

                if Records.objects.filter(studentID = request.POST.get('studentID')).exists():
                    user = form.cleaned_data.get('studentID')
                    messages.info(request, 'There is an existing student record for ' + user + ' in the database. Please re-check if there is a typographical error.')
                else:
                    form.save()
                    user = form.cleaned_data.get('studentID')
                    messages.success(request, 'Violation record was created for ' + user)
                    return redirect('violation-list')

        context = {
            'form': form,
        }
        return render(request, 'task/add.html', context)
    else:
        return redirect('violation-signin')


@login_required(login_url='violation-signin')
def table(request):
    if (request.user.is_authenticated and request.user.is_superuser) or (request.user.is_authenticated and request.user.is_department):
        num = ''
        info = Records.objects.all()[:5]
        if 'changeViolation' in request.POST:
            num = request.POST['changeViolation']
            if num == '':
                messages.info(request, 'Invalid student ID. Please enter a valid one.')
                info = []
                
            else:
                info = Records.objects.filter(studentID = num)
                if info.count() == 0:
                    messages.info(request, 'Student ID not found. Please try again.')
                else:
                    print(info[0].pk)

        context = {
            'info': info,
        }

        return render(request, 'task/table.html', context)
    else:
        return redirect('violation-signin')

@login_required(login_url='violation-signin')
def edit(request, pk):
    if (request.user.is_authenticated and request.user.is_superuser) or (request.user.is_authenticated and request.user.is_department):
        data = Records.objects.get(id=pk)
        form = addViolation(request.POST or None, instance=data)
        if request.method == 'POST':
            if form.is_valid():

                form.save()
                user = form.cleaned_data.get('studentID')
                messages.success(request, 'Violation record was updated for ' + user)
                return redirect('violation-list')
        context = {
            'data': data,
            'form': form,
        }
        return render(request, 'task/edit.html', context)
    else:
        return redirect('violation-signin')
