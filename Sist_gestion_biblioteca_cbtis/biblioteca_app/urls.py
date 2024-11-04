from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregarLibro, name='agregarLibro'),
    path('ver/', views.verListaLibro, name='verListaLibro'),
    path('ver/<int:libro_id>/', views.verlibro, name='verlibro'),
    path('buscar/', views.buscarLibro, name='buscarLibro'),
    path('borrar/', views.borrarLibro, name='borrarLibro'),
]