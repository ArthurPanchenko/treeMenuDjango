from django.shortcuts import render
from .models import Category


def index(request):
    
    return render(request, 'main_app/main.html')


def category(request, title):
    return render(request, 'main_app/main.html', {'category': title})