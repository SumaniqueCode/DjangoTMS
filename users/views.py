from django.shortcuts import render
from django.http import HttpResponse

def users(request):
    message="<h1>This is user page</h1>"
    return HttpResponse(message)
