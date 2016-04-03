# -*- coding: utf-8 -*-

from django import forms

########################################################################################
# Creando Cruces Yacimiento-Yacimiento Form
########################################################################################

OPCIONES_ESTADO = (
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

class CrucesYYForm(forms.Form):
    codigo 	= forms.CharField(required=False, max_length=20)
    estado = forms.ChoiceField(required=False, choices=OPCIONES_ESTADO)
    ubicacion = forms.CharField(required=False, max_length=20)
    carasurcopetrotipo = forms.CharField(required=False, max_length=50)
    material = forms.CharField(required=False, max_length=50)
    manifasociadas = forms.CharField(required=False, max_length=50)

    estado.widget.attrs 	= {'class':'chzn-select', 'data-placeholder':'Seleccione el estado'}
