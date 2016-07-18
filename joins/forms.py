# -*- coding: utf-8 -*-

from django import forms

########################################################################################
# Creando Cruces Yacimiento-Yacimiento Form
########################################################################################

OPCIONES_ESTADO = (
	('Todos', 'Todos'),
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
	('Cerro','Cerro'),
	('Cima','Cima'),
	('Ladera','Ladera'),
	('Fila','Fila'),
	('Pie de montaña','Pie de montaña'),
	('Barranco','Barranco'),
	('Acantilado','Acantilado'),
	('Valle','Valle'),
	('Río','Río'),
	('Lecho','Lecho'),
	('Margen derecha','Margen derecha'),
	('Margen izquierda','Margen izquierda'),
	('Isla','Isla'),
	('Raudal','Raudal'),
	('Costa','Costa'),
	('En el mar','En el mar'),
)

OPCIONES_UBICACION2 = (
	('Abrigo','Abrigo'),
	('Cueva','Cueva'),
	('Cueva de recubrimiento','Cueva de recubrimiento'),
)

CLASIFICACION = (
	('Linea sencilla','Linea sencilla'),
	('Linea compuesta','Linea compuesta'),
	('Figura rellena','Figura rellena'),
	('Figura rellena','Figura rellena'),
	('Impresion de manos positivo','Impresion de manos positivo'),
	('Impresion de manos negativo','Impresion de manos negativo'),
)

OPCIONES_SURCO_GRABADO = (
	('---', '---'),
	('Bajo relieve lineal','Bajo relieve lineal'),
	('Bajo relieve planar','Bajo relieve planar'),
	('Bajo relieve planar y lineal','Bajo relieve planar y lineal'),
	('Alto relieve lineal ','Alto relieve lineal'),
	('Alto relieve planar','Alto relieve planar'),
)

OPCIONES_SURCO_GRABADO2 = (
	('---', '---'),
	('Areas interlineales pulidas','Areas interlineales pulidas'),
	('Areas interlineales rebajadas','Areas interlineales rebajadas'),
	('Grabados superpuestos','Grabados superpuestos'),
	('Grabados rebajados','Grabados rebajados'),
)

OPCIONES_SURCO_GRABADO3 = (
	('Ancho de surco','Ancho de surco'),
	('Profundidad de surco','Profundidad de surco'),
	('Base redonda','Base redonda'),
	('Base aguda','Base aguda'),
	('Bajo relieve lineal','Bajo relieve lineal'),
	('Bajo relieve planar','Bajo relieve planar'),
	('Alto relieve lineal','Alto relieve lineal'),
	('Alto relieve planar','Alto relieve planar'),
)

OPCIONES_TIPO_PINTURA = (

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

	('Roca ignea','Roca ignea'),
	('Roca metamorfica','Roca metamorfica'),
	('Roca sedimentaria','Roca sedimentaria'),
)

OPCIONES_CARACTERISTICA_SURCO = (
	('Base redonda','Base redonda'),
	('Base aguda','Base aguda'),
)

OPCIONES_PIEDRA_EROSION = (
	('Tipo de línea sencilla','Tipo de línea sencilla'),
	('Tipo de línea compuesta','Tipo de línea compuesta'),
	('Color base','Color base'),
)

OPCIONES_MANIFESTACIONES_ASOCIADAS = (
	('Litica','Litica'),
	('Ceramica','Ceramica'),
	('Oseo','Oseo'),
	('Concha','Concha'),
	('Carbon no superficial','Carbon no superficial'),
	('Mitos','Mitos'),
	('Cementerios','Cementerios'),
	('Monticulos','Monticulos'),
	('Otros','Otros'),
)

SURCO = (
	('Abrasion','Abrasion'),
	('Percusion','Percusion'),
)

ESTADO_CONSERVACION = (
	('Bueno','Bueno'),
	('Modificado','Modificado'),
)

CARATERISTICA_PINTURA = (
	('Linea sencilla','Linea sencilla'),
	('Linea compuesta','Linea compuesta'),
	('Pintura positiva','Pintura positiva'),
	('Pintura negativa','Pintura negativa'),
)

CARATERISTICA_PINTURA2 = (
	('Linea sencilla','Linea sencilla'),
	('Linea compuesta','Linea compuesta'),
)

SURCO_GRABADO = (

	('Base redonda','Base redonda'),
	('Base aguda','Base aguda'),
	('Bajo relieve lineal','Bajo relieve lineal'),
	('Bajo relieve planar','Bajo relieve planar'),
	('Alto relieve lineal','Alto relieve lineal'),
	('Alto relieve planar','Alto relieve planar'),
)
 
class CrucesYYFormAdmin(forms.Form):
    codigo 	= forms.CharField(required=False, max_length=20)
    anchoDesde = forms.CharField(required=False, max_length=20)
    anchoHasta = forms.CharField(required=False, max_length=20)
    profundidadDesde = forms.CharField(required=False, max_length=20)
    profundidadHasta = forms.CharField(required=False, max_length=20)
    estado = forms.ChoiceField(required=False, choices=OPCIONES_ESTADO)
    estadoConservacion = forms.ChoiceField(required=False, choices=ESTADO_CONSERVACION)
    ubicacion = forms.ChoiceField(required=False, choices=OPCIONES_UBICACION)
    ubicacion2 = forms.ChoiceField(required=False, choices=OPCIONES_UBICACION2)
    surco = forms.ChoiceField(required=False, choices=SURCO)
    surcoGrabado = forms.ChoiceField(required=False, choices=SURCO_GRABADO)
    clasificacion = forms.ChoiceField(required=False, choices=CLASIFICACION)
    caracteristicaPintura = forms.ChoiceField(required=False, choices=CARATERISTICA_PINTURA)
    caracteristicaPintura2 = forms.ChoiceField(required=False, choices=CARATERISTICA_PINTURA2)
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
