from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def message(request):
    return render(request,"Message.html")

def success(request):
    messages.success(request,"This is Success Message")
    return render(request,'Message.html')

def info(request):
    messages.success(request,"This is Info Message")
    return render(request,'Message.html')

def error(request):
    messages.success(request,"This is Error Message")
    return render(request,'Message.html')

def warning(request):
    messages.success(request,"This is Warning Message")
    return render(request,'Message.html')


