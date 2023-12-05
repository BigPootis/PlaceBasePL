from django.shortcuts import render
from .models import Articles

def events(request):
    event=Articles.objects.all()
    return render(request, 'events/events.html', {'title':"Events",'event':event})

def login(request):
    return render(request, 'main/login.html', {'title': 'Login'})


# Create your views here.
