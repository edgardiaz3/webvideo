from django.db import models

# Create your models here.

class Pelicula(models.Model):
    nombre = models.CharField(max_length=40)
    actorprincipal= models.CharField(max_length=40)
    anio = models.IntegerField()

    #def __str__(self):
        #return f"Nombre: {self.nombre} - actor principal {self.actorprincipal} - anio {self.anio}"

class Serie(models.Model):
    nombre = models.CharField(max_length=40)
    actorprincipal = models.CharField(max_length=40)
    anio = models.IntegerField()

    #def __str__(self):
        #return f"Nombre: {self.nombre} - actor principal {self.actorprincipal} - anio {self.anio}"


class Documental(models.Model):
    nombre = models.CharField(max_length=40)
    productora = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)

    #def __str__(self):
        #return f"Nombre: {self.nombre} - Productora {self.productora} - genero {self.genero}"