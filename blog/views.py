from django.http import HttpResponse
from django.shortcuts import render
from .models import Articulo

from django.shortcuts import render, redirect
from .forms import ArticuloForm


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
        form = ArticuloForm(request.POST)
        if form.is_valid():
            articulo = Articulo(titulo=form.cleaned_data['titulo'], contenido=form.cleaned_data['contenido'])
            articulo.save()
            return redirect('index')
    else:
        form = ArticuloForm()

    return render(request, 'blog/create.html', {'form': form})
    #     request.method == 'POST': Verifica si el formulario fue enviado.
    # form.is_valid(): Comprueba que los datos del formulario sean correctos.
    # articulo.save(): Guarda los datos en la base de datos.
    # redirect('index'): Redirige al usuario a la página principal después de guardar.


def detail(request, articulo_id):  # --- 1
    articulo = Articulo.objects.get(id=articulo_id)  # --- 2
    params = {
        'articulo': articulo,  # Pasamos el artículo al contexto para la plantilla
    }
    return render(request, 'blog/detail.html', params)  # Renderizamos la plantilla 'detail.html'

def edit(request, article_id):
    # Obtener el artículo por su id
    articulo = Articulo.objects.get(id=article_id)
    
    # Verificar si el método de la solicitud es POST (cuando se envían datos)
    if request.method == 'POST':
        # Actualizar los campos del artículo con los datos enviados en el formulario
        articulo.titulo = request.POST['titulo']
        articulo.contenido = request.POST['contenido']
        articulo.save()  # Guardar los cambios
        return redirect('detail', article_id)  # Redirigir a la vista de detalle del artículo editado
    
    else:
        # Si no es POST, se muestra el formulario con los datos actuales del artículo
        form = ArticuloForm(initial={
            'titulo': articulo.titulo,
            'contenido': articulo.contenido,
        })
        params = {
            'articulo': articulo,  # Pasar el artículo a la plantilla
            'form': form,  # Pasar el formulario con los datos iniciales
        }
        return render(request, 'blog/edit.html', params)  # Renderizar la plantilla para editar