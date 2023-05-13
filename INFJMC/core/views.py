from django.shortcuts import render



# Create your views here.

def home(request):
    return render(request,'core/home.html')

def carrera(request):
    return render(request,'core/carreras.html')

def docente(request):
    return render(request, 'core/docentes.html')