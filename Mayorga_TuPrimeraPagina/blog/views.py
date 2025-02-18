from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def cursos_disponibles(request):
    post_list = Post.objects.all()
    return render(request, 'blog/cursos_disponibles.html', context={"posts": post_list})