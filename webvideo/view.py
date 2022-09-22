from django.http import HttpResponse
from django.template import Template, Context
import pathlib

from appvideo.urls import *

def inicio(request):
    return render(request,"inicio.html")

def contacto(request):
    return render(request,"contacto.html")



