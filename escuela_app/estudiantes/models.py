from django.db import models

# Create your models here.


class Estudiante(models.Model):
    id_e = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50)
    edad = models.PositiveSmallIntegerField()

    def __str__(self):
        nombre = "Id: " + self.id_e + " - " + "Nombre: " + self.nombre
        return nombre


class Materia(models.Model):
    codigo = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50)
    credito = models.PositiveSmallIntegerField()


    def __str__(self):
        nombre = "Codigo: " + self.codigo + " - " + "Nombre: " + self.nombre
        return nombre
        
#class Calificacion(models.Model):
#    id_c = models.CharField(primary_key=True, max_length=50)
#    nota_1 = models.PositiveSmallIntegerField()
#    nota_2 = models.PositiveSmallIntegerField()
#    nota_3 = models.PositiveSmallIntegerField()
#    Acumulado = models.PositiveSmallIntegerField()
#   Desicion = models.CharField(primary_key=True, max_length=50)


    