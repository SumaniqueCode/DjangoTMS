from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    date = datetime.now().date()
    time = datetime.now().time().strftime("%H:%M:%S")
    data = "<h1>Hello, World!</h1><h3>Current date is: "+str(date)+" and current time is : "+str(time)+".</h3>"
    return HttpResponse(data)

def routeError(request):
    error_message = "<h1>Page Not Found!</h1><h3> Go back to home.</h3> <a href ='/home'><button>Go back</button></a>"
    return HttpResponse(error_message)
