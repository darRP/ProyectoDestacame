from rest_framework import serializers
from .models import Persona, Chofer, Bus, Trayecto,  Pasajero


class ChoferSerializer(serializers.ModelSerializer):
   class Meta:
       model = Chofer
       fields = ('id','Rut','Nombre', 'ApellidoPaterno','ApellidoMaterno','Direccion','Telefono','NumeroDeLicencia','Eliminado')
class PasajeroSerializer(serializers.ModelSerializer):
   class Meta:
       model = Pasajero 
       fields = ('id','Rut','Nombre', 'ApellidoPaterno','ApellidoMaterno','Direccion','Telefono','NumeroAsientoAsginado', 'BusAsignado','Eliminado')
class BusSerializer(serializers.ModelSerializer):
   class Meta:
       model = Bus
       fields = ('id','Chofer','Patente','AsientoDisponibles','Pasajeros','Eliminado')

class TrayectoSerializer(serializers.ModelSerializer):
   class Meta:
       model = Trayecto
       fields = ('id','FechaCreacion','Hora_Inicio','Hora_Fin','Bus','Lugar_Inicio','Lugar_Fin','Eliminado')