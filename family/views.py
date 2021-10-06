from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

def index(request): #HttpRequest
    return HttpResponse("<h1>Page of application Family.<h1>")

def members(request, membersid):
    return HttpResponse(f"<h1>About member of family</h1><p>{membersid}</p>")

def archive (request, year):
    if int(year) > 2021:
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Archive</h1><p>{year}</p>")