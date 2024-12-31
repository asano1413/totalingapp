from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Student, Grade
from .forms import StudentForm, UserForm, SubjectForm, GradeForm


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'input.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('grade_list')
            else:
                return HttpResponse("Invalid login")

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_create(request):
    if request.method == 'POST':
        form = request.POST
        if form.is_valid():
            form.save()
            return redirect('success_page')  # 登録後のリダイレクト
        else:
            # フォームにエラーがある場合
            return render(request, 'regist_user.html', {'form': form})
    else:
        # GETリクエストの場合
        form = ()
        return render(request, 'regist_user.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
    else:
        logout(request)
        return redirect('index')

def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = SubjectForm()
    return render(request, 'subject_create.html', {'form': form})

def home_view(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})


def input_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        else:
            return HttpResponse("Invalid form")


def grade_create(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request, 'input.html', {'form': form})

def grade_list(request):
    grades = Grade.objects.all()
    return render(request, 'student_list.html', {'grades': grades})