from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
# ----    
    path('estudiante', views.estudiante, name='estudiante'),
    path('estudiante/crear', views.crear_estudiante, name='crear_estudiante'),
    path('estudiante/editar', views.editar_estudiante, name='editar_estudiante'),

# ----
    path('materia', views.materia, name='materia'),
    path('materia/crear', views.crear_materia, name='crear_materia'),
    path('materia/editar', views.editar_materia, name='editar_materia'),
]