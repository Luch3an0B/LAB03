from django.shortcuts import render
from django.http import HttpResponse
from django.http import render

# Create your views here.
def index(request):
    return HttpResponse("Hola Mundo")

def home(request):
    return render(request,'core/home.html')

def carreras(request):
    return HttpResponse()

def docentes(request):
    return HttpResponse()