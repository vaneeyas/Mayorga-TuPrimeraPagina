from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def cursos_disponibles(request):
    miCurso = Curso.objects.all()
    return render(request, 'blog/cursos_disponibles.html', context={"cursos": miCurso})