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
	('(14.1) Cerro','(14.1) Cerro'),
	('(14.1.1) Cima','(14.1.1) Cima'),
	('(14.1.2) Ladera','(14.1.2) Ladera'),
	('(14.1.4) Fila','(14.1.4) Fila'),
	('(14.1.5) Pie de montaña','(14.1.5) Pie de montaña'),
	('(14.1.6) Barranco','(14.1.6) Barranco'),
	('(14.1.7) Acantilado','(14.1.7) Acantilado'),
	('(14.2) Valle','(14.2) Valle'),
	('(14.3) Río','(14.3) Río'),
	('(14.3.1) Lecho','(14.3.1) Lecho'),
	('(14.3.2) Margen derecha','(14.3.2) Margen derecha'),
	('(14.3.3) Margen izquierda','(14.3.3) Margen izquierda'),
	('(14.3.4) Isla','(14.3.4) Isla'),
	('(14.3.5) Raudal','(14.3.5) Raudal'),
	('(14.4) Costa','(14.4) Costa'),
	('(14.5) En el mar','(14.5) En el mar'),
)

OPCIONES_SURCO_GRABADO = (
	('---', '---'),
	('(24.1.2.1) Bajo relieve lineal','(24.1.2.1) Bajo relieve lineal'),
	('(24.1.2.2) Bajo relieve planar','(24.1.2.2) Bajo relieve planar'),
	('(24.1.2.1 y 24.1.2.2) Bajo relieve planar y lineal','(24.1.2.1 y 24.1.2.2) Bajo relieve planar y lineal'),
	('(24.1.3.1) Alto relieve lineal ','(24.1.3.1) Alto relieve lineal'),
	('(24.1.3.2) Alto relieve planar','(24.1.3.2) Alto relieve planar'),
)

OPCIONES_SURCO_GRABADO2 = (
	('---', '---'),
	('(24.1.12.1) Áreas interlineales pulidas','(24.1.12.1) Áreas interlineales pulidas'),
	('(24.1.12.2) Áreas interlineales rebajadas','(24.1.12.2) Áreas interlineales rebajadas'),
	('(24.1.12.3) Grabados superpuestos','(24.1.12.3) Grabados superpuestos'),
	('(24.1.12.4) Grabados rebajados','(24.1.12.4) Grabados rebajados'),
	('(24.1.12.5) Re-grabados','(24.1.12.5) Re-grabados'),
)

OPCIONES_SURCO_GRABADO3 = (
	('---','---'),
	('(24.1.1) Ancho de surco','(24.1.1) Ancho de surco'),
	('(24.1.2) Profundidad de surco','(24.1.2) Profundidad de surco'),
	('(24.1.3.1) Base redonda','(24.1.3.1) Base redonda'),
	('(24.1.3.2) Base aguda','(24.1.3.2) Base aguda'),
	('(24.1.2.1) Bajo relieve lineal','(24.1.2.1) Bajo relieve lineal'),
	('(24.1.2.2) Bajo relieve planar','(24.1.2.2) Bajo relieve planar'),
	('(24.1.3.1) Alto relieve lineal','(24.1.3.1) Alto relieve lineal'),
	('(24.1.3.2) Alto relieve planar','(24.1.3.2) Alto relieve planar'),
)

OPCIONES_TIPO_PINTURA = (

	('---', '---'),
	('(25.6.1.1) Pintura positiva negra','(25.6.1.1) Pintura positiva negra'),
	('(25.6.1.2) Pintura positiva blanca','(25.6.1.2) Pintura positiva blanca'),
	('(25.6.1.3) Pintura positiva amarilla','(25.6.1.3) Pintura positiva amarilla'),
	('(25.6.1.4) Pintura positiva roja','(25.6.1.4) Pintura positiva roja'),
	('(25.6.1.5) Pintura positiva dos rojos','(25.6.1.5) Pintura positiva dos rojos'),
	('(25.6.1.6) Pintura positiva tres rojos','(25.6.1.6) Pintura positiva tres rojos'),
	('(25.6.2.1) Pintura negativa negra','(25.6.2.1) Pintura negativa negra'),
	('(25.6.2.2) Pintura negativa blanca','(25.6.2.2) Pintura negativa blanca'),
	('(25.6.2.3) Pintura negativa amarilla','(25.6.2.3) Pintura negativa amarilla'),
	('(25.6.2.4) Pintura negativa roja','(25.6.2.4) Pintura negativa roja'),
	('(25.6.2.5) Pintura negativa dos rojos','(25.6.2.5) Pintura negativa dos rojos'),
	('(25.6.2.6) Pintura negativa tres rojos','(25.6.2.6) Pintura negativa tres rojos'),
)

OPCIONES_MATERIAL = (

	('---', '---'),
	('(22.1.1) Roca ígnea','(22.1.1) Roca ígnea'),
	('(22.1.2) Roca metamórfica','(22.1.2) Roca metamórfica'),
	('(22.1.3) Roca sedimentaria','(22.1.3) Roca sedimentaria'),
	('(27.4.9, 27.4.9.1, 27.4.9.2, 27.4.9.3, 27.4.9.4) Erosión','(27.4.9, 27.4.9.1, 27.4.9.2, 27.4.9.3, 27.4.9.4) Erosión'),
)

OPCIONES_CARACTERISTICA_SURCO = (
	('---', '---'),
	('(24.1.3.1) Base redonda','(24.1.3.1) Base redonda'),
	('(23.2, 23.2.1, 23.2.2, 23.2.3, 23.2.4) Información de abrasión','(23.2, 23.2.1, 23.2.2, 23.2.3, 23.2.4) Información de abrasión'),
	('(24.1.3.2) Base aguda','(24.1.3.2) Base aguda'),
	('(23.1.1, 23.1.1.1, 23.1.1.2) Información de percusión','(23.1.1, 23.1.1.1, 23.1.1.2) Información de percusión'),
)

OPCIONES_PIEDRA_EROSION = (
	('---', '---'),
	('Tipo de línea sencilla','Tipo de línea sencilla'),
	('Tipo de línea compuesta','Tipo de línea compuesta'),
	('Color base','Color base'),
)

OPCIONES_MANIFESTACIONES_ASOCIADAS = (
	('---','---'),
	('(30.1) Lítica','(30.1) Lítica'),
	('(30.2) Cerámica','(30.2) Cerámica'),
	('(30.3) Oseo','(30.3) Oseo'),
	('(30.4) Concha','(30.4) Concha'),
	('(30.5) Carbón no superficial','(30.5) Carbón no superficial'),
	('(30.6) Mitos','(30.6) Mitos'),
	('(30.7) Cementerios','(30.7) Cementerios'),
	('(30.8) Montículos','(30.8) Montículos'),
	('(30.9) Otros','(30.9) Otros'),
)
 

class CrucesYYFormAdmin(forms.Form):
    codigo 	= forms.CharField(required=False, max_length=20)
    estado = forms.ChoiceField(required=False, choices=OPCIONES_ESTADO)
    ubicacion = forms.ChoiceField(required=False, choices=OPCIONES_UBICACION)
    carasurcopetrotipo = forms.ChoiceField(required=False, choices=OPCIONES_SURCO_GRABADO)
    carasurcopetrotipo2 = forms.ChoiceField(required=False, choices=OPCIONES_SURCO_GRABADO2)
    carasurcopetrotipo3 = forms.ChoiceField(required=False, choices=OPCIONES_SURCO_GRABADO3)
    tipoPintura = forms.ChoiceField(required=False, choices=OPCIONES_TIPO_PINTURA)
    caracteristicaSurco = forms.ChoiceField(required=False, choices=OPCIONES_CARACTERISTICA_SURCO)
    piedraErosion = forms.ChoiceField(required=False, choices=OPCIONES_PIEDRA_EROSION)
    material = forms.ChoiceField(required=False, choices=OPCIONES_MATERIAL)
    manifasociadas = forms.ChoiceField(required=False,widget=forms.Select,choices=OPCIONES_MANIFESTACIONES)
    estado.widget.attrs 	= {'class':'chzn-select', 'data-placeholder':'Seleccione el estado'}
    manifAsociadas = forms.ChoiceField(required=False,choices=OPCIONES_MANIFESTACIONES_ASOCIADAS)

class CrucesYYForm(forms.Form):
	nombre 	= forms.CharField(required=False, max_length=100)
	estado = forms.ChoiceField(required=False,widget=forms.Select, choices=OPCIONES_ESTADO)
	manifestacion = forms.ChoiceField(required=False,widget=forms.Select,choices=OPCIONES_MANIFESTACIONES)
	nombre.widget.attrs    =  {'class':'special','placeholder':'Introduzca el nombre'}
	estado.widget.attrs 	= {'class':'chzn-select', 'placeholder':'Seleccione el estado'}
