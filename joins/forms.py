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

OPCIONES_SURCO_GRABADO = (
	('---', '---'),
	('Bajo relieve lineal','Bajo relieve lineal'),
	('Bajo relieve planar','Bajo relieve planar'),
	('Alto relieve lineal','Alto relieve lineal'),
	('Alto relieve planar','Alto relieve planar'),
	('Áreas interlineales pulidas','Áreas interlineales pulidas'),
	('Áreas interlineales rebajadas','Áreas interlineales rebajadas'),
	('Grabados superpuestos','Grabados superpuestos'),
	('Grabados rebajados','Grabados rebajados'),
	('Re-grabados','Re-grabados'),
)

OPCIONES_TIPO_PINTURA = (

	('---', '---'),
	('Pintura positiva negra','Pintura positiva negra'),
	('Pintura positiva blanca','Pintura positiva blanca'),
	('Pintura positiva amarilla','Pintura positiva amarilla'),
	('Pintura positiva roja','Pintura positiva roja'),
	('Pintura positiva dos rojos','Pintura positiva dos rojos'),
	('Pintura positiva tres rojos','Pintura positiva tres rojos'),
	('Pintura negativa negra','Pintura negativa negra'),
	('Pintura negativa blanca','Pintura negativa blanca'),
	('Pintura negativa amarilla','Pintura negativa amarilla'),
	('Pintura negativa roja','Pintura negativa roja'),
	('Pintura negativa dos rojos','Pintura negativa dos rojos'),
	('Pintura negativa tres rojos','Pintura negativa tres rojos'),
)

OPCIONES_MATERIAL = (

	('---', '---'),
	('Roca ígnea','Roca ígnea'),
	('Roca metamórfica','Roca metamórfica'),
	('Roca sedimentaria','Roca sedimentaria'),
	('Erosión','Erosión'),
)

OPCIONES_CARACTERISTICA_SURCO = (
	('---', '---'),
	('Base redonda','Base redonda'),
	('Información de abrasión','Información de abrasión'),
	('Base aguda','Base aguda'),
	('Información de persusión','Información de persusión'),
)

OPCIONES_PIEDRA_EROSION = (
	('---', '---'),
	('Tipo de línea sencilla','Tipo de línea sencilla'),
	('Tipo de línea compuesta','Tipo de línea compuesta'),
	('Color base','Color base'),
)




class CrucesYYFormAdmin(forms.Form):
    codigo 	= forms.CharField(required=False, max_length=20)
    estado = forms.ChoiceField(required=False, choices=OPCIONES_ESTADO)
    ubicacion = forms.ChoiceField(required=False, choices=OPCIONES_UBICACION)
    carasurcopetrotipo = forms.ChoiceField(required=False, choices=OPCIONES_SURCO_GRABADO)
    tipoPintura = forms.ChoiceField(required=False, choices=OPCIONES_TIPO_PINTURA)
    caracteristicaSurco = forms.ChoiceField(required=False, choices=OPCIONES_CARACTERISTICA_SURCO)
    piedraErosion = forms.ChoiceField(required=False, choices=OPCIONES_PIEDRA_EROSION)
    material = forms.ChoiceField(required=False, choices=OPCIONES_MATERIAL)
    manifasociadas = forms.ChoiceField(required=False,widget=forms.Select,choices=OPCIONES_MANIFESTACIONES)
    estado.widget.attrs 	= {'class':'chzn-select', 'data-placeholder':'Seleccione el estado'}

class CrucesYYForm(forms.Form):
	nombre 	= forms.CharField(required=False, max_length=100)
	estado = forms.ChoiceField(required=False,widget=forms.Select, choices=OPCIONES_ESTADO)
	manifestacion = forms.ChoiceField(required=False,widget=forms.Select,choices=OPCIONES_MANIFESTACIONES)
	nombre.widget.attrs    =  {'class':'special','placeholder':'Introduzca el nombre'}
	estado.widget.attrs 	= {'class':'chzn-select', 'placeholder':'Seleccione el estado'}
