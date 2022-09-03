from django.shortcuts import render

from .models import Lang


def home(request):
    data = {
        'langs': Lang.objects.all()
    }
    return render(request, 'home.html', data)


def auth(request):
    return render(request, 'log_in.html')
