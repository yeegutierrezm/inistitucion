from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import EstudianteForm

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

# --------
def estudiante(request):
    estudiante = Estudiante.objects.all()
    return render(request, 'estudiante/index.html', {'estudiante': estudiante })

def crear_estudiante(request):
    formulario = EstudianteForm(request.POST or None)
    return render(request, 'estudiante/crear.html', {'formulario': formulario})

def editar_estudiante(request):
    return render(request, 'estudiante/editar.html')

# --------
def materia(request):
    materia = Materia.objects.all()
    return render(request, 'materia/index.html', {'materia': materia })

def crear_materia(request):
    return render(request, 'materia/crear.html')

def editar_materia(request):
    return render(request, 'materia/editar.html')
