from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from.models import *

menu = ['About', 'Add articles', 'Contact us', 'Sign In']

def index(request):
    posts = Family.objects.all()
    return render(request, 'family/index.html', {'posts': posts, 'menu': menu, 'title':'BILDUK -> home'})

def about(request):
    return render(request, 'family/about.html', {'menu': menu, 'title':'BILDUK -> about'})

def members(request, membersid):
    return HttpResponse(f"<h1>About member of family</h1><p>{membersid}</p>")

def archive (request, year):
    if int(year) > 2021:
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Archive</h1><p>{year}</p>")