from django.shortcuts import render, get_object_or_404
from rest_framework import serializers, viewsets, generics
from .models import Persona, Chofer, Bus, Trayecto, Pasajero
from .serializer import  ChoferSerializer, BusSerializer, TrayectoSerializer, PasajeroSerializer


# Create your views here.
class ChoferAPI(viewsets.ModelViewSet):
    queryset=Chofer.objects.all()
    serializer_class = ChoferSerializer
class BusAPI(viewsets.ModelViewSet):
    queryset=Bus.objects.all()
    serializer_class = BusSerializer
class TrayectoAPI(viewsets.ModelViewSet):
    queryset=Trayecto.objects.all()
    serializer_class = TrayectoSerializer

class PasajeroAPI(viewsets.ModelViewSet):
    queryset=Pasajero.objects.all()
    serializer_class = PasajeroSerializer 
