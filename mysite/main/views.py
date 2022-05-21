from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')

def blogs(request):
    return render(request, 'main/blogs.html')

def login(request):
    return render(request, 'main/login.html')