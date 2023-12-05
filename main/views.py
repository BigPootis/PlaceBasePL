from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html', {'title':"PlaceBase"})

def login(request):
    return render(request, 'main/login.html', {'title': 'Login'})



# Create your views here.
