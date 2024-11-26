from django.urls import path
from . import views

urlpatterns = [
    path('auxiliar1/', views.Auxiliar1),
    path('auxiliar2/', views.Auxiliar2),
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
]

from django.urls import path
from . import views