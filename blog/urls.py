from django.urls import path
from . import views

urlpatterns = [
    path('auxiliar1/', views.Auxiliar1),
    path('auxiliar2/', views.Auxiliar2),
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:articulo_id>', views.detail, name='detail'),  # Ruta para la vista de detalles con un parámetro dinámico 'articulo_id'
    path('edit/<int:article_id>/', views.edit, name='edit'),  # Agregado el '/' al final
]

from django.urls import path
from . import views