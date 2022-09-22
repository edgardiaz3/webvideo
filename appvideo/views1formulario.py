

#Joel, con este codigo intente hacer que en una sola pantalla aparecieran los tres formularios, pero no funcionaba, si mandaba y se almacenaba la informacion pero mezclaba la informacion que se introducia.
#¿Alguna sugerencia?

#from django.shortcuts import render
#from django.http import HttpResponse
#from appvideo.forms import *
#from appvideo.models import *
## Create your views here.
#
#
#def contacto(request):
#    return render(request,"contacto.html")
#
#
#def home(request):
#    return render(request,"home.html")
#
#def api_registrar(request):
#    if request.method == "POST":
#        formulario = form_Pelicula(request.POST)
#        formulario2 = form_Serie(request.POST)
#        formulario3 = form_Documental(request.POST)
#        if formulario.is_valid() & formulario2.is_valid() & formulario3.is_valid():
#            informacion = formulario.cleaned_data
#                   
#            pelicula = Pelicula ( nombre = informacion['nombre'], actorprincipal = informacion['actorprincipal'], anio = informacion['anio'])
#            pelicula.save()
#            informacion2 = formulario2.cleaned_data
#            serie = Serie ( nombre = informacion2['nombre'], actorprincipal = informacion2['actorprincipal'], anio = informacion2['anio'])
#            serie.save()
#            informacion3 = formulario3.cleaned_data
#            documental = Documental ( nombre = informacion3['nombre'], productora = informacion3['productora'], genero = informacion3['genero'])    
#            documental.save()
#            return render ( request, "api_registrar.html")
#    else:
#            formulario = form_Pelicula()
#            formulario2 = form_Serie()
#            formulario3 = form_Documental()
#    return render ( request, "api_registrar.html", {"formulario":formulario ,"formulario2":formulario2 ,"formulario3":formulario3 })
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
#
#
#
#
#    return 0