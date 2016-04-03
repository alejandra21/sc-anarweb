# -*- coding: utf-8 -*-

from django.http import HttpResponse
from joins.forms import CrucesYYForm
from django.shortcuts import render
from haystack.query import SearchQuerySet
from anarapp.models import Yacimiento

def index(request):
    form = CrucesYYForm()
    return render(request, 'joins/index.html', {'form' : form})
    

UBICACIONES = [
    '','Cerro','Cima','Ladera','Falda','Fila',
    'Pie de Monte','Barranco','Acantilado','Valle',
    'Río','Lecho','Margen Derecha',
    'Margen Izquierda','Isla','Raudal','Costa'       
]

ESTADOS = [
    'Amazonas', 'Anzoategui', 'Apure',
    'Aragua', 'Barinas', 'Bolívar',
    'Carabobo', 'Cojedes', 'Delta Amacuro',
    'Falcón', 'Guárico', 'Lara', 'Mérida',
    'Miranda', 'Monagas', 'Nueva Esparta', 
    'Portuguesa', 'Sucre', 'Tachira', 
    'Trujillo', 'Vargas', 'Yaracuy', 'Zulia'
]    

MANIFESTACIONES = [
        'Geoglifo',
        'Pintura Rupestre',
        'Petroglifo',
        'Petroglifo Pintado',
        'Micro-Petroglifo',
        'Piedra Mítica Natural',
        'Cerro Mítico Natural',
        'Cerro Mitico Natural con Petroglifo',
        'Cerro Mitico Natural Con Pintura',
        'Cerro Mitico Natural Con Dolmen',
        'Monumentos Megalíticos',
        'Monolitos',
        'Monolitos Con Grabados',
        'Menhires',
        'Menhires Con Puntos Acoplados',
        'Menhires Con Petroglifo',
        'Menhires Con Pintura',
        'Amolador',
        'Batea',
        'Puntos Acoplados',
        'Cupulas',
        'Mortero o Metate'
]

#Cuentos y cuales yacimientos hay en estado
def cruce1(form):
    sqs = SearchQuerySet()
    sqs = sqs.filter(estado = form.cleaned_data['estado'])
    total = sqs.count()

    estado = form.cleaned_data['estado']
    return {
        'total' : total, 
        'estado':estado, 
        'results':sqs}
#Bibliografia
def cruce27(form):
    yacimiento = Yacimiento.objects.get(codigo = form.cleaned_data['codigo'])
    codigo = form.cleaned_data['codigo'] 
    return {
        'codigo': codigo,
        'yacimiento': yacimiento,
    }
#Listar Dolmenes y menhires
def cruce8(form):
    sqs = SearchQuerySet()
    sqs = sqs.filter(pais = 'Venezuela').filter(tipo__in = [4, 5, 6, 7, 8])
    total = sqs.count()
    yacimientos = {}
    for estado in ESTADOS:
        lista = sqs.filter(estado = estado)
        yacimientos[estado] = lista
    return {
        'total' : total, 
        'yacimientos': yacimientos}

#Numero de piedras trabajadas a numeros de piedra en el yacimiento original
def cruce9(form):
    sqs = SearchQuerySet()
    sqs = sqs.filter(estado = form.cleaned_data['estado'])
    values = {}
    for e in sqs:
        try:
            values[e.__getattribute__('codigo')] = e.object.ConstitucionYacimiento 
        except:
            pass
    piedras = sum(0 if e.nroPiedras is None else e.nroPiedras for b,e in values.items())
    grabadas = sum(0 if e.nroPiedrasGrabadas is None else e.nroPiedrasGrabadas for b,e in values.items())
    pintadas = sum(0 if e.nroPiedrasPintadas is None else e.nroPiedrasPintadas for b,e in values.items())
    colocadas = sum(0 if e.nroPiedrasColocadas is None else e.nroPiedrasColocadas for b,e in values.items())

    return {
        'estado': sqs[0].estado,
        'piedras': piedras,
        'grabadas': grabadas,
        'pintadas': pintadas,
        'colocadas': colocadas,
        'yacimientos': sqs,
    }
#Listar la manifestacion por estado
def cruce10(form):
    #Revizar que este en el estado seleccionado
    if form.cleaned_data['codigo'] != '':
        sqs = SearchQuerySet()
        sqs = sqs.filter(estado = form.cleaned_data['estado']).filter(codigo = form.cleaned_data['codigo'])
        if sqs != []:
            for yac in sqs:
                if len(yac.manifestacion) != 0:
                    if yac.manifestacion[0].encode('utf8') != 'None':
                        if int(yac.manifestacion[0]) <= 22:
                            yac.manifestacion = MANIFESTACIONES[int(yac.manifestacion[0])]
            return {
            'yacimientos': sqs}

        else:
            return {
            'yacimientos': sqs}

    #Buscar en todo ese estado
    elif form.cleaned_data['codigo'] == '':
        sqs = SearchQuerySet()
        sqs = sqs.filter(estado = form.cleaned_data['estado'])
        for yac in sqs:
            if len(yac.manifestacion) != 0:
                if yac.manifestacion[0].encode('utf8') != 'None':
                    if int(yac.manifestacion[0]) <= 22:
                        yac.manifestacion = MANIFESTACIONES[int(yac.manifestacion[0])]

        return {
        'yacimientos': sqs}

#Listar la manifestacion por ubicacion
def cruce11(form):
    ubi = UBICACIONES.index(form.cleaned_data['ubicacion'])
    sqs = SearchQuerySet()
    sqs = sqs.filter(ubicacion = ubi).order_by('estado')
    yacimientos = {}
    for estado in ESTADOS:
        lista = sqs.filter(estado = estado)
        yacimientos[estado] = lista
        ubicaciones = {}
        for m in MANIFESTACIONES:
            ubicaciones[m] = len(lista.filter(manifestacion = MANIFESTACIONES.index(m)))
        yacimientos[estado] =  ubicaciones
    return {
            'ubi' : form.cleaned_data['ubicacion'],
            'yacimientos': yacimientos}

#listar ancho y profundidad de surco grabado, de petroglifos
def cruce12(form):
    sqs = SearchQuerySet()
    sqs = sqs.filter(pais = 'Venezuela').filter(manifestacion__in = [3, 4, 5])
    yacimientos = {}
    for estado in ESTADOS:
        lista = sqs.filter(estado = estado)
        yacimientos[estado] = lista
        for l in lista:
            l.carasurcopetroancho = l.carasurcopetroancho[0]
            l.carasurcopetroprofun = l.carasurcopetroprofun[0]

    return { 
        'yacimientos': yacimientos}

#Listar por estado los petroglifos con relieve
def cruce14(form):
    tipos = ['bajo relieve lineal',
    'bajo relieve planar',
    'bajo relieve planar y lineal',
    'alto relieve lineal',
    'alto relieve planar',
    'alto relieve planar y lineal',
    'bajo relieve planar y alto relieve planar',
    'bajo relieve planar y alto relieve lineal ',
    'bajo relieve lineal y alto relieve planar',
    'bajo relieve lineal y alto relieve lineal'

    ]
    list = []

    if form.cleaned_data['carasurcopetrotipo'].lower() == tipos[0].lower():
        list.append(5)
    if form.cleaned_data['carasurcopetrotipo'].lower() == tipos[1].lower():
        list.append(6)
    if form.cleaned_data['carasurcopetrotipo'].lower() == tipos[2].lower():
        list.append(6)
        list.append(5)
    if form.cleaned_data['carasurcopetrotipo'].lower() == tipos[3].lower():
        list.append(8)
    if form.cleaned_data['carasurcopetrotipo'].lower() == tipos[4].lower():
        list.append(9)
    if form.cleaned_data['carasurcopetrotipo'].lower() == tipos[5].lower():
        list.append(8)
        list.append(9)
    if form.cleaned_data['carasurcopetrotipo'].lower() == tipos[6].lower():
        list.append(6)
        list.append(9)
    if form.cleaned_data['carasurcopetrotipo'].lower() == tipos[7].lower():
        list.append(6)
        list.append(8)
    if form.cleaned_data['carasurcopetrotipo'].lower() == tipos[8].lower():
        list.append(5)
        list.append(9)
    if form.cleaned_data['carasurcopetrotipo'].lower() == tipos[9].lower():
        list.append(5)
        list.append(8)
    sqs = SearchQuerySet()
    sqs = sqs.filter(pais = 'Venezuela').filter(carasurcopetrotipo = list)
    yacimientos = {}
    total = sqs.count()
    for estado in ESTADOS:
        lista = sqs.filter(estado = estado)
        yacimientos[estado] = lista
    return { 
    'total':total,
    'tipo':form.cleaned_data['carasurcopetrotipo'],
    'yacimientos': yacimientos}

#petroglifos con aeras interlineadas
def cruce16(form):
    area = ['areas interlineales pulidas',
    'areas interlineales rebajadas',
    'grabados superpuestos',
    'grabados rebajados'
    ]          
    list = []

    list.append(area.index(form.cleaned_data['carasurcopetrotipo'].lower())+11)

    '''if form.cleaned_data['carasurcopetrotipo'].lower() == area[0].lower():
            list.append(11)
    elif form.cleaned_data['carasurcopetrotipo'].lower() == area[1].lower():
            list.append(12)
    elif form.cleaned_data['carasurcopetrotipo'].lower() == area[2].lower():
            list.append(13)
    elif form.cleaned_data['carasurcopetrotipo'].lower() == area[3].lower():
            list.append(14)'''
    sqs = SearchQuerySet()
    sqs = sqs.filter(pais = 'Venezuela').filter(carasurcopetrotipo = list,manifestacion__in = [3,4,5])
    return {'cruce':form.cleaned_data['carasurcopetrotipo'],
            'yacimientos': sqs}

#Roca del petroglifo
def cruce17(form):
    value = ''
    filters = ['roca ignea',
    'roca metamorfica',
    'roca sedimentaria',
    'erosion parcialmente moderada',
    'erosion parcialmente severa',
    'erosion extensiva moderada',
    'erosion extensiva severa'
    ]
    list = []

    list.append(filters.index(form.cleaned_data['material'].lower()) +1)

    if list[0] <=3 and 1 <= list[0]:
        value = 'material'
    else:
        value == 'conservacion'
        list[0] = list[0] -1

    '''if form.cleaned_data['material'].lower() == filters[0].lower:
        value = 'material'
        list.append(1)
    elif form.cleaned_data['material'].lower() == filters[1].lower:
        value = 'material'
        list.append(2)
    elif form.cleaned_data['material'].lower() == filters[2].lower:
        value = 'material'
        list.append(3)
    elif form.cleaned_data['material'].lower() == filters[3].lower:
        value = 'conservacion'
        list.append(3)
    elif form.cleaned_data['material'].lower() == filters[4].lower:
        value = 'conservacion'
        list.append(4)
    elif form.cleaned_data['material'].lower() == filters[5].lower:
        value = 'conservacion'
        list.append(5)
    elif form.cleaned_data['material'].lower() == filters[6].lower:
        value = 'conservacion'
        list.append(6)'''

    sqs = SearchQuerySet()
    sqs = sqs.filter(pais = 'Venezuela').filter(value = list,manifestacion__in = [3,4,5])
    yacimientos = {}
    for estado in ESTADOS:
        lista = sqs.filter(estado = estado)
        yacimientos[estado] = lista
    return {
    'tipo':form.cleaned_data['material'],
    'yacimientos': yacimientos}

#Mafinistacion asociada a litica,ceramica, osea,etc
def cruce19(form):
    filters = ['litica',
    'ceramica',
    'oseo',
    'concha',
    'carbon no superficial',
    'mitos',
    'cementerios',
    'monticulos',
    'otros'
    ]
    list = 0
    try:
        list = filters.index(form.cleaned_data['manifasociadas'].lower()) + 1
        sqs = SearchQuerySet()
        sqs = sqs.filter(pais = 'Venezuela').filter(manifasociadas = list)
        yacimientos = {}
        lista = []
        for estado in ESTADOS:
            lista = sqs.filter(estado = estado)
            yacimientos[estado] = lista
        return {
        'manifa':form.cleaned_data['manifasociadas'],
        'yacimientos': yacimientos}

    except:
        return {}

#proporcion de piedra en petroglifos y ubicacion
def cruce20(form):
  ubi = UBICACIONES.index(form.cleaned_data['ubicacion'])
  sqs = SearchQuerySet()
  sqs = sqs.filter(ubicacion = ubi, manifestacion__in = [3, 4, 5]).order_by('estado')
  yacimientos = {}
  for estado in ESTADOS:
    lista = sqs.filter(estado = estado)
    yacimientos[estado] = lista
  return {
    'yacimientos':yacimientos,
    'ubica':form.cleaned_data['ubicacion']}
  


def cruces(request, cruce_id):
    form = CrucesYYForm(request.GET)
    if form.is_valid():
        functions = {1:cruce1,
        2:cruce27,
        3:cruce27,
        4:cruce27,
        5:cruce27,
        6:cruce27,
        7:cruce27,
        8:cruce8,
        9:cruce9,
        10:cruce10,
        11:cruce11,
        12:cruce12,
        13:render(request, 'joins/index.html', {'form' : form}),
        14:cruce14,
        15:render(request, 'joins/index.html', {'form' : form}),
        16:cruce16,
        17:cruce17,
        18:render(request, 'joins/index.html', {'form' : form}),
        19:cruce19,
        20:cruce20
        }
        if(cruce_id == '13' or cruce_id == '15' or cruce_id == 18):
           return render(request, 'joins/index.html', {'form' : form})
        func = functions[int(cruce_id)]
        dic = func(form)
        return render(request,'joins/cruce'+cruce_id+'.html',dic)

    