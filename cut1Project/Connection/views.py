from django.shortcuts import render, redirect
from Connection.form import StudentForm, StudentinfoForm
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'home.html')


def contact(request):
    form = StudentForm()
    return render(request, 'contact.html', {'form': form})


def student(request):
    return render(request, 'student.html')


def admin(request):
    return render(request, 'admin.html')


def teacher(request):
    return render(request, 'teacher.html')


def register(request):
    form = StudentinfoForm()
    if request.method == 'POST':
        form = StudentinfoForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentinfoForm()
            messages.success(request, 'User registered successfully!')
            return redirect('register')
    else:
        form = StudentinfoForm()
        return render(request, 'register.html',{'form': form})
