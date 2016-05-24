from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    print request
    title = "<center><h1>Hello, world. Welcome to index page of Polls !</h1></center>"
    return HttpResponse(title)
