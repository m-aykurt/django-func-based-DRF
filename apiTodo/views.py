from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to API Todo</h1>")
