from haystack import indexes
from anarapp.models import Yacimiento, Piedra

##################################################
# Piedra Index
##################################################

class PiedraIndex(indexes.SearchIndex, indexes.Indexable):
	#Busqueda General
	text = indexes.CharField(document=True, use_template=True)
	
	#Piedra
	codigo 			    = indexes.CharField(model_attr='codigo')
	nombre 			= indexes.CharField(model_attr='nombre')
	figuras 		        = indexes.CharField(model_attr='nombreFiguras')

	def get_model(self):
		return Piedra

	def index_queryset(self, using=None):
		return self.get_model().objects.all()

##################################################
# Yacimiento Index
##################################################

class YacimientoIndex(indexes.SearchIndex, indexes.Indexable):
	#Busqueda General
	text = indexes.CharField(document=True, use_template=True)
	
	#Yacimiento
	codigo 			    = indexes.CharField(model_attr='codigo')
	pais                  = indexes.CharField(model_attr='pais')
	municipio 		= indexes.CharField(model_attr='municipio')
	estado 			= indexes.CharField(model_attr='estado')
	nombre 			= indexes.CharField(model_attr='nombre')

	localidad 		    = indexes.CharField()
	fotografia 		= indexes.CharField()
	tipo 			        = indexes.MultiValueField() 
	exposicion 		= indexes.MultiValueField() 

	manifestacion 	= indexes.MultiValueField() 	
	ubicacion 		= indexes.MultiValueField() 
	material 		= indexes.MultiValueField() 
	conservacion 	= indexes.MultiValueField() 
	
	manifasociadas 	= indexes.MultiValueField()
	carasurcopetrotipo  = indexes.MultiValueField()
	carasurcopetroancho = indexes.MultiValueField()
	carasurcopetroprofun = indexes.MultiValueField()
	

	def get_model(self):
		return Yacimiento

	def index_queryset(self, using=None):
		return self.get_model().objects.all()


	def prepare(self, obj):
		self.prepare_data = super(YacimientoIndex, self).prepare(obj)
		
		#Localidad Yacimiento
		try:
			localidad = obj.LocalidadYacimiento
			self.prepare_data['localidad'] = localidad.nombrePoblado + ' ' + localidad.nombreNoPoblado
		except:
			pass
		
		#Fotografias	
		fotografias = obj.FotografiaYac.all()
		self.prepare_data['fotografia'] = 'true' if fotografias.count() > 0 else 'false'
		
		#Tipo Yacimiento
		try:
			tipo = obj.TipoYacimiento
			self.prepare_data['tipo'] = []
			
			if tipo.esParedRocosa:
				self.prepare_data['tipo'].append(1)
			if tipo.esRoca:
				self.prepare_data['tipo'].append(2)
			if tipo.esDolmen:
				self.prepare_data['tipo'].append(3)
			if tipo.esAbrigo:
				self.prepare_data['tipo'].append(4)
			if tipo.esCueva:
				self.prepare_data['tipo'].append(5)
			if tipo.esCuevadeRec:
				self.prepare_data['tipo'].append(6)
			if tipo.esTerrenoSup:
				self.prepare_data['tipo'].append(7)
			if tipo.esTerrenoPro:
				self.prepare_data['tipo'].append(8)
		except:
			pass
			
		#Exposicion
		try:
			exposicion = obj.TipoExposicionYac
			self.prepare_data['exposicion'] = []			
			
			if exposicion.expuesto:
				self.prepare_data['exposicion'].append(1)
			#if exposicion.noExpuesto:
			#	self.prepare_data['exposicion'].append(2)
			if exposicion.expuestoperiodicamente:
				self.prepare_data['exposicion'].append(3)
		except:
			pass
			
		#Manifestaciones
		manifestaciones = obj.ManifestacionYacimiento.all()			
		self.prepare_data['manifestacion'] = []
		
		for m in manifestaciones:
			self.prepare_data['manifestacion'].append(m.tipoManifestacion)

		#Ubicacion de la manifestacion
		ubicaciones = obj.UbicacionYacimiento.all()
		self.prepare_data['ubicacion'] = []

		for u in ubicaciones:
			self.prepare_data['ubicacion'].append(u.ubicacionManifestacion)


		#Material
		try:
			material = obj.MaterialYacimiento
			self.prepare_data['material'] = []			
			
			if material.esRoca and material.esIgnea :
				self.prepare_data['material'].append(1)
			if material.esRoca and material.esMetamor:
				self.prepare_data['material'].append(2)
			if material.esRoca and materia.esSedimentaria:
				self.prepare_data['material'].append(3)
			if material.esTierra:
				self.prepare_data['material'].append(4)
			if material.esHueso:
				self.prepare_data['material'].append(5)
			if material.esCorteza:
				self.prepare_data['material'].append(6)
			if material.esPiel:
				self.prepare_data['material'].append(7)	
		except:
			pass

		#Conservacion
		try:
			conservacion = obj.EstadoConserYac
			self.prepare_data['conservacion'] = []
						
			if conservacion.enBuenEstado:
				self.prepare_data['conservacion'].append(1)
			if exposicion.estadoModificado:
				self.prepare_data['conservacion'].append(2)
			if conservacion.porErosion and conservacion.porErosionParModerada:
				self.prepare_data['conservacion'].append(3)
			if conservacion.porErosion and conservacion.porErosionParSevere:
				self.prepare_data['conservacion'].append(4)
			if conservacion.porErosion and conservacion.porErosionExtModerada:
				self.prepare_data['conservacion'].append(5)
			if conservacion.porErosion and conservacion.porErosionExtSevere:
				self.prepare_data['conservacion'].append(6)
		except:
			pass
			
		
		#Manifestaciones Asociadas
		try:
			asociada = obj.ManifestacionesAsociadas
			self.prepare_data['manifasociadas'] = []
			
			if asociada.esLitica:
				self.prepare_data['manifasociadas'].append(1)
			if asociada.esCeramica:
				self.prepare_data['manifasociadas'].append(2)
			if asociada.esOseo:
				self.prepare_data['manifasociadas'].append(3)
			if asociada.esConcha:
				self.prepare_data['manifasociadas'].append(4)
			if asociada.esCarbon:
				self.prepare_data['manifasociadas'].append(5)
			if asociada.esMito:
				self.prepare_data['manifasociadas'].append(6)
			if asociada.esCementerio:
				self.prepare_data['manifasociadas'].append(7)
			if asociada.esMonticulo:
				self.prepare_data['manifasociadas'].append(8)
		except:
			pass

		#CaraSurcoPetroglifo

		try:
			caracpetro = obj.CaracSurcoPetroglifo
			self.prepare_data['carasurcopetroancho'] = caracpetro.anchoDe + ' ' +caracpetro.anchoA
			self.prepare_data['carasurcopetroprofun'] = caracpetro.produndidadDe + ' '+caracpetro.profundidadA
			self.prepare_data['carasurcopetrotipo'] = []
			if caracpetro.esBase:
				self.prepare_data['carasurcopetrotipo'].append(1)
			if caracpetro.esBaseRedonda:
				self.prepare_data['carasurcopetrotipo'].append(2)
			if caracpetro.esBaseAguda:
				self.prepare_data['carasurcopetrotipo'].append(3)
			if caracpetro.esBajoRelieve:
				self.prepare_data['carasurcopetrotipo'].append(4)
			if caracpetro.esBajoRelieveLineal:
				self.prepare_data['carasurcopetrotipo'].append(5)
			if caracpetro.esBajoRelievePlanar:
				self.prepare_data['carasurcopetrotipo'].append(6)
			if caracpetro.esAltoRelieve:
				self.prepare_data['carasurcopetrotipo'].append(7)
			if caracpetro.esAltoRelieveLineal:
				self.prepare_data['carasurcopetrotipo'].append(8)
			if caracpetro.esAltoRelievePlanar:
				self.prepare_data['carasurcopetrotipo'].append(9)
			if caracpetro.esAreaInterlineal:
				self.prepare_data['carasurcopetrotipo'].append(10)
			if caracpetro.esAreaInterlinealPulida:
				self.prepare_data['carasurcopetrotipo'].append(11)
			if caracpetro.esAreaInterlinealRebajada:
				self.prepare_data['carasurcopetrotipo'].append(12)
			if caracpetro.esGrabadoSuperpuesto:
				self.prepare_data['carasurcopetrotipo'].append(13)
			if caracpetro.esGrabadoRebajado:
				self.prepare_data['carasurcopetrotipo'].append(14)

		except:
			pass

		return self.prepare_data	

"""
class BaseIndex(indexes.SearchIndex, indexes.Indexable):
	#Busqueda General
	text = indexes.CharField(document=True, use_template=True)	

	def get_model(self):
		return Yacimiento

	def index_queryset(self, using=None):
		return self.get_model().objects.all()
		
	def prepare(self, instance):
		self.prepare_data = super(BaseIndex, self).prepare(instance)
		
		#Listando todas las piedras una sola vez
		piedras = None
		try:
			piedras = instance.Piedra.all()
		except:
			pass
		
		#Recorriendo todos los modelos de anarapp
		for mname, model in dynamic.get_models(anarapp.models):
			if mname == 'Yacimiento':
				continue
			
			foreign = None
			elem 	= None
			elems	= None
			
			#Se relaciona con Piedra y existe al menos una piedra
			if dynamic.has_attr(model, 'piedra') and piedras != None:
				try:
					elems = [getattr(piedra, name) for piedra in piedras]
				except:
					continue
				
				for fname, ftype, name in dynamic.get_attrs(model):
			 		if ftype == 'OneToOneField' or ftype == 'ForeignKey':
						continue
						
					self.prepare_data[fname] = [getattr(e, name) for e in elems]
				continue
				
			#Se relaciona con Yacimiento
			if dynamic.has_attr(model, 'yacimiento'):
				foreign = dynamic.get_type(model, 'yacimiento')
				try:
					elem = getattr(instance, mname)
				except:
					continue
			
			#Relaciones uno a uno: un campo por modelo	
			if foreign == 'OneToOneField':
				for fname, ftype, name in dynamic.get_attrs(model):
					if ftype == 'OneToOneField' or ftype == 'ForeignKey':
						continue
					
					value = getattr(elem, name)
					
					#Troll Attribute
					if fname.endswith('cantidad'):
						value = unicode(value)
						
					#Troll Type
					if ftype == 'BooleanField':
						value = 'true' if getattr(elem, name) else 'false'
						
					self.prepare_data[fname] = value
			 
			#Relaciones muchos a muchos: todos los campos multivalue
			elif foreign == 'ForeignKey':
				elems = elem.all()
				
				for fname, ftype, name in dynamic.get_attrs(model):
			 		if ftype == 'OneToOneField' or ftype == 'ForeignKey':
						continue
					
					values = []
					
					#Handling Troll Type
					if ftype == 'BooleanField':
						for e in elems:
							values.append('true' if getattr(e,name) else 'false')
					else:
						values = [getattr(e, name) for e in elems]
					
					self.prepare_data[fname] = values
						
		
		#print self.prepare_data			
		return self.prepare_data


def crear_yacimiento_index():
	attrs = {}

	#Recorriendo todos los modelos de anarapp
	for mname, model in dynamic.get_models(anarapp.models):
		foreign = None
			
		#Se relaciona con Yacimiento
		if dynamic.has_attr(model, 'yacimiento'):
			foreign = dynamic.get_type(model, 'yacimiento')
		
		#Se relaciona con Piedra	
		elif dynamic.has_attr(model, 'piedra'):
			foreign = dynamic.get_type(model, 'piedra')
		
		#Es la clase principal
		elif mname == 'Yacimiento':
			for fname, ftype, name in dynamic.get_attrs(model):
				attrs[fname] = indexes.CharField(model_attr=name)
			continue
		
		#Relacion uno a uno: un campo por modelo	
		if foreign == 'OneToOneField':
			for fname, ftype, name in dynamic.get_attrs(model):
				if ftype == 'CharField':
					attrs[fname] = indexes.CharField()
				elif ftype == 'IntegerField':
					attrs[fname] = indexes.IntegerField(null=True)
				elif ftype == 'BooleanField':
					attrs[fname] = indexes.CharField()					
				elif ftype == 'DateField':
					attrs[fname] = indexes.DateField()
		
		#Relacion muchos a muchos: todos los campos con multivalue			
		elif foreign == 'ForeignKey':
			for fname, ftype, name in dynamic.get_attrs(model):
				if ftype == 'OneToOneField' or ftype == 'ForeignKey':
					continue
				attrs[fname] = indexes.MultiValueField()		 

	return type("YacimientoIndex", (BaseIndex, indexes.Indexable), attrs)

########################
# Creando Index	
########################
YacimientoIndex = crear_yacimiento_index()
"""
