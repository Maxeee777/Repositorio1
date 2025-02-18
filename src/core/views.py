from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def saludar(request):
    return HttpResponse("Hola desde Djangoooo")

def saludar_con_parametros(request, nombre:str, apellido:str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"Mi nombre es {nombre} y mi apellido {apellido}")

def index (request):
    return render(request, "core/index.html")