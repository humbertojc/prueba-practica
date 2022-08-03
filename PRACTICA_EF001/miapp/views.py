from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
# Create your views here.
def carreras(request):
    return render(request, 'carreras.html', {
        'titulo':'LISTADO DE CARRERAS'#,
    })

def cursos(request):
    return render(request, 'cursos.html', {
        'titulo':'LISTADO DE CURSOS',
        'mensaje':'Proyecto para examen final'
    })

def crear_carrera(request):
    return render(request, 'crear_carrera.html', {
        'titulo':'AGREGAR CARRERA'

    })

def crear_curso(request):
    return render(request, 'crear_curso.html', {
        'titulo':'AGREGAR CURSO',
    })