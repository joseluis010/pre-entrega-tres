from django.http import HttpResponse
from  django.template import Context, Template


def inicio(request): # el index 
    return HttpResponse("hola ")