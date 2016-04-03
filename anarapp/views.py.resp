#coding: latin-1

from anarapp.models import Yacimiento, Piedra
from django.http import HttpResponse
from django.shortcuts import render
from haystack.views import SearchView
from anarapp.forms import PiedraForm

# Create your views here.

def index(request):
    lista_de_yacimientos = Yacimiento.objects.all().order_by('nombre')
    return render(request, 'yacimientos/index.html', {
        'yacimientos':lista_de_yacimientos
        })
    
def patrimonio(request):
    return render(request, 'informacion/patrimonio.html')

def yacimiento(request, pk):
    yacimiento = Yacimiento.objects.get(codigo = pk)
    piedras = Piedra.objects.filter(yacimiento = yacimiento.id)
    print "HOLAAA"
    
    form = PiedraForm()
    
    return render(request, 'anarapp/detail.html', {
        'yacimiento' : yacimiento,
        'form' : form,
        'piedras' : piedras
    })

def piedra(request, pk):
    piedra = Piedra.objects.get(codigo = pk)
    form = PiedraForm(request.GET)
    
    return render(request, 'anarapp/piedra.html', {
        'piedra' : piedra,
        'form' : form
    })
