from django import forms

class ArticuloForm(forms.Form):
    titulo = forms.CharField(label='Título', max_length=255)
    contenido = forms.CharField(label='Contenido', widget=forms.Textarea())