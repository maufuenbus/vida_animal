from rest_framework import routers
from .viewsets import * #PersonaViewSet, AnimalPerdidoViewSet, AnimalEncontradoViewSet, AnimalAdoptableViewSet, SolicitudAdopcionViewSet, SolicitudContactoViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('api/personas', PersonaViewSet, 'personas' )
router.register('api/AnimalPerdidos', AnimalPerdidoViewSet, 'animalPerdidos' )
router.register('api/animalEncontrados', AnimalEncontradoViewSet, 'animalEncontrados' )
router.register('api/animalAdoptables', AnimalAdoptableViewSet, 'animalAdoptados' )
router.register('api/solicitudAdopciones', SolicitudAdopcionViewSet, 'solicitudAdopciones' )
router.register('api/solicitudContactos', SolicitudContactoViewSet, 'solicitudContactos' )



urlpatterns = [
    path('', include(router.urls)),
    path('api/personas/<int:pk>/', PersonaViewSet.as_view({'put': 'update', 'delete': 'destroy'}), name='personas-detail'),
    path('api/AnimalPerdidos/<int:pk>/', AnimalPerdidoViewSet.as_view({'put': 'update', 'delete': 'destroy'}), name='animalPerdidos-detail'),
    path('api/animalEncontrados/<int:pk>/', AnimalEncontradoViewSet.as_view({'put': 'update', 'delete': 'destroy'}), name='animalEncontrados-detail'),
    path('api/animalAdoptables/<int:pk>/', AnimalAdoptableViewSet.as_view({'put': 'update', 'delete': 'destroy'}), name='animalAdoptados-detail'),
    path('api/solicitudAdopciones/<int:pk>/', SolicitudAdopcionViewSet.as_view({'put': 'update', 'delete': 'destroy'}), name='solicitudAdopciones-detail'),
    path('api/solicitudContactos/<int:pk>/', SolicitudContactoViewSet.as_view({'put': 'update', 'delete': 'destroy'}), name='solicitudContactos-detail'),
]
