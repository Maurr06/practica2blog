from django.db import models

# Create your models here.
class Articulo(models.Model):  # Definición del modelo Article
    titulo = models.CharField(max_length=255)  # Campo de texto con longitud máxima de 255 caracteres
    contenido = models.TextField()  # Campo de texto más extenso para contenido