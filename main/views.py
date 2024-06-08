from django.shortcuts import render, redirect
from django.http import HttpResponse

from main.forms import AddStudentForm
from main.models import News


def index(request):
    news = News.objects.order_by('-time_create')
    return render(request, 'main/index.html', {'news': news})

def about(request):
    return render(request, 'main/aboutUs.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def signup(request):

    if request.method == 'POST':
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddStudentForm()
    return render(request, 'main/signup.html', {'form': form})