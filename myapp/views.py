from django.shortcuts import render, redirect

from .models import Student
from .forms import StudentForm, RegisterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.core.paginator import Paginator

@login_required
def home(request):

    students = Student.objects.filter(
        user=request.user
    )


    search = request.GET.get('search')


    if search:

        students = students.filter(
            name__icontains=search
        )


    paginator = Paginator(
        students,
        5
    )


    page_number = request.GET.get(
        'page'
    )


    students = paginator.get_page(
        page_number
    )


    return render(
        request,
        'myapp/home.html',
        {
            'students': students,
            'search': search
        }
    )


@login_required
def add_student(request):

    form = StudentForm()


    if request.method == "POST":

        form = StudentForm(
            request.POST
        )


        if form.is_valid():

            student = form.save(
                commit=False
            )

            student.user = request.user

            student.save()


            messages.success(
                request,
                "Student added successfully"
            )


            return redirect('home')


    return render(
        request,
        'myapp/add_student.html',
        {'form': form}
    )


@login_required
def update_student(request, id):

    student = Student.objects.get(
        id=id,
        user=request.user
    )


    form = StudentForm(
        instance=student
    )


    if request.method == "POST":

        form = StudentForm(
            request.POST,
            instance=student
        )


        if form.is_valid():

            form.save()


            messages.success(
                request,
                "Student updated successfully"
            )


            return redirect('home')


    return render(
        request,
        'myapp/add_student.html',
        {'form': form}
    )


@login_required
def delete_student(request, id):

    student = Student.objects.get(
        id=id,
        user=request.user
    )


    student.delete()


    messages.success(
        request,
        "Student deleted successfully"
    )


    return redirect('home')


def register(request):

    form = RegisterForm()


    if request.method == "POST":

        form = RegisterForm(
            request.POST
        )


        if form.is_valid():

            user = form.save()

            login(
                request,
                user
            )


            messages.success(
                request,
                "Account created successfully"
            )


            return redirect('home')


    return render(
        request,
        'myapp/register.html',
        {'form': form}
    )
        
@login_required
def profile(request):

    total_students = Student.objects.filter(
        user=request.user
    ).count()


    return render(
        request,
        'myapp/profile.html',
        {
            'total_students': total_students
        }
    )

    return render(
        request,
        'myapp/register.html',
        {'form': form}
    )