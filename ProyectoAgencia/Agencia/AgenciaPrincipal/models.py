from django.db import models
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Persona(models.Model): 
    Rut = models.CharField(max_length=30,unique=True)
    Nombre = models.CharField(max_length=30)
    ApellidoPaterno = models.CharField(max_length=30,blank=True,null=True)
    ApellidoMaterno = models.CharField(max_length=30,blank=True,null=True)
    Direccion = models.CharField(max_length=50)
    Telefono = models.IntegerField()
    Eliminado = models.BooleanField(default=False)
    def __str__(self):
        return (" Rut: "+self.Rut + " , Nombre: " + self.Nombre + " " + self.ApellidoPaterno +" "+ self.ApellidoMaterno)
    def namePersona(self):
        return (" Rut: "+self.Rut + " , Nombre: " + self.Nombre + " " + self.ApellidoPaterno +" "+ self.ApellidoMaterno)
class Chofer(Persona):
    NumeroDeLicencia = models.CharField(max_length=100)   
    
class Bus(models.Model):
    Chofer = models.ForeignKey(Chofer, on_delete=models.CASCADE)
    Patente = models.CharField(max_length=10,unique=True)
    AsientoDisponibles = models.IntegerField(default=10, )
    Pasajeros = models.CharField(default='[]', max_length=100000)
    Eliminado = models.BooleanField(default=False )
    def __str__(self):
        return self.Patente
class Pasajero(Persona):
    NumeroAsientoAsginado = models.IntegerField(null=True,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ],
    )
    BusAsignado = models.ForeignKey(Bus, on_delete=models.CASCADE,null=True,)



class Trayecto(models.Model): 
    Bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    FechaCreacion = models.DateField(auto_now_add=True, null=True, blank=True)
    Hora_Inicio = models.DateTimeField(unique=True, null=True, blank=True)
    Hora_Fin = models.DateTimeField(unique=True, null=True, blank=True)
    Lugar_Inicio = models.CharField(max_length=60)
    Lugar_Fin = models.CharField(max_length=60)  
    Eliminado = models.BooleanField(default=False ) 
