from django.http import HttpResponse

# Create your views here.
def HolaMundo(request):
    return HttpResponse('<h1>Hola Mundo.</h1>')

def Auxiliar1(request):
    return HttpResponse('<h2>Hola Mundito.</h2>')

def Auxiliar2(request):
    return HttpResponse('<h3>Hola Munditito.</h3>')