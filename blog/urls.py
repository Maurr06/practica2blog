from django.urls import path
from . import views

urlpatterns = [
    path('auxiliar1/', views.Auxiliar1),
    path('auxiliar2/', views.Auxiliar2)
]