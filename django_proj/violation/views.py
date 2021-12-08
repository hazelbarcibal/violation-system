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

    context = {
        'form': form,
    }
    return render(request, 'task/add.html', context)


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

def edit(request, pk):
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
