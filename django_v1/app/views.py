from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def Index(request):
    try:
        return HttpResponse("Hello World!")
    except Exception as e:
        return HttpResponse("Error!")