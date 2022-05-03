import email
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import URLPattern
# Create your views here.
def index(request):
    return render(request,"index.html", {})

def contact(request):
    if request.method == "POST":
        name    = request.POST['name']
        email   = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        return render(request, "contact.html", {'name':name})

    else:
        return render(request, "contact.html")

def About(request):
    return render(request, "About.html", {})

def Resume(request):
    return render(request, "Resume.html", {})

def Portfolio(request):
    return render(request, "Portfolio.html", {})







