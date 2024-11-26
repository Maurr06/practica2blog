from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Articulo

# Create your views here.
def HolaMundo(request):
    return HttpResponse('<h1>Hola Mundo.</h1>')

def Auxiliar1(request):
    return HttpResponse('<h2>Hola Mundito.</h2>')

def Auxiliar2(request):
    return HttpResponse('<h3>Hola Munditito.</h3>')

def index(request):
    articulos = Articulo.objects.all()  # --- 2
    params = {  # --- 3
        'articulos': articulos,
    }
    return render(request, 'blog/index.html', params)  # --- 4