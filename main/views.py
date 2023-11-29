from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def hot(request):
    return HttpResponse("""<h1>Говно</h1>
                         <h2><a href='http://127.0.0.1:8000'>и</a></h2>   
                        <h3>моча</h3>
                            """)


# Create your views here.
