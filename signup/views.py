from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(requests):
    return HttpResponse("<h1> Welcome to signup page. </h1>")