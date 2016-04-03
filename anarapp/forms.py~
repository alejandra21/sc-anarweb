# -*- coding: utf-8 -*-

from django import forms
from haystack.forms import SearchForm
import anarapp.models
import dynamic

from django.forms import ModelForm
from suit.widgets import LinkedSelect, AutosizedTextarea, TextInput, Select



class BaseForm(SearchForm):
    # Busqueda
    def search(self):
        sqs = super(BaseForm, self).search()
        print sqs


        if not self.is_valid():
        	return self.no_query_found()

        filters = {}
        for field, value in self.cleaned_data.items():
            if self.cleaned_data[field]:
                if isinstance(value, list):
                    filters[field + '__in'] = value	
                else:
                    filters[field] = value

        return sqs.filter(**filters)


def crear_form(classes, name):
	""" Crea un FORM con todos los atributos de las clases dadas """

	attrs 	= {}
	
	for fclass in classes:
		mclass = getattr(anarapp.models, fclass)

		if dynamic.get_type(mclass, 'yacimiento') == 'ForeignKey' or dynamic.has_attr(mclass, 'piedra'):
			foreign.append(mclass.abbr)
		
		for fname, ftype, flabel in dynamic.get_attrs_wlabel(mclass):
			if ftype == 'CharField':
				attrs[fname] = forms.CharField(required=False, max_length=100, label=flabel)
			elif ftype == 'IntegerField':
				attrs[fname] = forms.IntegerField(required=False, label=flabel)
			elif ftype == 'BooleanField':
				attrs[fname] = forms.BooleanField(required=False, label=flabel)			
			elif ftype == 'DateField':
				attrs[fname] = forms.DateField(required=False, label=flabel)
	attrs['valor'] = forms.CharField(required=False, max_length=100)

	return type(name, (BaseForm,), attrs)

########################################################################################
# Creando Basic Form
########################################################################################

OPCIONES_MANIFESTACION = (
    (1,        'Geoglifo'),
    (2,        'Pintura Rupestre'),
    (3,        'Petroglifo'),
    (4,        'Petroglifo Pintado'),
    (5,        'Micro-Petroglifo'),
    (6,        'Piedra Mítica Natural'),
    (7,        'Cerro Mítico Natural'),
    (8,        'Cerro Mitico Natural con Petroglifo'),
    (9,        'Cerro Mitico Natural Con Pintura'),
    (10,'Cerro Mitico Natural Con Dolmen'),
    (11,'Monumentos Megalíticos'),
    (12,'Monolitos'),
    (13,'Monolitos Con Grabados'),
    (14,'Menhires'),
    (15,'Menhires Con Puntos Acoplados'),
    (16,'Menhires Con Petroglifo'),
    (17,'Menhires Con Pintura'),
    (18,'Amolador'),
    (19,'Batea'),
    (20,'Puntos Acoplados'),
    (21,'Cupulas'),
    (22,'Mortero o Metate'),
)  

class BasicForm(BaseForm):
        manifestacion         = forms.MultipleChoiceField(required=False, choices=OPCIONES_MANIFESTACION)
        
        # Seleccion Multiple
        manifestacion.widget.attrs         = {'class':'chzn-select', 'data-placeholder':'Seleccione el tipo de manifestación'}


########################################################################################
# Creando Advanced Form
########################################################################################


OPCIONES_ESTADO = (
        ('Amazonas'        , 'Amazonas'),
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

OPCIONES_TIPO = (
        (1, 'Pared Rocosa'),
    (2, 'Roca'),
    (3, 'Dolmen(natural)'),
    (4, 'Abrigo'),
    (5, 'Cueva'),
    (6, 'Cueva de Recubrimiento'),
    (7, 'Terreno Superficial'),
    (8, 'Terreno Profundo'),
)

OPCIONES_EXPOSICION = (
        (1, 'Expuesto'),
    (2, 'No Expuesto'),
    (3, 'Expuesto Periodicamente'),
)

OPCIONES_UBICACION = (
    (1, 'Cerro'),
    (2, 'Valle'),
    (3, 'Río'),
    (4, 'Costa'),
)

OPCIONES_MATERIAL = (
         (1, 'Roca'),
    (2, 'Tierra'),
    (3, 'Hueso'),
    (4, 'Corteza de árbol'),
    (5, 'Pieles'),
)

OPCIONES_CONSERVACION = (
        (1, 'Bueno'),
        (2, 'Modificado'),
)

OPCIONES_MANIF_ASOCIADAS = (
        (1, 'Lítica'),
        (2, 'Cerámica'),
        (3, 'Oseo'),
        (4, 'Concha'),
        (5, 'Carbón No Superficial'),
        (6, 'Mitos'),
        (7, 'Cementerios'),
        (8, 'Montículos'),

)



class AdvancedForm(BasicForm):

        codigo                             = forms.CharField(required=False, max_length=20)
        municipio                 = forms.CharField(required=False, max_length=150)
        estado                         = forms.MultipleChoiceField(required=False, choices=OPCIONES_ESTADO)
        nombre                         = forms.CharField(required=False, max_length=100)
        localidad                     = forms.CharField(required=False, max_length=150)
        fotografia                 = forms.BooleanField(required=False)
        tipo                                 = forms.MultipleChoiceField(required=False, choices=OPCIONES_TIPO)
        exposicion                 = forms.MultipleChoiceField(required=False, choices=OPCIONES_EXPOSICION)
        
        ubicacion                 = forms.MultipleChoiceField(required=False, choices=OPCIONES_UBICACION)
        material                     = forms.MultipleChoiceField(required=False, choices=OPCIONES_MATERIAL)
        conservacion         = forms.MultipleChoiceField(required=False, choices=OPCIONES_CONSERVACION)
        
        manifasociadas         = forms.MultipleChoiceField(required=False, choices=OPCIONES_MANIF_ASOCIADAS)
        
        #Seleccion multiple
        estado.widget.attrs                          = {'class':'chzn-select', 'data-placeholder':'Seleccione el estado'}
        tipo.widget.attrs                                  = {'class':'chzn-select', 'data-placeholder':'Seleccione el tipo de yacimiento'}
        exposicion.widget.attrs             = {'class':'chzn-select', 'data-placeholder':'Seleccione el tipo de exposición'}
        ubicacion.widget.attrs                     = {'class':'chzn-select', 'data-placeholder':'Seleccione la ubicación'}
        material.widget.attrs                      = {'class':'chzn-select', 'data-placeholder':'Seleccione el tipo de material'}
        conservacion.widget.attrs         = {'class':'chzn-select', 'data-placeholder':'Seleccione el estado de conservación'}
        manifasociadas.widget.attrs = {'class':'chzn-select', 'data-placeholder':'Seleccione las manifetaciones asociadas'}



class PiedraForm(BaseForm):
    yacimiento      = forms.CharField(required=False, max_length=20)
    codigo                             = forms.CharField(required=False, max_length=20)
    nombre                     = forms.CharField(required=False, max_length=150)
    estado                         = forms.MultipleChoiceField(required=False, choices=OPCIONES_ESTADO)
    figuras                             = forms.CharField(required=False, max_length=100)
    otros                         = forms.CharField(required=False, max_length=150)    

    estado.widget.attrs                          = {'class':'chzn-select', 'data-placeholder':'Seleccione el estado'}

class YacimientoForm(forms.ModelForm):
        pass












"""

# Opciones de Select    


OPCIONES_UBI_MANIFEST = (
    (1,'Cerro'),
    (2,'Cerro - Cima'),
    (3,'Cerro - Ladera'),
    (4,'Cerro - Fila'),
    (5,'Cerro - Pie de Monte'),
    (6,'Cerro - Barranco'),
    (7,'Cerro - Acantilado'),
    (8,'Valle'),
    (9,'Río'),
    (10,'Río - Lecho'),
    (11,'Río - Margen Derecha'),
    (12,'Río - Margen Izquierda'),
    (13,'Río - Isla'),
    (14,'Río - Raudal'),
    (15,'Costa'),
   
)

OPCIONES_ESTADO = (
	('Amazonas','Amazonas'),
	('Anzoategui','Anzoategui'),
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

OPCIONES_ORIENTACION = (
	(1, 'Cerro'),
	(2, 'Valle'),
	(3, 'Río'),
	(4, 'Costa'),
	(5, 'Cielo'),
)

OPCIONES_SUELO = (
	(1, 'Forestal'),
	(2, 'Ganadero'),
	(3, 'Agricultura de Riego'),
	(4, 'Urbano'),
	(5, 'Turístico'),
)

OPCIONES_LOCALIDAD = (
	(1, 'Centro de Poblado'),
	(2, 'Urbano'),
	(3, 'Rural'),
	(4, 'Indigena'),
	(5, 'No Poblado'),
)

OPCIONES_TIPO_YACIMIENTO = (
	(1, 'Pared Rocosa'),
    (2, 'Roca'),
    (3, 'Dolmen(natural)'),
    (4, 'Abrigo'),
    (5, 'Cueva'),
    (6, 'Cueva de Recubrimiento'),
    (7, 'Terreno Superficial'),
    (8, 'Terreno Profundo'),
)

OPCIONES_HIDROLOGIA = (
	(1, 'Rio'),
    (2, 'Laguna'),
    (3, 'Arroyo'),
    (4, 'Arroyo Perenne'),
    (5, 'Manantial'),
    (6, 'Manantial Intermitente'),
)

OPCIONES_EXPOSICION = (
	(1, 'Expuesto'),
    (2, 'No Expuesto'),
    (3, 'Expuesto Periodicamente'),
)

OPCIONES_FOTOGRAFIAS = (
	(1, 'Aerea'),
    (2, 'No Aerea'),
    (3, 'Satelital'),
)

OPCIONES_MATERIAL = (
 	(1, 'Roca'),
    (2, 'Roca Ignea'),
    (3, 'Roca Metamórfica'),
    (4, 'Roca Sedimentaria'),
    (5, 'Tierra'),
    (6, 'Hueso'),
    (7, 'Corteza de árbol'),
    (8, 'Pieles'),
)

OPCIONES_ORIENTACION = (
	(1, 'Hacia Cerro'),
	(2, 'Hacia Valle'),
	(3, 'Hacia Rio'),
	(4, 'Hacia Costa'),
	(5, 'Hacia Cielo'),
)

OPCIONES_TEC_PINTURA = (
	(1, 'Dedo'),
	(2, 'Fibra'),
	(3, 'Soplado'),
)

OPCIONES_TEC_PETROGLIFO = (
	(1, 'Grabado'),
	(2, 'Grabado Percusión'),
	(3, 'Grabado Percusión Directa'),
	(4, 'Grabado Percusión Indirecta'),
	(5, 'Abrasión'),
	(6, 'Abrasión Piedra'),
	(7, 'Abrasión Arena'),
	(8, 'Concha'),
)

OPCIONES_MONUMENTO = (
	(1, 'Monolitos'),
	(2, 'Menhires'),
	(3, 'Dolmen (artificial)'),
)   

OPCIONES_MANIF_ASOCIADAS = (
	(1, 'Lítica'),
	(2, 'Cerámica'),
	(3, 'Oseo'),
	(4, 'Concha'),
	(5, 'Carbón No Superficial'),
	(6, 'Mitos'),
	(7, 'Cementerios'),
	(8, 'Montículos'),
)

OPCIONES_SURCO_PETROGLIFO = (
	(1, 'Base'),
	(2, 'Base Redonda'),
	(3, 'Base Aguda'),
	(4, 'Bajo Relieve'),
	(5, 'Lineal'),
	(6, 'Planar'),
	(7, 'Alto Relieve'),
	(8, 'Lineal'),
	(9, 'Planar'),
	(10, 'Áreas Interlineales'),
	(11, 'Pulidas'),
	(12, 'Rebajadas'),
	(13, 'Superpuestos'),
	(14, 'Rebajados'),
)

OPCIONES_CARACT_PINTURA = (
	(1, 'Pintura Rupestre'),
	(2, 'Técnica Dactilar'),
	(3, 'Técnica Fibra'),
	(4, 'Línea Sencilla'),
	(5, 'Línea Compuesta'),
	(6, 'Impresión de Manos'),
	(7, 'Impresión de Manos Positivo'),
	(8, 'Impresión de Manos Negativo'),
	(9, 'Figuras Superpuestas'),
)

OPCIONES_CARACT_MONOLITOS = (
	(1, 'Con Grabados'),
)

OPCIONES_CARACT_MENHIRES = (
	(1, 'Con Piedras Verticales'),
	(2, 'Con Puntos Acoplados'),
	(3, 'Con Petroglifo'),
	(4, 'Con Pinturas'),
)

OPCIONES_CARACT_DOLMEN = (
	(1, 'Con Petroglifo'),
	(2, 'Con Pinturas'),
)

OPCIONES_EST_CONSERVACION = (
	(1, 'Bueno'),
	(2, 'Modificado'),
	(3, 'Trasladado'),
	(4, 'Sumergido'),
	(5, 'Enterrado'),
	(6, 'Perdido'),
	(7, 'Destruido'),
	(8, 'Crecimiento Vegetal'),
	(9, 'Pátina'),
	(10, 'Erosión'),
)

OPCIONES_GRADO_DESTRUCCION = (
   #(11, 'Grado de Destrucción del Sitio')),
	(12, 'Natural'),
	(13, 'Natural Ligera'),
	(14, 'Natural Aguda'),
	(15, 'Humana'),
	(16, 'Humana Ligera'),
	(17, 'Humana Aguda'),
)
OPCIONES_CAUSA_DESTRUCCION = (
   #(18, 'Destrucción Potencial del Sitio'),
	(19, 'Asentamiento Humano'),
	(20, 'Obra Infraestrucrura a Corto Plazo'),
	(21, 'Obra Infraestrucrura a Mediano Plazo'),
	(22, 'Obra Infraestrucrura a Largo Plazo'),
	(23, 'Nivelación del Terreno Como Obra Agrícola'),
	(24, 'Extracción Como Actividad Familiar'),
	(25, 'Extracción Como Actividad Mayor'),
	(26, 'Vandalismo'),
	(27, 'Erosión'),
	(28, 'Erosión Parcial Moderada'),
	(29, 'Erosión Parcial Severa'),
	(30, 'Erosión Extensiva Moderada'),
	(31, 'Erosión Extensiva Severa'),
)

class BasicForm(SearchForm):
	#Yacimiento
	nombre 		= forms.CharField(required=False, max_length=100)				#1
	municipio 	= forms.CharField(required=False, max_length=150)    			#2
	estado 		= forms.MultipleChoiceField(required=False, choices=OPCIONES_ESTADO)	#3

	#Foraneos
	hayFotografia 	= forms.BooleanField(required=False)
	manifestacion 	= forms.MultipleChoiceField(required=False, choices=OPCIONES_TIPO_MANIFEST)	#13
	orientacion 	= forms.MultipleChoiceField(required=False, choices=OPCIONES_ORIENTACION)	#15	
	
	#Seleccion multiple
	manifestacion.widget.attrs 	= {'class':'chzn-select', 'data-placeholder':'Seleccione el tipo de manifestación'}
	orientacion.widget.attrs 	= {'class':'chzn-select', 'data-placeholder':'Seleccione la orientación'}
	estado.widget.attrs 	 	= {'class':'chzn-select', 'data-placeholder':'Seleccione el estado'}
	
	# Busqueda
	def search(self):
		for item in models.__subclasses__():
			print item.__name__
	
		sqs = super(BasicForm, self).search()

		if not self.is_valid():
			return self.no_query_found()

		filters = {}
		for field, value in self.cleaned_data.items():
			if self.cleaned_data[field]:
				if isinstance(value, list):
					filters[field + '__in'] = value
				else:
					filters[field] = value

		return sqs.filter(**filters)

class YacimientoForm(BasicForm):
	#Codigo
	codigo 		= forms.CharField(required=False, max_length=20) #00
	
	#Datos generales del Yacimiento
	localidad  		= forms.MultipleChoiceField(required=False, choices=OPCIONES_LOCALIDAD)				#4
	nombreLocalidad = forms.CharField(required=False, max_length=150)
	
	fotografia	 	= forms.MultipleChoiceField(required=False, choices=OPCIONES_FOTOGRAFIAS)			#11
	fechaFotografia = forms.DateField(required=False, input_formats=['%d-%m-%Y','%d/%m/%Y'])
	
	suelo			= forms.MultipleChoiceField(required=False, choices=OPCIONES_SUELO)					#5
	tipo			= forms.MultipleChoiceField(required=False, choices=OPCIONES_TIPO_YACIMIENTO)		#12
	hidrologia		= forms.MultipleChoiceField(required=False, choices=OPCIONES_HIDROLOGIA)			#19
	exposicion		= forms.MultipleChoiceField(required=False, choices=OPCIONES_EXPOSICION)			#20
	
	nroPiedras 			= forms.IntegerField(required=False)											#21
	nroPiedrasGrabadas 	= forms.IntegerField(required=False)
	nroPiedrasPintadas 	= forms.IntegerField(required=False)
	nroPiedrasColocadas = forms.IntegerField(required=False)
	
	#La Manifestacion
	ubicacion 	= forms.MultipleChoiceField(required=False, choices=OPCIONES_UBI_MANIFEST) 				#14
	material	= forms.MultipleChoiceField(required=False, choices=OPCIONES_MATERIAL)					#22	

	#Tecnicas
	tecnicaGeoglifo  	= forms.CharField(required=False, max_length=400)								#23
	tecnicaPintura  	= forms.MultipleChoiceField(required=False, choices=OPCIONES_TEC_PINTURA)
	tecnicaPetroglifo  	= forms.MultipleChoiceField(required=False, choices=OPCIONES_TEC_PETROGLIFO)
	tecnicaMicroPetro  	= forms.MultipleChoiceField(required=False, choices=OPCIONES_TEC_PETROGLIFO)
	tipoMonumento  		= forms.MultipleChoiceField(required=False, choices=OPCIONES_MONUMENTO)
	tecnicaMonumento	= forms.CharField(required=False, max_length=400)

	surcoPetroglifo		= forms.MultipleChoiceField(required=False, choices=OPCIONES_SURCO_PETROGLIFO) 	#24
	caractPintura		= forms.MultipleChoiceField(required=False, choices=OPCIONES_CARACT_PINTURA) 	#25
	caractMonolitos		= forms.MultipleChoiceField(required=False, choices=OPCIONES_CARACT_MONOLITOS) 	#26
	caractMenhires		= forms.MultipleChoiceField(required=False, choices=OPCIONES_CARACT_MENHIRES) 	
	caractDolmen		= forms.MultipleChoiceField(required=False, choices=OPCIONES_CARACT_DOLMEN) 	

	#Conservacion
	estadoConservacion	= forms.MultipleChoiceField(required=False, choices=OPCIONES_EST_CONSERVACION)	#27
	gradoDestruccion	= forms.MultipleChoiceField(required=False, choices=OPCIONES_GRADO_DESTRUCCION)
	causasDestruccion	= forms.MultipleChoiceField(required=False, choices=OPCIONES_CAUSA_DESTRUCCION)  
	
	patinaConsider		= forms.BooleanField(required=False)											#28
	otrosConsider		= forms.CharField(required=False, max_length=400)

	#Manifestaciones Asociadas
	manifestAsociadas	= forms.MultipleChoiceField(required=False, choices=OPCIONES_MANIF_ASOCIADAS)	#30
	otrosValores		= forms.CharField(required=False, max_length=150)								#33
	
	#Observaciones
	observaciones		= forms.CharField(required=False, max_length=150)								#34



	# Seleccion multiple
	localidad.widget.attrs 	 = {'class':'chzn-select', 'data-placeholder':'Seleccione el tipo de localidad'}
	suelo.widget.attrs 		 = {'class':'chzn-select', 'data-placeholder':'Seleccione el tipo de suelo'}
	fotografia.widget.attrs  = {'class':'chzn-select', 'data-placeholder':'Seleccione el tipo de fotografía'}
	tipo.widget.attrs 		 = {'class':'chzn-select', 'data-placeholder':'Seleccione el tipo de yacimiento'}
	hidrologia.widget.attrs  = {'class':'chzn-select', 'data-placeholder':'Seleccione el tipo de hidrologia'}
	exposicion.widget.attrs  = {'class':'chzn-select', 'data-placeholder':'Seleccione el tipo de exposición'}
	ubicacion.widget.attrs 	 = {'class':'chzn-select', 'data-placeholder':'Seleccione la ubicación'}	
	material.widget.attrs 	 = {'class':'chzn-select', 'data-placeholder':'Seleccione el tipo de material'}
	
	tecnicaPintura.widget.attrs 	= {'class':'chzn-select', 'data-placeholder':'Seleccione las técnicas de pintura'}
	tecnicaPetroglifo.widget.attrs 	= {'class':'chzn-select', 'data-placeholder':'Seleccione las técnicas de petroglifo'}
	tecnicaMicroPetro.widget.attrs 	= {'class':'chzn-select', 'data-placeholder':'Seleccione las técnicas de micro petroglifo'}
	tipoMonumento.widget.attrs 	 	= {'class':'chzn-select', 'data-placeholder':'Seleccione el tipo de monumento'}
	surcoPetroglifo.widget.attrs 	= {'class':'chzn-select', 'data-placeholder':'Seleccione características del surco'}
	caractPintura.widget.attrs 		= {'class':'chzn-select', 'data-placeholder':'Seleccione características de la pintura'}
	caractMonolitos.widget.attrs 	= {'class':'chzn-select', 'data-placeholder':'Seleccione características de monolito'}	
	caractMenhires.widget.attrs 	= {'class':'chzn-select', 'data-placeholder':'Seleccione características de menhir'}	
	caractDolmen.widget.attrs 		= {'class':'chzn-select', 'data-placeholder':'Seleccione características de dolmen'}
			
	estadoConservacion.widget.attrs = {'class':'chzn-select', 'data-placeholder':'Seleccione el estado de conservacion'}	
	gradoDestruccion.widget.attrs 	= {'class':'chzn-select', 'data-placeholder':'Seleccione el grado de destrucción'}	
	causasDestruccion.widget.attrs 	= {'class':'chzn-select', 'data-placeholder':'Seleccione las causas de destrucción'}
	manifestAsociadas.widget.attrs 	= {'class':'chzn-select', 'data-placeholder':'Seleccione el tipo de manifestación asociada'}



OPCIONES_ORIENT_CARAS = (
    (0, 'Tope'),
    (1, 'Norte'),
    (2, 'Noreste'),
    (3, 'Este'),
    (4, 'Sureste'),
    (5, 'Sur'),
    (6, 'Suroeste'),
    (7, 'Oeste'),
    (8, 'Noroeste'),
    (9, 'Piso o plano inclinado'),
)

OPCIONES_UBI_CARAS = (
	(1, 'Toda la caverna'),
	(2, 'Áreas específicas'),
	(3, 'Sala principal'),
	(4, 'Otra sala'),
	(5, 'Lago interior'),
	(6, 'Claraboya'),
)

OPCIONES_LUMINOSIDAD = (
    (0, 'No tiene'),
    (1, 'Fótico'),
    (2, 'Escótico'),
)

OPCIONES_TIPO_FIGURA = (
    (1, 'Antropomorfas'),
    (2, 'Zoomorfas'),
    (3, 'Geométricas'),
    (4, 'Puntos Acoplados'),
    (5, 'Cupulas'),
    (6, 'Zoo-antropomorfas'),
    (7, 'Antropo-geométricas'),
    (8, 'Zoo-geométricas'),
    (9, 'Amoladores'),
    (10, 'Bateas'),
)

OPCIONES_CONEX_FIGURA = (
    (1, 'Presencia de una sola figura'),
    (2, 'Menos del 10% interconectadas'),
    (3, '50% interconectadas'),
    (4, 'Mas del 80% interconectadas'),
)


class AdvancedForm(YacimientoForm):
	#Codigo
	codigoPiedra  = forms.CharField(required=False, max_length=20) 								#Pa00
	
	#Datos Generales de la Piedra
	estadoPiedra  = forms.CharField(required=False, max_length=40) 								#Pa3
	nombrePiedra  = forms.CharField(required=False, max_length=150) 							#Pa1
	nombreFiguras = forms.CharField(required=False, max_length=150) 							#Pa2
	numeroCaras	  = forms.IntegerField(required=False)											#Pa4
	numeroCarasTrabajadas = forms.IntegerField(required=False)									#Pa5
	
	orientacionCaras = forms.MultipleChoiceField(required=False, choices=OPCIONES_ORIENT_CARAS) #Pa6
	altoMaximo		 = forms.IntegerField(required=False)										#Pa7
	largoMaximo		 = forms.IntegerField(required=False)
	anchoMaximo		 = forms.IntegerField(required=False)
	
	ubicacionCaras	 = forms.MultipleChoiceField(required=False, choices=OPCIONES_UBI_CARAS)	#Pa8
	luminosidad		 = forms.MultipleChoiceField(required=False, choices=OPCIONES_LUMINOSIDAD)
	altura			 = forms.IntegerField(required=False)
	andamiaje		 = forms.BooleanField(required=False)
	
	#Las Figuras
	tipoFigura		= forms.MultipleChoiceField(required=False, choices=OPCIONES_TIPO_FIGURA)	#Pa9
	conexionFiguras = forms.MultipleChoiceField(required=False, choices=OPCIONES_CONEX_FIGURA)	#Pa11
	
	#Tratamiento de la Roca
	limpiezaCon 		= forms.CharField(required=False, max_length=40)						#Pa12
	rellenoSurcos 		= forms.CharField(required=False, max_length=40)
	tratamientoDigital	= forms.CharField(required=False, max_length=40)
	programaVersion		= forms.CharField(required=False, max_length=40)
	otrosTratamientos	= forms.CharField(required=False, max_length=150)
	
	#Manifestaciones Asociadas
	manifAsociadaPiedra	= forms.CharField(required=False, max_length=150)						#Pa1.1
	otrosValoresPiedra	= forms.CharField(required=False, max_length=150)						#Pa15
	
	#Observaciones
	observacionesPiedra = forms.CharField(required=False, max_length=150)						#Pa16
	
	# Seleccion multiple
	orientacionCaras.widget.attrs 	= {'class':'chzn-select', 'data-placeholder':'Seleccione la orientación'}
	ubicacionCaras.widget.attrs 	= {'class':'chzn-select', 'data-placeholder':'Seleccione la ubicación'}
	luminosidad.widget.attrs 	 	= {'class':'chzn-select', 'data-placeholder':'Seleccione el tipo de luminosidad'}
	tipoFigura.widget.attrs 	 	= {'class':'chzn-select', 'data-placeholder':'Seleccione el tipo de figura'}	
	conexionFiguras.widget.attrs 	= {'class':'chzn-select', 'data-placeholder':'Seleccione el tipo de conexión'}	
"""	

shortTextField = {'class': 'input-small', 'style': 'width:75%'}
regularTextField = {'class': 'input-medium', 'style': 'width:75%'}
fullTextField = {'class': 'input-medium', 'style': 'width:95%'}
regularTextArea = {'rows': 4, 'style': 'width:75%'}
regularSelect = {'class': 'input-medium'}


### Formularios utilizados por el backend para yacimiento
class YacimientoForm(ModelForm) :

    class Meta:
        widgets = {
                'codigo': TextInput(attrs=regularTextField),
		'nombre': TextInput(attrs=regularTextField),
		'pais': TextInput(attrs=regularTextField),
        }

class LocalidadYacimientoForm(ModelForm) :
    class Meta:
        widgets = {
                'nombrePoblado': TextInput(attrs=regularTextField),
		'nombreNoPoblado': TextInput(attrs=regularTextField),
        }	

class TenenciaDeTierraForm(ModelForm) :
    class Meta:
        widgets = {
                'esTenenciaOtros': TextInput(attrs=regularTextField),
        }

class IndicacionesForm(ModelForm) :
    class Meta:
        widgets = {
                'direcciones': AutosizedTextarea(attrs=regularTextArea),
                'puntoDatum': AutosizedTextarea(attrs=regularTextArea),
        }
            
class PlanoForm(ModelForm) :
    class Meta:
        widgets = {
                'numeroPlano': TextInput(attrs=regularTextField),
        }
        
class CoordenadasForm(ModelForm) :
    class Meta:
        widgets = {
                'longitud': TextInput(attrs=fullTextField),
                'latitud': TextInput(attrs=fullTextField),
                'utmAdicional': TextInput(attrs=fullTextField),
        }

class AltitudForm(ModelForm) :
    class Meta:
        widgets = {
                'texto': TextInput(attrs=regularTextField),
		'altura': TextInput(attrs=regularTextField),
		'superficie': TextInput(attrs=regularTextField),
		'desarrollo': TextInput(attrs=regularTextField),
		'desnivel': TextInput(attrs=regularTextField),
        }        

class TexturaSueloForm(ModelForm) :
    class Meta:
        widgets = {
                'mixto': TextInput(attrs=regularTextField),            
        }

class FloraYacimientoForm(ModelForm) :
    class Meta:
        widgets = {
                'flora': AutosizedTextarea(attrs=regularTextArea),
        }

class FaunaYacimientoForm(ModelForm) :
    class Meta:
        widgets = {
                'fauna': AutosizedTextarea(attrs=regularTextArea),
        }

class HidrologiaYacimientoForm(ModelForm) :
    class Meta:
        widgets = {
                'otros': TextInput(attrs=regularTextField),
		'nombre': TextInput(attrs=regularTextField),
		'distancia': TextInput(attrs=regularTextField),
		'observaciones': AutosizedTextarea(attrs=regularTextArea),
        }

class TipoExposicionYacForm(ModelForm) :
    class Meta:
        widgets = {
		'observaciones': AutosizedTextarea(attrs=regularTextArea),
        }

class ConstitucionYacimientoForm(ModelForm) :
    class Meta:
        widgets = {
                'nroPiedras': TextInput(attrs=regularTextField),
		'nroPiedrasGrabadas': TextInput(attrs=regularTextField),
		'nroPiedrasPintadas': TextInput(attrs=regularTextField),
                'nroPiedrasColocadas': TextInput(attrs=regularTextField),
		'otros': TextInput(attrs=regularTextField)
        }

class OrientacionYacimientoForm(ModelForm) :
    class Meta:
        widgets = {
                'otros': TextInput(attrs=regularTextField),
		'orientacion': TextInput(attrs=regularTextField),
        }

class MaterialYacimientoForm(ModelForm) :
    class Meta:
        widgets = {
                'tipo': TextInput(attrs=regularTextField),
		'otros': TextInput(attrs=regularTextField),
        }

class TecnicaParaGeoglifoForm(ModelForm) :
    class Meta:
        widgets = {
                'tecnicas': AutosizedTextarea(attrs=regularTextArea),
        }

class TecnicaParaPinturaForm(ModelForm) :
    class Meta:
        widgets = {
                'otros': AutosizedTextarea(attrs=regularTextArea),
        }
        
class TecnicaParaPetroglifoForm(ModelForm) :
    class Meta:
        widgets = {
                'otros': AutosizedTextarea(attrs=regularTextArea),
        }

class TecnicaParaMicroPetroForm(ModelForm) :
    class Meta:
        widgets = {
                'otros': AutosizedTextarea(attrs=regularTextArea),
        }
        
class TecnicaParaMonumentosForm(ModelForm) :
    class Meta:
        widgets = {
                'tecnicas': AutosizedTextarea(attrs=regularTextArea),
                'otros': AutosizedTextarea(attrs=regularTextArea),
        }

class CaracSurcoPetroglifoForm(ModelForm) :
    class Meta:
        widgets = {
                'anchoDe': TextInput(attrs=regularTextField),
                'anchoA': TextInput(attrs=regularTextField),
                'produndidadDe': TextInput(attrs=regularTextField),
                'profundidadA': TextInput(attrs=regularTextField),
        }
        
class CaracSurcoAmoladoresForm(ModelForm) :
    class Meta:
        widgets = {
                'largo': TextInput(attrs=regularTextField),
                'ancho': TextInput(attrs=regularTextField),
                'diametro': TextInput(attrs=regularTextField),                
        }

class CaracSurcoBateasForm(ModelForm) :
    class Meta:
        widgets = {
                'largo': TextInput(attrs=regularTextField),
                'ancho': TextInput(attrs=regularTextField),
                'diametro': TextInput(attrs=regularTextField),
                'profundidad': TextInput(attrs=regularTextField),                
        }

class CaracSurcoPuntosAcoplForm(ModelForm) :
    class Meta:
        widgets = {
                'diametro': TextInput(attrs=regularTextField),
                'profundidad': TextInput(attrs=regularTextField),
                'otros': AutosizedTextarea(attrs=regularTextArea),                
        }

class CaracSurcoCupulasForm(ModelForm) :
    class Meta:
        widgets = {
                'largo': TextInput(attrs=regularTextField),
                'ancho': TextInput(attrs=regularTextField),
                'diametro': TextInput(attrs=regularTextField),
                'profundidad': TextInput(attrs=regularTextField),
                'otros': AutosizedTextarea(attrs=regularTextArea),                
        }

class CaracSurcoMorteroForm(ModelForm) :
    class Meta:
        widgets = {
                'largo': TextInput(attrs=regularTextField),
                'ancho': TextInput(attrs=regularTextField),                
        }

class CaracDeLaPinturaForm(ModelForm) :
    class Meta:
        widgets = {
                'otros': AutosizedTextarea(attrs=regularTextArea),                
                'anchoDe': TextInput(attrs=regularTextField),
                'anchoA': TextInput(attrs=regularTextField),
                'anchoDeComp': TextInput(attrs=regularTextField),
                'anchoAComp': TextInput(attrs=regularTextField),
        }

class ColoresForm(ModelForm) :

    class Meta:
        widgets = {                
                'c':  TextInput(attrs=shortTextField),
                'm': TextInput(attrs=shortTextField),
                'y': TextInput(attrs=shortTextField),                    
                'k': TextInput(attrs=shortTextField),                    
        }
        		
		
class CaracMonolitosForm(ModelForm) :
    class Meta:
        widgets = {                
                'cantidad': TextInput(attrs=regularTextField),
                'cantidadConGrabados': TextInput(attrs=regularTextField),
        }

class CaracMenhiresForm(ModelForm) :
    class Meta:
        widgets = {                
                'cantidadPiedrasVerticales': TextInput(attrs=regularTextField),
                'cantidadConPuntosAcoplados': TextInput(attrs=regularTextField),
                'cantidadConPetroglifo': TextInput(attrs=regularTextField),
                'cantidadConPinturas': TextInput(attrs=regularTextField),
                'distanciamiento': TextInput(attrs=regularTextField),
        }

class CaracDolmenArtForm(ModelForm) :
    class Meta:
        widgets = {                
                'cantidadConPetroglifo': TextInput(attrs=regularTextField),
                'cantidadConPinturas': TextInput(attrs=regularTextField),                
        }
        
class NotasYacimientoForm(ModelForm) :
    class Meta:
        widgets = {                
                'notas': AutosizedTextarea(attrs=regularTextArea),                
        }

class EstadoConserYacForm(ModelForm) :
    class Meta:
        widgets = {                
                'trasladado': TextInput(attrs=regularTextField),
                'trasladadoPa': TextInput(attrs=regularTextField),
                'sumergido': TextInput(attrs=regularTextField),
                'sumergidoPa': TextInput(attrs=regularTextField),
                'enterrado': TextInput(attrs=regularTextField),
                'enterradoPa': TextInput(attrs=regularTextField),
                'perdido': TextInput(attrs=regularTextField),
                'perdidoPa': TextInput(attrs=regularTextField),
                'destruido': TextInput(attrs=regularTextField),
                'destruidoPa': TextInput(attrs=regularTextField),
                'crecimientoVeg': TextInput(attrs=regularTextField),
                'crecimientoVegPa': TextInput(attrs=regularTextField),
                'patina': TextInput(attrs=regularTextField),
                'patinaPa': TextInput(attrs=regularTextField),
                'erosion': TextInput(attrs=regularTextField),
                'erosionPa': TextInput(attrs=regularTextField),
                'especificar': AutosizedTextarea(attrs=regularTextArea),                
        }


class CausasDestruccionYacForm(ModelForm) :
    class Meta:
        widgets = {   
				'otros': AutosizedTextarea(attrs=regularTextArea),
        }		

class IntensidadDestruccionYacForm(ModelForm) :
    class Meta:
        widgets = {   
		        'observaciones': AutosizedTextarea(attrs=regularTextArea),
                'mas': TextInput(attrs=regularTextField),		
        }			
        
class ConsiderTempForm(ModelForm) :
    class Meta:
        widgets = {                
                'otros': AutosizedTextarea(attrs=regularTextArea),
        }

class CronologiaTentativaForm(ModelForm) :
    class Meta:
        widgets = {                
                'autor': TextInput(attrs=regularTextField),
                'fecha': TextInput(attrs=regularTextField),
                'institucion': TextInput(attrs=regularTextField),
                'pais': TextInput(attrs=regularTextField),
                'direccion': AutosizedTextarea(attrs=regularTextArea),
                'telefono': TextInput(attrs=regularTextField),
                'mail': TextInput(attrs=regularTextField),
                'tecnica':  AutosizedTextarea(attrs=regularTextArea),
                'bibliografia': AutosizedTextarea(attrs=regularTextArea),
                'twitter': TextInput(attrs=regularTextField),
                'facebook': TextInput(attrs=regularTextField),
        }


class ManifestacionesAsociadasForm(ModelForm) :
    class Meta:
        widgets = {                
                'descripcionLitica': AutosizedTextarea(attrs=regularTextArea),
                'descripcionCeramica': AutosizedTextarea(attrs=regularTextArea),
                'descripcionOseo': AutosizedTextarea(attrs=regularTextArea),
                'descripcionConcha': AutosizedTextarea(attrs=regularTextArea),
                'descripcionCarbon': AutosizedTextarea(attrs=regularTextArea),                
				'descripcionMito': AutosizedTextarea(attrs=regularTextArea),
                'descripcionCementerio': AutosizedTextarea(attrs=regularTextArea), 
                'descripcionMonticulo': AutosizedTextarea(attrs=regularTextArea),         
                'otros':  AutosizedTextarea(attrs=regularTextArea),
        }

class ManifestacionesLiticaForm(ModelForm) :
    class Meta:
        widgets = {                
				'descripcionLitica': AutosizedTextarea(attrs=regularTextArea),
        }

class ManifestacionesCeramicaForm(ModelForm) :
    class Meta:
        widgets = {                
                'descripcionCeramica': AutosizedTextarea(attrs=regularTextArea),        
        }

class ManifestacionesOseoForm(ModelForm) :
    class Meta:
        widgets = {                
                'descripcionOseo': AutosizedTextarea(attrs=regularTextArea),        
        }

class ManifestacionesConchaForm(ModelForm) :
    class Meta:
        widgets = {                
                'descripcionConcha': AutosizedTextarea(attrs=regularTextArea),        
        }

class ManifestacionesCarbonForm(ModelForm) :
    class Meta:
        widgets = {                
                'descripcionCarbon': AutosizedTextarea(attrs=regularTextArea),                        
        }

class ManifestacionesMitoForm(ModelForm) :
    class Meta:
        widgets = {                
				'descripcionMito': AutosizedTextarea(attrs=regularTextArea),        
        }

class ManifestacionesCementerioForm(ModelForm) :
    class Meta:
        widgets = {                
                'descripcionCementerio': AutosizedTextarea(attrs=regularTextArea),         
        }

class ManifestacionesMonticuloForm(ModelForm) :
    class Meta:
        widgets = {                
                'descripcionMonticulo': AutosizedTextarea(attrs=regularTextArea),         
        }

class ManifestacionesOtrosForm(ModelForm) :
    class Meta:
        widgets = {                
                'otros':  AutosizedTextarea(attrs=regularTextArea),
        }
				
class OtrosValForm(ModelForm) :
    class Meta:
        widgets = {                               
                'texto':  AutosizedTextarea(attrs=regularTextArea),
        }

class ObservacionesForm(ModelForm) :
    class Meta:
        widgets = {                               
                'texto':  TextInput(attrs=regularTextArea),
        }

### Formularios para las clases de multimedia
class FotoForm(ModelForm) :
    class Meta:
        widgets = {                
                'negativo': TextInput(attrs=regularTextField),
                'tipoFotografia': TextInput(attrs=regularTextField),
                'fotografo': TextInput(attrs=regularTextField),
                'institucion': TextInput(attrs=regularTextField),
                'numReferencia': TextInput(attrs=regularTextField),                
                'numRollo': TextInput(attrs=regularTextField),
                'numFoto': TextInput(attrs=regularTextField),                
                'numMarcaNegativo': TextInput(attrs=regularTextField),
                'numCopiaAnar': TextInput(attrs=regularTextField),  
        }
        
class BibliografiaForm(ModelForm) :
    class Meta:
        widgets = {                
                'codigo': TextInput(attrs=regularTextField),
                'titulo': TextInput(attrs=regularTextField),
                'autor': TextInput(attrs=regularTextField),
                'ano': TextInput(attrs=regularTextField),
                'institucion': TextInput(attrs=regularTextField),                                
				'descripcion': TextInput(attrs=regularTextField)
        }

class MatAudioVisualForm(ModelForm) :
    class Meta:
        widgets = {                
                'formato': TextInput(attrs=regularTextField)
        }

class VideoForm(ModelForm) :
    class Meta:
        widgets = {                
                'anio': TextInput(attrs=regularTextField),
                'formato': TextInput(attrs=regularTextField),
                'titulo': TextInput(attrs=regularTextField),
                'autor': TextInput(attrs=regularTextField),
                'institucion': TextInput(attrs=regularTextField),                
                'numReferencia': TextInput(attrs=regularTextField),
                'numCopia': TextInput(attrs=regularTextField),
        }

class PaginaWebForm(ModelForm) :
    class Meta:
        widgets = {                
                'direccionURL': TextInput(attrs=regularTextField)
        }

class MultimediaForm(ModelForm) :
    class Meta:
        widgets = {                
                'tecnica': TextInput(attrs=regularTextField)
        }

class ObtencionInfoForm(ModelForm) :
    class Meta:
        widgets = {                
                'nombre': TextInput(attrs=regularTextField),
                'direccion':  AutosizedTextarea(attrs=regularTextArea),
                'telefono': TextInput(attrs=regularTextField),
                'telefonoCel': TextInput(attrs=regularTextField),
                'mail': TextInput(attrs=regularTextField),
                'paginaWeb': TextInput(attrs=regularTextField),                
                'twitter': TextInput(attrs=regularTextField),
                'nombreFacebook': TextInput(attrs=regularTextField),
                'blog': TextInput(attrs=regularTextField)      
        }
        
class RepGrafPiedraForm(ModelForm) :
    class Meta:
        widgets = {                
                'numPiezas': TextInput(attrs=shortTextField),
                'instituto': TextInput(attrs=fullTextField),
                'persona': TextInput(attrs=fullTextField),
                'tipoReproduccion' : Select(attrs=regularSelect)
        }

class TratFotoPiedraForm(ModelForm) :
    class Meta:
        widgets = {                
                'limpiezaCon': AutosizedTextarea(attrs=regularTextArea),
                'rellenoSurcos': AutosizedTextarea(attrs=regularTextArea),
                'tratamientoDigital': AutosizedTextarea(attrs=regularTextArea),
                'programaVersion' : AutosizedTextarea(attrs=regularTextArea),
                'otrosTratamientos' : AutosizedTextarea(attrs=regularTextArea),
                
        }

### Formularios utilizados por el backend para piedra        

class DimensionPiedraForm(ModelForm) :

    class Meta:
        widgets = {
        		'dimensiones': TextInput(attrs={'class': 'input-medium'}),            
                'alto': TextInput(attrs={'class': 'input-small'}),
                'largo': TextInput(attrs={'class': 'input-small'}),
            	'ancho': TextInput(attrs={'class': 'input-small'}),
        }
  
class ManifestacionesAsociadasForm(ModelForm):

	class Meta:
		widgets = {
				'hasMitos' : TextInput(attrs=regularTextField),
				'hasOtros' : TextInput(attrs=regularTextField),
		}

class UbicacionCarasForm(ModelForm) :

    class Meta:
        widgets = {                
                'bocaPrincipal':  TextInput(attrs=regularTextField),
                'altura': TextInput(attrs=regularTextField),                 
        }


class FigurasPorTipoForm (ModelForm):
    class Meta:
        widgets = {
            'numero': TextInput(attrs={'class': 'input-medium'}),
            'cantidad': TextInput(attrs={'class': 'input-small'}),
            'tipoFigura': Select(attrs={'class': 'input-medium'}),
            'numero': TextInput(attrs={'class': 'input-small'}),
            'descripcion' : AutosizedTextarea(attrs={'rows': 2})
        }			
	
class CaraTrabajadaForm (ModelForm):
    class Meta:
        widgets = {
            'numero': TextInput(attrs={'class': 'input-medium'}),
            'orientacion': Select(attrs={'class': 'input-medium'})
        }
		
class PiedraForm(ModelForm) :

    class Meta:
        widgets = {
                'yacimiento': LinkedSelect,
                'codigo': TextInput(attrs=regularTextField),
                'nombre': TextInput(attrs=regularTextField),
        }


