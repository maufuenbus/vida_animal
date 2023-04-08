from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('datos_api_bd.urls'))
#     path('api/v1.0/', include('persona.urls')),
#     path('api/v1.0/', include('animalPerdido.urls')),
#     path('api/v1.0/', include('animalEncontrado.urls')),
#     path('api/v1.0/', include('animalAdoptable.urls')),
#     path('api/v1.0/', include('solicitudAdopcion.urls')),
#     path('api/v1.0/', include('solicitudContacto.urls')),
]
