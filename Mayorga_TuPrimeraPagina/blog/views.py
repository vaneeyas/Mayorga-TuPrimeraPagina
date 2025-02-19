from django.shortcuts import render, redirect
from .models import Curso
from .models import Profesor
from .models import Estudiante
from django.http import HttpResponse
from .forms import CursoForm

app_name="blog"

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def cursos_disponibles(request):
    curso = Curso.objects.all()
    return render(request, 'blog/cursos_disponibles.html', context={"cursos": curso})

def agregar_curso(request):
    if request.method=="POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            return redirect('cursos_disponibles')
    else:
        cursoForm = CursoForm()
    return render(request, 'blog/agregar_curso.html', context={"cursoForm": cursoForm})    

def profesores(request):
    profesor = Profesor.objects.all()
    return render(request, 'blog/profesores.html', context={"profesores": profesor})

def estudiantes(request):
    estudiante = Estudiante.objects.all()
    return render(request, 'blog/estudiantes.html', context={"estudiantes": estudiante})