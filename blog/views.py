from django.http import HttpResponse
from django.shortcuts import render
from .models import Articulo

from django.shortcuts import render, redirect
from .forms import ArticleForm


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

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = Articulo(titulo=form.cleaned_data['titulo'], contenido=form.cleaned_data['contenido'])
            article.save()
            return redirect('index')
    else:
        form = ArticleForm()

    return render(request, 'blog/create.html', {'form': form})
    #     request.method == 'POST': Verifica si el formulario fue enviado.
    # form.is_valid(): Comprueba que los datos del formulario sean correctos.
    # article.save(): Guarda los datos en la base de datos.
    # redirect('index'): Redirige al usuario a la página principal después de guardar.