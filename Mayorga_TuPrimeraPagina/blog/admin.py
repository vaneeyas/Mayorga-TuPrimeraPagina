from django.contrib import admin
from blog.models import Profesor, Curso, Estudiante

admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Estudiante)


from django.contrib import admin 
from .models import Curso 