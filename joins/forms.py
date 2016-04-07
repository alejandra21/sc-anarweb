# -*- coding: utf-8 -*-

from django import forms

########################################################################################
# Creando Cruces Yacimiento-Yacimiento Form
########################################################################################

OPCIONES_ESTADO = (
	('---', '---'),
	('Amazonas'	, 'Amazonas'),
	('Anzoategui', 'Anzoategui'),
	('Apure', 'Apure'),
	('Aragua', 'Aragua'),
	('Barinas', 'Barinas'),
	('Bolívar', 'Bolívar'),
	('Carabobo', 'Carabobo'),
	('Cojedes', 'Cojedes'),
	('Delta Amacuro', 'Delta Amacuro'),
	('Falcón', 'Falcón'),
	('Guárico', 'Guárico'),
	('Lara', 'Lara'),
	('Mérida', 'Mérida'),
	('Miranda', 'Miranda'),
	('Monagas', 'Monagas'),
	('Nueva Esparta', 'Nueva Esparta'),
	('Portuguesa', 'Portuguesa'),
	('Sucre', 'Sucre'),
	('Tachira', 'Tachira'),
	('Trujillo', 'Trujillo'),
	('Vargas', 'Vargas'),
	('Yaracuy', 'Yaracuy'),
	('Zulia', 'Zulia'),

)

OPCIONES_MANIFESTACIONES = (
	('---', '---'),
	('Pinturas Rupestres','Pinturas Rupestres'),
	('Cerros y Piedras Miticas Naturales','Cerros y Piedras Miticas Naturales'),
	('Amoladores,Cupula,Puntos Acoplados','Amoladores,Cúpula,Puntos Acoplados'),
	('Geoglifo','Geoglifo'),
	('Micropentoglifos','Micropentoglifos'),
	('Monumentos megaliticos','Monumentos megaliticos'),
	('Petroglifos','Petroglifos'),
)

OPCIONES_UBICACION = (
	('---', '---'),
	('Cerro','Cerro'),
	('Cima','Cima'),
	('Ladera','Ladera'),
	('Fila','Fila'),
	('Pie de montaña','Pie de montaña'),
	('Barranco','Barranco'),
	('Acantilado','Acantilado'),
	('Cerro','Cerro'),
	('Valle','Valle'),
	('Río','Río'),
	('Lecho','Lecho'),
	('Margen izquierdo','Margen izquierdo'),
	('Margen derecho','Margen derecho'),
	('Isla','Isla'),
	('Raudal','Raudal'),
	('Costa','Costa'),
)



class CrucesYYFormAdmin(forms.Form):
    codigo 	= forms.CharField(required=False, max_length=20)
    estado = forms.ChoiceField(required=False, choices=OPCIONES_ESTADO)
    ubicacion = forms.ChoiceField(required=False, choices=OPCIONES_UBICACION)
    carasurcopetrotipo = forms.CharField(required=False, max_length=50)
    material = forms.CharField(required=False, max_length=50)
    manifasociadas = forms.ChoiceField(required=False,widget=forms.Select,choices=OPCIONES_MANIFESTACIONES)
    estado.widget.attrs 	= {'class':'chzn-select', 'data-placeholder':'Seleccione el estado'}

class CrucesYYForm(forms.Form):
	nombre 	= forms.CharField(required=False, max_length=100)
	estado = forms.ChoiceField(required=False,widget=forms.Select, choices=OPCIONES_ESTADO)
	manifestacion = forms.ChoiceField(required=False,widget=forms.Select,choices=OPCIONES_MANIFESTACIONES)
	nombre.widget.attrs    =  {'class':'special','placeholder':'Introduzca el nombre'}
	estado.widget.attrs 	= {'class':'chzn-select', 'placeholder':'Seleccione el estado'}
