from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
"""""
def home (request):
    msg = " <h1>Welcome to Django Framework</h1>"
    return HttpResponse(msg)

def index(request):
    return HttpResponse("<h1>This is Index page</h1>")

def users(request):
    return HttpResponse("<h1>This is users page</h1>")
"""
def home(request):
    return render(request,"Home.html",{'Name':'Sivagiri'})


