from django.shortcuts import render
from django.http import HttpResponse

from main.models import News


def index(request):
    news = News.objects.order_by('-time_create')
    return render(request, 'main/index.html', {'news': news})
# Create your views here.
