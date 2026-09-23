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
"""""
def home(request):
    return render(request,"Home.html",{'Name':'Sivagiri'})
"""

def home (request):
    """
    result = os.path.join(BASE_DIR,"templates")
    print(result)
    """
    return render(request,"home.html",{'Name':'Sathya'})

def product(request):
    mobile = int(request.GET["mobile"])
    keyboard = int(request.GET["keyboard"])
    monitor = int(request.GET["monitor"])
    price = (mobile + keyboard + monitor)

    return render(request,"result.html",{'price':price})

