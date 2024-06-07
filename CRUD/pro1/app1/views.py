from django.shortcuts import render, redirect, HttpResponse
from .forms import TeacherForm
from .models import Teacher
# Create your views here.


def AddView(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    return render(request, 'app1/add.html', {'form':form})


def ShowView(request):
    obj = Teacher.objects.all()
    return render(request, 'app1/show.html', context={'obj':obj})