from socket import fromshare
from django import forms

class form_Pelicula(forms.Form):
    nombre = forms.CharField(max_length=40)
    actorprincipal= forms.CharField(max_length=40)
    anio = forms.IntegerField()

    

class form_Serie(forms.Form):
    nombre = forms.CharField(max_length=40)
    actorprincipal = forms.CharField(max_length=40)
    anio = forms.IntegerField()

    

class form_Documental(forms.Form):
    nombre = forms.CharField(max_length=40)
    productora = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=40)
