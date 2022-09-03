from django.shortcuts import render

from main.models import Lang


def home(request):
    return render(request, 'header.html')


def auth(request):
    return render(request, 'log_in.html')
