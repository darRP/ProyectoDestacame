from django.conf.urls import url,include
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import urls, routers
from rest_framework.authtoken import views
from AgenciaPrincipal.views  import  ChoferAPI, BusAPI, TrayectoAPI,  PasajeroAPI

apiurl = routers.SimpleRouter()
apiurl.register('choferes',ChoferAPI)
apiurl.register('buses',BusAPI)
apiurl.register('trayectos',TrayectoAPI)
apiurl.register('pasajeros',PasajeroAPI)

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api/', include(apiurl.urls)),
]

