from django.http import HttpResponse
from django.shortcuts import render 

#from  django.template import Context, Template


def inicio(request): # el index 
    return HttpResponse("hola ")


def probando_template_render(request): 
    nombre = "Louis" 
    apellido = "Van Beethoven" 
    datos = { "nombre": nombre, "apellido": apellido}
    return render(request, "template1.html", context=datos)


def probando_template2(request):
    lista_de_notas = [2, 2, 3, 7, 5] 
    contexto = {"notas": lista_de_notas} 
    return render(request, "template2.html", contexto)