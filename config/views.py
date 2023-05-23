from django.http import HttpResponse
from django.shortcuts import render 

#from  django.template import Context, Template


def inicio(request): # el index 
    return HttpResponse("hola ")


def probando_template(request):
   # Es necesario importar las clases Context y Template: from django.template import Context, Template
    mi_html = open("./templates/template1.html", encoding="utf-8")
    mi_template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context()
    mi_documento = mi_template.render(mi_contexto) 
    return HttpResponse(mi_documento)