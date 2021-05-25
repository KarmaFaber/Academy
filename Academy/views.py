from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render


def index_father(request):
    doc_index=loader.get_template('index_father.html')
    doc=doc_index.render()
    return HttpResponse(doc)

def ingresar(request):
    doc_index=loader.get_template('ingresar.html')
    doc=doc_index.render()
    return HttpResponse(doc)


def p_privacidad(request):
    doc_index=loader.get_template('politicaPrivacidad.html')
    doc=doc_index.render()
    return HttpResponse(doc)






