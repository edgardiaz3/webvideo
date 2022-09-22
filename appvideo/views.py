
from django.shortcuts import render
from django.http import HttpResponse
from appvideo.forms import *
from appvideo.models import *

# Create your views here.


def contacto(request):
    return render(request,"contacto.html")


def home(request):
    return render(request,"home.html")

def api_registrar(request):
    if request.method == "POST":
        formulario = form_Pelicula(request.POST)               
        if formulario.is_valid() :
            informacion = formulario.cleaned_data      
            pelicula = Pelicula ( nombre = informacion['nombre'], actorprincipal = informacion['actorprincipal'], anio = informacion['anio'])
            pelicula.save()
            return render ( request, "api_registrar.html")     
    else:
            formulario = form_Pelicula()
    return render ( request, "api_registrar.html", {"formulario":formulario})   
            
    
def api_registrarserie(request):
    if request.method == "POST":
        formulario2 = form_Serie(request.POST)
        if formulario2.is_valid():
            informacion2 = formulario2.cleaned_data
            serie = Serie ( nombre = informacion2['nombre'], actorprincipal = informacion2['actorprincipal'], anio = informacion2['anio'])
            serie.save()
            return render ( request, "api_registrarserie.html")
    else:
        formulario2 = form_Serie()
    return render ( request, "api_registrarserie.html",{"formulario2":formulario2 })


def api_registrardocumental(request):
    if request.method == "POST":
        formulario3 = form_Documental(request.POST)
        if formulario3.is_valid():
            informacion3 = formulario3.cleaned_data
            documental = Documental ( nombre = informacion3['nombre'], productora = informacion3['productora'], genero = informacion3['genero'])
            documental.save()
            return render ( request, "api_registrardocumental.html")
    else :
        formulario3 = form_Documental()
    return render ( request, "api_registrardocumental.html",{"formulario3":formulario3 })


def buscar_pelicula(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre",]
        peliculas = Pelicula.objects.filter(nombre__icontains = nombre)
        return render(request , "buscar_pelicula.html", {"peliculas ": peliculas})
    else:
        respuesta ="No enviaste datos"
    return HttpResponse(respuesta)

def buscar_documental(request):
    if request.GET["productora"]:
        productora = request.GET['productora',]
        documentales = Documental.objects.filter(productora__icontains = productora)
        return render(request , "buscar_documental.html", {"documentales ": documentales})
    else:
        respuesta ="No enviaste datos"
    return HttpResponse(respuesta)



#
#def registrar(request):
#    if request.method == "POST":
#            pelicula = Pelicula (nombre = request.POST['nombre'], actorprincipal= request.POST['actorprincipal'], anio= request.POST['anio'])
#            pelicula.save()
#            serie= Serie (nombre = request.POST['nombre'], actorprincipal= request.POST['actorprincipal'], anio= request.POST['anio'])
#            serie.save()
#            documental = Documental (nombre = request.POST['nombre'], productora= request.POST['productora'], genero= request.POST['genero'])
#            documental.save()
#            return render(request, "home.html")
#    return render(request,"registrar.html")




    return 0