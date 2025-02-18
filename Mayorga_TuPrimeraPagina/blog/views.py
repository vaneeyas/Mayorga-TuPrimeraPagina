from django.shortcuts import render
from .models import Curso
from .models import Profesor
from .models import Estudiante
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def cursos_disponibles(request):
    curso = Curso.objects.all()
    return render(request, 'blog/cursos_disponibles.html', context={"cursos": curso})

def profesores(request):
    profesor = Profesor.objects.all()
    return render(request, 'blog/profesores.html', context={"profesores": profesor})

def estudiantes(request):
    estudiante = Estudiante.objects.all()
    return render(request, 'blog/estudiantes.html', context={"estudiantes": estudiante})