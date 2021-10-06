from django.http.response import HttpResponse
from django.shortcuts import render

def index(request): #HttpRequest
    return HttpResponse("<h1>Page of application Family.<h1>")

def members(request):
    return HttpResponse("<h1>About member of family</h1>")
