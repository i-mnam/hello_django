# dojo.views.py

from django.http import HttpResponse
from django.shortcuts import render


def mysum(request, x, y=0, z=0):
    # request : HttpRequest
    return HttpResponse("x:"+ str(int(x)+1) 
        + "y: " + str(int(y)+10)
        + "z: " + str(int(z) + 100)
        ) 