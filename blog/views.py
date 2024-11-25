from django.http import HttpResponse

# Create your views here.
def HolaMundo(request):
    return HttpResponse('<h1>Hola Mundo.</h1>')