from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.template import loader

from musicshop.forms import FormularioAddPedido
from musicshop.models import Articulo


def listArt (request):
    template=loader.get_template('listArt.html')
    dato=Articulo.objects.order_by('id')
    contexto={
        'articulo': dato
    }
    return HttpResponse(template.render(
        contexto,request
    ))


def addPedido (request):
    if request.method=='POST':
        formulario=FormularioAddPedido(request.POST)
        if formulario.is_valid():
            articulo=formulario.save()
            articulo.save()
            return HttpResponseRedirect('addPedido')

    else:
        formulario=FormularioAddPedido()
    template= loader.get_template('addPedido.html')
    contexto = {
            'formulario':formulario,
        }
    return HttpResponse(template.render(contexto,request))