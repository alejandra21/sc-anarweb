# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ObjectDoesNotExist
from smart_selects.db_fields import ChainedForeignKey

from django.utils.safestring import mark_safe

########################################################################################
# Clases modificadas
########################################################################################

def short_text(text):
	""" Retorna un string limitado para evitar que los toString se vean muy largos"""
	return text[0:100]

class CharField(models.CharField):
	
	"""Tipo de Dato implementado para evitar que los campos títulos y textos se 
	vean limitados, al utilizar el tipo de datos de postgre 'text' que es sin limite."""

	def __init__(self, *args, **kwargs):
		kwargs.setdefault('max_length', 65000)
		super(CharField, self).__init__(*args, **kwargs)

	def db_type(self, connection):
		return 'text'

	def south_field_triple(self):
		"""Only necessary if using South migrations, which you should."""
		from south.modelsinspector import introspector
		field_class = self.__class__.__module__ + "." + self.__class__.__name__
		args, kwargs = introspector(self)
		return (field_class, args, kwargs)
		
########################################################################################
# Diagrama de yacimiento
########################################################################################

class Estado(models.Model):
        
    nombre = CharField('3. Estado/Provincia')
    activo = models.IntegerField('Activo', validators=[MinValueValidator(0), MaxValueValidator(1)])
     
    #representacion en string de un objeto de tipo estado
    def __unicode__(self):
        return self.nombre
        	
    abbr = 'edo'

    class Meta:
        verbose_name = '3. Estado/Provincia'
        verbose_name_plural = '3. Estado/Provincia'

class Municipio(models.Model):
        
    nombre = CharField('2. Municipio')
    estado = models.ForeignKey(Estado, related_name='Municipio')	
    activo = models.IntegerField('Activo', validators=[MinValueValidator(0), MaxValueValidator(1)])
    
    #representacion en string de un objeto de tipo municipio
    def __unicode__(self):
        return self.nombre
        	
    abbr = 'mpio'

    class Meta:
        verbose_name = '2. Municipio'
        verbose_name_plural = '2. Municipios'		
		
class Yacimiento(models.Model):
       
    codigo = models.CharField('(00). Codigo ANAR', unique = True, max_length=20)
    pais = CharField('0. Pais',  default = 'Venezuela')
    nombre = CharField('1. Nombre(s) del Yacimiento', blank = True, null = True)
    estado = models.ForeignKey(Estado, related_name='EstadoYac', verbose_name = '3. Estado/Provincia', blank = True, null = True)		    
    municipio = ChainedForeignKey(Municipio, related_name='MunicipioYac', verbose_name = '2. Municipio', blank = True, null = True,
					chained_field = 'estado', chained_model_field = 'estado', show_all = False, auto_choose = True)
	     
    #representacion en string de un objeto tipo Yacimiento
    def __unicode__(self):
        return short_text('PB1-' + self.codigo + '-' + self.nombre)
        
    def _get_tipo_manifestaciones(self):
	
        "Determina los tipos de manifestaciones presentes en un yacimiento"
        try :
            manifestacion = ManifestacionYacimiento.objects.get(yacimiento=self.id)
            return manifestacion.texto_descriptivo
        except ObjectDoesNotExist:
            return '';
			
    tipos_de_manifestaciones = property(_get_tipo_manifestaciones)
	
    abbr = 'yac'

    class Meta:
        verbose_name = 'Yacimiento'
        verbose_name_plural = 'Yacimientos'



class Yacimiento(models.Model):
       
    codigo = models.CharField('(00). Codigo ANAR', unique = True, max_length=20)
    pais = CharField('0. Pais',  default = 'Venezuela')
    nombre = CharField('1. Nombre(s) del Yacimiento')
    municipio = CharField('2. Municipio')    
    estado = CharField('3. Estado/Provincia')    
     
    #representacion en string de un objeto tipo Yacimiento
    def __unicode__(self):
        return short_text('PB1-' + self.codigo + '-' + self.nombre)
        
    def _get_tipo_manifestaciones(self):
	
        "Determina los tipos de manifestaciones presentes en un yacimiento"
        try :
            manifestacion = ManifestacionYacimiento.objects.get(yacimiento=self.id)
            return manifestacion.texto_descriptivo
        except ObjectDoesNotExist:
            return '';
			
    tipos_de_manifestaciones = property(_get_tipo_manifestaciones, '13. Tipo de Manifestación')
	
    abbr = 'yac'

    class Meta:
        verbose_name = 'Yacimiento'
        verbose_name_plural = 'Yacimientos'

class LocalidadYacimiento(models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='LocalidadYacimiento')
    
    esCentroPoblado = models.BooleanField('4.1. Centro de Poblado')
    esUrbano = models.BooleanField('4.1.1. Urbano')
    esRural = models.BooleanField('4.1.2. Rural')
    esIndigena = models.BooleanField('4.1.3. Indigena')
    nombrePoblado = CharField('4.1.4. Nombre', blank = True)
    esCentroNoPoblado = models.BooleanField('4.2. No Poblado')
    nombreNoPoblado = CharField('4.2.1. Nombre', blank = True)

    abbr = 'loc'

    def __unicode__(self):
        return '' # '# ' + str(self.id)
            
    class Meta:
        verbose_name = '4. Localidad'
        verbose_name_plural = '4. Localidad'
		
class UsoActSuelo(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='UsoActSuelo')
    
    esForestal = models.BooleanField('5.1. Forestal')
    esGanadero = models.BooleanField('5.2. Ganadero')
    esAgriRiesgo = models.BooleanField('5.3. Agricultura de Riesgo')
    esAgriTemp = models.BooleanField('5.4. Agricultura Temporal')
    esSueloUrbano = models.BooleanField('5.5. Urbano')
    esSueloTuristico = models.BooleanField('5.6. Turístico')
    
    abbr = 'uas'

    class Meta:
        verbose_name = '5. Uso Actual Del Suelo'
        verbose_name_plural = '5. Uso Actual Del Suelo'
    
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class TenenciaDeTierra(models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='TenenciaDeTierra')
   
    esPrivada = models.BooleanField('5.7.1. Privada')
    esComunal = models.BooleanField('5.7.2. Comunal')
    esEjido = models.BooleanField('5.7.3. Ejido')
    esMunicipal = models.BooleanField('5.7.4. Municipal')
    esABRAE = models.BooleanField('5.7.5. ABRAE (Área Bajo Régimen Especial)')
    esTenenciaOtros = CharField('5.7.6. Otros', blank = True)
    
    abbr = 'tdt'
    
    class Meta:
        verbose_name = '5.7 Tenencia de la Tierra'
        verbose_name_plural = '5.7 Tenencia de la Tierra'

    def __unicode__(self):
        return '' # '# ' + str(self.id)

class Indicaciones(models.Model):
 
    yacimiento = models.OneToOneField(Yacimiento, related_name='Indicaciones')
    
    direcciones = CharField('6. Indicaciones para llegar al Yacimiento', blank = True) 
    puntoDatum = CharField('6.1 Punto Datum ', blank = True)
    
    abbr = 'ind'
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = '6. Indicaciones para llegar al Yacimiento'

    def __unicode__(self):
        return '' # '# ' + str(self.id)

class Croquis (models.Model):

    yacimiento = models.ForeignKey(Yacimiento, related_name='Croquis')
    archivo = models.ImageField('6.2. Esquema de llegada - Archivo', upload_to='esquema/%Y_%m', null=True, blank=True)
    
    abbr = 'crq'

    class Meta:
        verbose_name = '..'
        verbose_name_plural = ''

    def __unicode__(self):
        return '' # '# ' + str(self.id)

class Plano (models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='Plano')
    numeroPlano = CharField('7. Número de plano', blank = True)
    abbr = 'pln'

    class Meta:
        verbose_name = '7. Número de Plano'
        verbose_name_plural = '7. Número de Plano'
    
    def __unicode__(self):
        return '' # '# ' + str(self.id)

 
class Coordenadas (models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='Coordenadas')
   
    longitud = CharField('8. Long. O(W)', blank = True)
    latitud = CharField('8. Lat. N', blank = True)
    utmAdicional = CharField('8. Utm Adicional', blank = True)
    
    abbr = 'crd'

    class Meta:
        verbose_name = '8. Coordenadas'
        verbose_name_plural = '8. Coordenadas'

    def __unicode__(self):
        return '' # '# ' + str(self.id)

class Datum (models.Model):
    
    OPCIONES_DATUM = (
        (1, '9.1 WGS 84'),
        (2, '9.2 La Canoa - Provisional Suramérica 1956'),
    ) 
     
    yacimiento = models.OneToOneField(Yacimiento, related_name='Datum')    
    tipoDatum = models.IntegerField('9. Datum GPS',choices = OPCIONES_DATUM, blank = True,null = True)
    
    abbr = 'dtm'

    class Meta:
        verbose_name = '9. Datum GPS'
        verbose_name_plural = '9. Datum GPS'

    def __unicode__(self):
        return '' # '# ' + str(self.id) 

class Altitud (models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='Altitud')

    texto = CharField('10.0. Texto', blank = True)   
    altura = CharField('10.1. Altura en mts', blank = True)
    superficie = CharField('10.2. Superficie en m2', blank = True)
    desarrollo = CharField('10.3. Desarrollo', blank = True)
    desnivel = CharField('10.4. Desnivel', blank = True)
    abbr = 'atd'  

    class Meta:
        verbose_name = '10. Altitud'
        verbose_name_plural = '10. Altitud'

    def __unicode__(self):
        return '' # '# ' + str(self.id)

class FotografiaYac (models.Model):
    
    yacimiento = models.ForeignKey(Yacimiento, related_name='FotografiaYac')
       
    esAerea = models.BooleanField('11. Aerea')
    noEsAerea = models.BooleanField('11. No Aerea')
    esSatelital = models.BooleanField('11. Satelital')
    fecha = models.CharField('11. Fecha', blank = True, null= True, max_length=100)	
    archivo = models.ImageField('11. Fotografía - Archivo', upload_to='yacimiento/%Y_%m', null=True, blank=True)
    
    abbr = 'fty'  

    class Meta:
        verbose_name = '11. Fotografia'
        verbose_name_plural = '11. Fotografias'

    def __unicode__(self):
        return '' # '# ' + str(self.id)

class TipoYacimiento (models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='TipoYacimiento')

    esParedRocosa = models.BooleanField('12.1. Pared Rocosa')
    esRoca = models.BooleanField('12.2. Roca')
    esDolmen = models.BooleanField('12.3. Dolmen(natural)')
    esAbrigo = models.BooleanField('12.4. Abrigo')
    esCueva = models.BooleanField('12.5. Cueva')
    esCuevadeRec = models.BooleanField('12.6. Cueva de Recubrimiento')
    esTerrenoSup = models.BooleanField('12.7. Terreno Superficial')
    esTerrenoPro = models.BooleanField('12.8. Terreno Profundo')
    
    abbr = 'tyc'

    class Meta:
        verbose_name = '12. Tipo de Yacimiento'
        verbose_name_plural = '12. Tipo de Yacimiento'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)


class ManifestacionYacimiento(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ManifestacionYacimiento')

    esGeoglifo = models.BooleanField('13.1. Geoglifo')
    esPintura = models.BooleanField('13.2. Pintura Rupestre')
    esPetroglifo = models.BooleanField('13.3. Petroglifo')
    esPetroglifoPintado = models.BooleanField('13.3.1. Petroglifo Pintado')
    esMicroPetroglifo = models.BooleanField('13.4. Micro-Petroglifo')
    esPiedraMiticaNatural = models.BooleanField('13.5. Piedra Mítica Natural')
    esCerroMiticoNatural = models.BooleanField('13.6. Cerro Mítico Natural')
    esCerroConPetroglifo = models.BooleanField('13.6.1. Con Petroglifo')
    esCerroConPintura = models.BooleanField('13.6.2. Con Pintura')
    esCerroConDolmen = models.BooleanField('13.6.3. Con Dolmen')
    esMonumentosMegaliticos = models.BooleanField('13.7. Monumentos Megalíticos')
    esMonolitos = models.BooleanField('13.7.1. Monolitos')
    esMonolitoConGrabados = models.BooleanField('13.7.1.1. Con Grabados')
    esMenhires = models.BooleanField('13.7.2. Menhires')
    esMenhiresConPuntos = models.BooleanField('13.7.2.1. Con Puntos Acoplados')
    esMenhiresConPetroglifo = models.BooleanField('13.7.2.2. Con Petroglifo')
    esMenhiresConPintura = models.BooleanField('13.7.2.3. Con Pintura')
    esAmolador = models.BooleanField('13.8. Amolador')
    esBatea = models.BooleanField('13.9. Batea')
    esPuntosAcoplados = models.BooleanField('13.10. Puntos Acoplados')
    esCupulas = models.BooleanField('13.11. Cupulas')
    esMortero = models.BooleanField('13.12. Mortero o Metate')
	
    abbr = 'tmy'

    def __unicode__(self):
        return '' # '# ' + str(self.id)
	
    def get_texto_descriptivo(self):
	
		"Genera un texto descriptivo de los tipos de manfestacion que representa el objeto"				
		return  (
			('Geoglifo, ' if self.esGeoglifo else '') +
			('Pintura Rupestre, ' if self.esPintura else '') +
			('Petroglifo, ' if self.esPetroglifo else '' ) +
			('Petroglifo Pintado, ' if self.esPetroglifoPintado else '' ) +
			('Micro-Petroglifo, ' if self.esMicroPetroglifo else '' ) +
			('Piedra Mítica Natural, ' if self.esPiedraMiticaNatural else '' ) +
			('Cerro Mítico Natural, ' if self.esCerroMiticoNatural else '' ) + 
			('Cerro Mítico Natural Con Petroglifo, ' if self.esCerroConPetroglifo else '' ) +
			('Cerro Mítico Natural Con Pintura, ' if self.esCerroConPintura else '' ) +
			('Cerro Mítico Natural Con Dolmen, ' if self.esCerroConDolmen else '' ) +
			('Monumentos Megalíticos, ' if self.esMonumentosMegaliticos else '' ) +
			('Monolitos, ' if self.esMonolitos else '' ) +
			('Monolitos Con Grabados, ' if self.esMonolitoConGrabados else '' ) +
			('Menhires, ' if self.esMenhires else '' ) +
			('Menhires Con Puntos Acoplados, ' if self.esMenhiresConPuntos else '' ) +
			('Menhires Con Petroglifo, ' if self.esMenhiresConPetroglifo else '' ) + 
			('Menhires Con Pintura, ' if self.esMenhiresConPintura else '' ) + 
			('Amolador, ' if self.esAmolador else '' ) +
			('Batea, ' if self.esBatea else '' ) +	
			('Puntos Acoplados, ' if self.esPuntosAcoplados else '' ) +
			('Cúpulas, ' if self.esCupulas else '' ) +
			('Mortero o Metate ' if self.esMortero else '') 				
		)
	
    texto_descriptivo = property(get_texto_descriptivo)
	
    class Meta:
        verbose_name = '13. Tipo de Manifestación'
        verbose_name_plural = '13. Tipo de Manifestación'
	
    
class UbicacionYacimiento(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='UbicacionYacimiento')
    
    enCerro = models.BooleanField('14.1. Cerro')
    enCerroCima = models.BooleanField('14.1.1. Cima')
    enCerroLadera = models.BooleanField('14.1.2. Ladera')
    enCerroFalda = models.BooleanField('14.1.3. Falda')
    enCerroFila = models.BooleanField('14.1.4. Fila')
    enCerroPieDeMonte = models.BooleanField('14.1.5. Pie de Monte')
    enCerroBarranco = models.BooleanField('14.1.6. Barranco')
    enCerroAcantilado = models.BooleanField('14.1.7. Acantilado')
    enValle = models.BooleanField('14.2. Valle')
    enRio = models.BooleanField('14.3. Río')
    enRioLecho = models.BooleanField('14.3.1. Lecho')
    enRioMargenDerecha = models.BooleanField('14.3.2. Margen Derecha')
    enRioMargenIzquierda = models.BooleanField('14.3.3. Margen Izquierda')
    enRioIsla = models.BooleanField('14.3.4. Isla')
    enRioRaudal = models.BooleanField('14.3.5. Raudal')
    enRioCosta = models.BooleanField('14.4. Costa')

    abbr = 'ubm'
        
    class Meta:
        verbose_name = '14. Ubicación'
        verbose_name_plural = '14. Ubicación'
    
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class OrientacionYacimiento (models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='OrientacionYacimiento')

    haciaCerro = models.BooleanField('15.1. Hacia Cerro')
    haciaValle = models.BooleanField('15.2. Hacia Valle')
    haciaRio = models.BooleanField('15.3. Hacia Rio')
    haciaCosta = models.BooleanField('15.4. Hacia Costa')
    haciaCielo = models.BooleanField('15.5. Hacia Cielo')
    otros = CharField('15.6. Otros', blank = True)
    orientacion = CharField('15.7. Orientacion Cardinal', blank = True)
    
    abbr = 'oyc'

    class Meta:
        verbose_name = '15. Orientacion del Yacimiento'
        verbose_name_plural = '15. Orientacion del Yacimiento'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class TexturaSuelo (models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='TexturaSuelo')

    esRocaMadre = models.BooleanField('16.1. Roca Madre')
    esPedregoso = models.BooleanField('16.2. Pedregoso')
    esArenoso = models.BooleanField('16.3. Arenoso')
    esArcilloso = models.BooleanField('16.4. Arcilloso')
    mixto = CharField('16.5. Mixto', blank = True)
    
    abbr = 'tsl'

    class Meta:
        verbose_name = '16. Textura del Suelo'
        verbose_name_plural = '16. Textura del Suelo'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class FloraYacimiento (models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='FloraYacimiento')    
    flora = CharField('17. Flora', blank = True)
    
    abbr = 'fly'

    class Meta:
        verbose_name = '17. Flora'
        verbose_name_plural = '17. Flora'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class FaunaYacimiento (models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='FaunaYacimiento')
    fauna = CharField('18. Fauna', blank = True)
    
    abbr = 'fay'
    
    class Meta:
        verbose_name = '18. Fauna'
        verbose_name_plural = '18. Fauna'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class HidrologiaYacimiento (models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='HidrologiaYacimiento')
    
    rio = models.BooleanField('19.1. Rio')
    laguna = models.BooleanField('19.2. Laguna')
    arroyo = models.BooleanField('19.3. Arroyo')
    arroyoPerenne= models.BooleanField('19.3.1. Perenne')
    manantial = models.BooleanField('19.4. Manantial')
    manantialIntermitente = models.BooleanField('19.4.1. Intermitente')
    otros = CharField('19.5. Otros', blank = True)
    nombre = CharField('19.6. Nombre', blank = True)
    distancia = CharField('19.7. Distancia al Yacimiento', blank = True)
    observaciones = CharField('19.8. Observaciones', blank = True)
    
    abbr = 'hiy'

    class Meta:
        verbose_name = '19. Hidrología'
        verbose_name_plural = '19. Hidrología'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class TipoExposicionYac(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='TipoExposicionYac')
    
    expuesto = models.BooleanField('20.1. Expuesto')
    noExpuesto = models.BooleanField('20.2. No Expuesto')
    expuestoPeriodicamente = models.BooleanField('20.3. Expuesto Periódicamente')
    observaciones = CharField('20.4. Observaciones', blank = True)
    
    abbr = 'tey'

    class Meta:
        verbose_name = '20. Exposición'
        verbose_name_plural = '20. Exposición'

    def __unicode__(self):
        return '' # '# ' + str(self.id)

class ConstitucionYacimiento (models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ConstitucionYacimiento')
    
    nroPiedras = models.IntegerField('21.1. Nro de Piedras en el Yacimiento Original', blank = True, null = True, )
    nroPiedrasGrabadas = models.IntegerField('21.1.1. Nro de Piedras Grabadas', blank = True, null = True, )
    nroPiedrasPintadas = models.IntegerField('21.1.2. Nro de Piedras Pintadas', blank = True, null = True, )
    nroPiedrasColocadas = models.IntegerField('21.1.3. Nro Piedras Colocadas', blank = True, null = True, )
    otros = CharField('21.2. Otros', blank = True)
    
    abbr = 'cny'

    class Meta:
        verbose_name = '21. Constitución del Yacimiento'
        verbose_name_plural = '21. Constitución del Yacimiento'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class MaterialYacimiento(models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='MaterialYacimiento')
        
    esRoca = models.BooleanField('22.1. Roca')
    esIgnea = models.BooleanField('22.1.1. Origen - Ignea')
    esMetamor= models.BooleanField('22.1.2. Origen - Metamórfica')
    esSedimentaria = models.BooleanField('22.1.3. Origen - Sedimentaria')
    tipo = CharField('22.1.4. Origen - Tipo', blank = True)
    esTierra = models.BooleanField('22.2. Tierra')
    esHueso = models.BooleanField('22.3. Hueso')
    esCorteza = models.BooleanField('22.4. Corteza de árbol')
    esPiel = models.BooleanField('22.5. Pieles')
    otros = CharField('22.6. Otros', blank = True)
    
    abbr = 'may'

    class Meta:
        verbose_name = '22. Material'
        verbose_name_plural = '22. Material'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id) 

class TecnicaParaGeoglifo (models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='TecnicaParaGeoglifo')
    esGeoflifo = models.BooleanField('13.1. Geoflifo')
    tecnicas = CharField('23.1. Técnicas de Construcción', blank = True)
    
    abbr = 'tge'
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = '23. Técnicas'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class TecnicaParaPintura (models.Model):
 
    yacimiento = models.OneToOneField(Yacimiento, related_name='TecnicaParaPintura')
    
    esPintura = models.BooleanField('13.2. Pintura Rupestre')
    conDedo = models.BooleanField('23.2. Dedo')
    fibra = models.BooleanField('23.3. Fibra')
    soplado = models.BooleanField('23.4. Soplado')
    otros = CharField('23.5. Otros', blank = True)
    
    abbr = 'tpi'

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)    

class TecnicaParaPetroglifo (models.Model):
 
    yacimiento = models.OneToOneField(Yacimiento, related_name='TecnicaParaPetroglifo')
    
    esPetroglifo = models.BooleanField('13.3. Petroglifo')
    esGrabado = models.BooleanField('23.6. Grabado')
    esGrabadoPercusion = models.BooleanField('23.6.1. Percusión')
    esGrabadoPercusionDirecta = models.BooleanField('23.6.1.1. Directa')
    esGrabadoPercusionIndirecta = models.BooleanField('23.6.1.2. Indirecta')
    esAbrasion = models.BooleanField('23.6.2. Abrasión')
    esAbrasionPiedra = models.BooleanField('23.6.2.1. Piedra')
    esAbrasionArena = models.BooleanField('23.6.2.2. Arena')
    esConcha = models.BooleanField('23.6.2.3. Concha')
    otros = CharField('23.6.3. Otros', blank = True)
    
    abbr = 'tpe'

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class TecnicaParaMicroPetro (models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='TecnicaParaMicroPetro')
    
    esMicro = models.BooleanField('13.4. Micro-Petroglifo')
    esGrabado = models.BooleanField('23.6. Grabado')
    esGrabadoPercusion = models.BooleanField('23.6.1. Percusión')
    esGrabadoPercusionDirecta = models.BooleanField('23.6.1.1. Directa')
    esGrabadoPercusionIndirecta = models.BooleanField('23.6.1.2. Indirecta')
    esAbrasion = models.BooleanField('23.6.2. Abrasión')
    esAbrasionPiedra = models.BooleanField('23.6.2.1. Piedra')
    esAbrasionArena = models.BooleanField('23.6.2.2. Arena')
    esConcha = models.BooleanField('23.6.2.3. Concha')
    otros = CharField('23.6.3. Otros', blank = True)
    
    abbr = 'tmi'

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class TecnicaParaMonumentos (models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='TecnicaParaMonumentos')
    
    esMonumento = models.BooleanField('13.7. Monumentos Megalíticos')
    esMonolito = models.BooleanField('13.7.1 Monolitos')
    esMenhir = models.BooleanField('13.7.2 Menhires')
    esDolmen = models.BooleanField('13.7.3 Dolmen (artificial)')
    tecnicas = CharField('23.7. Técnicas de Construcción', blank = True)
    otros = CharField('23.8. Otros', blank = True)
    
    abbr = 'tmo'

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class CaracSurcoPetroglifo (models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='CaracSurcoPetroglifo')
    
    esCaracSucorPetro = models.BooleanField('13.3. Petroglifo')
    anchoDe = CharField('24.1. Ancho desde (en cm)', blank = True)
    anchoA = CharField('24.1. Ancho hasta (en cm)', blank = True)
    produndidadDe = CharField('24.2. Profundidad desde (en cm)', blank = True)
    profundidadA = CharField('24.2. Profundidad hasta (en cm)', blank = True)
    esBase = models.BooleanField('24.3. Base')
    esBaseRedonda = models.BooleanField('24.3.1. Redonda')
    esBaseAguda = models.BooleanField('24.3.2. Aguda')
    esBajoRelieve = models.BooleanField('24.4. Bajo Relieve')
    esBajoRelieveLineal = models.BooleanField('24.4.1. Lineal')
    esBajoRelievePlanar = models.BooleanField('24.4.2. Planar')
    esAltoRelieve = models.BooleanField('24.5. Alto Relieve')
    esAltoRelieveLineal = models.BooleanField('24.5.1. Lineal')
    esAltoRelievePlanar = models.BooleanField('24.5.2. Planar')
    esAreaInterlineal = models.BooleanField('24.6. Áreas Interlineales')
    esAreaInterlinealPulida = models.BooleanField('24.6.1. Pulidas')
    esAreaInterlinealRebajada = models.BooleanField('24.6.2. Rebajadas')
    esGrabadoSuperpuesto = models.BooleanField('24.7. Grabados Superpuestos')
    esGrabadoRebajado = models.BooleanField('24.8. Grabados Rebajados')
    
    abbr = 'cpe'

    class Meta:
        verbose_name = ''
        verbose_name_plural = '24. Características del surco grabado'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class CaracSurcoAmoladores(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='CaracSurcoAmoladores')
        
    esCaracSurcoAmoladores = models.BooleanField('13.9. Amoladores')
    largo = CharField('24.9. Largo (en cm)', blank = True)
    ancho = CharField('24.10. Ancho (en cm)', blank = True)
    diametro = CharField('24.11. Diámetro (en cm)', blank = True)
    
    abbr = 'cam'

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)
        
class CaracSurcoBateas(models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='CaracSurcoBateas')
    
    esCaracSurcoBateas = models.BooleanField('13.10. Bateas')
    largo = CharField('24.12. Largo (en cm)', blank = True)
    ancho = CharField('24.13. Ancho (en cm)', blank = True)
    diametro = CharField('24.13a. Diametro (en cm)',  blank = True)
    profundidad = CharField('24.13b. Profundidad (en cm)',  blank = True)
    abbr = 'cba'

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)


class CaracSurcoPuntosAcopl (models.Model):

    esCaracSurcPuntosAcopl = models.BooleanField('13.11. Puntos Acoplados')
    yacimiento = models.OneToOneField(Yacimiento, related_name='CaracSurcoPuntosAcopl')
    esPunteado= models.BooleanField('24.14. Punteado')
    diametro = CharField('24.14a. Diametro (en cm)',  blank = True)
    profundidad = CharField('24.14b. Profundidad (en cm)',  blank = True)
    otros = CharField('24.14c. Otros',  blank = True)    
    
    abbr = 'cpa'
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class CaracSurcoCupulas (models.Model):
    
    esCaracSurcoCupulas = models.BooleanField('13.12. Cúpula')
    yacimiento = models.OneToOneField(Yacimiento, related_name='CaracSurcoCupulas')
    largo = CharField('24.15. Largo (en cm)', blank = True)
    ancho = CharField('24.16. Ancho (en cm)', blank = True)
    diametro = CharField('24.17. Diámetro (en cm)', blank = True)
    profundidad = CharField('24.17a. Profundidad (en cm)',  blank = True)
    otros = CharField('24.17b. Otros',  blank = True)
    
    abbr = 'ccu'

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class CaracSurcoMortero (models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='CaracSurcoMortero')
    
    esCaracSurcoMortero = models.BooleanField('13.13. Mortero o Metate')
    largo = CharField('24.9. Largo (en cm)', blank = True)
    ancho = CharField('24.10. Ancho (en cm)', blank = True)
    
    abbr = 'cmr'

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)


class CaracDeLaPintura (models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='CaracDeLaPintura')

    esPinturaRupestre = models.BooleanField('13.2. Pintura Rupestre')
    esTecnicaDactilar = models.BooleanField('25.1.1. Técnica - Dactilar')
    esTecnicaFibra = models.BooleanField('25.1.2. Técnica - Fibra')
    otros = CharField('25.1.3. Técnica - Otros', blank = True)
    esLineaSencilla= models.BooleanField('25.2.1 Tipo de Línea - Sencilla')
    anchoDe = CharField('25.2.1.1 Ancho desde (en cm)', blank = True)
    anchoA = CharField('25.2.1.2 Ancho hasta (en cm)', blank = True)
    esLineaCompuesta= models.BooleanField('25.2.2 Tipo de Línea - Compuesta')
    anchoDeComp = CharField('25.2.2.1 Ancho desde (en cm)', blank = True)
    anchoAComp = CharField('25.2.2.2 Ancho hasta (en cm)', blank = True)  
    esFiguraRellena = models.BooleanField('25.3. Figura Rellena')
    esImpresionDeManos = models.BooleanField('25.4. Impresión de Manos')
    esImpresionDeManosPositivo = models.BooleanField('25.4.1. Positivo')
    esImpresionDeManosNegativo = models.BooleanField('25.4.2. Negativo')
    tienesFigurasSuperpuestas = models.BooleanField('25.5. Figuras Superpuestas')
 
    abbr = 'pin'
    
    class Meta:
        verbose_name = '13.2. Pintura Rupestre'
        verbose_name_plural = '25. Características de la Pintura'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class Colores (models.Model):

    yacimiento = models.ForeignKey(Yacimiento, related_name='Colores')
    c = CharField('C', blank = True)
    m = CharField('M', blank = True)
    y = CharField('Y', blank = True)
    k = CharField('K', blank = True)

    abbr = 'col'
    
    class Meta:
        verbose_name = '25.6. Colores'
        verbose_name_plural = '25.6. Colores'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)
		
class DescColores (models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ColoresPositiva')
    
    esPositiva = models.BooleanField('25.6.1 Positiva')
    posNegro = CharField('25.6.1.1 Negro', blank = True)
    posBlanco = CharField('25.6.1.2 Blanco', blank = True)
    posAmarillo = CharField('25.6.1.3 Amarillo', blank = True)
    posUnRojo = CharField('25.6.1.4 Un rojo', blank = True)
    posDosRojos = CharField('25.6.1.5 Dos rojos', blank = True)
    posTresRojos = CharField('25.6.1.6 Tres rojos', blank = True)	
	
    esNegativa = models.BooleanField('25.6.2 Negativa')
    negNegro = CharField('25.6.2.1 Negro', blank = True)
    negBlanco = CharField('25.6.2.2 Blanco', blank = True)
    negAmarillo = CharField('25.6.2.3 Amarillo', blank = True)
    negUnRojo = CharField('25.6.2.4 Un rojo', blank = True)
    negDosRojos = CharField('25.6.2.5 Dos rojos', blank = True)
    negTresRojos = CharField('25.6.2.6 Tres rojos', blank = True)	
	
    colorBase = CharField('25.6.3 Color base (áreas interlineales)', blank = True)	
    abbr = 'dco'
    
    class Meta:
        verbose_name = '25.6. Colores'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)
		
class CaracMonolitos(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='CaracMonolitos')
    
    esCarcaMonolitos = models.BooleanField('13.7.1 Monolitos')
    cantidad = models.IntegerField('26.1.. Cantidad ', blank = True, null = True, )
    esPinturaRupestre = models.BooleanField('13.7.1.1. Con Grabados')
    cantidadConGrabados = models.IntegerField('26.2.. Cantidad con Grabados', blank = True, null = True, )
    
    abbr = 'mon'

    class Meta:
        verbose_name = ''
        verbose_name_plural = '26. Características Monumentos Megalíticos'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class CaracMenhires(models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='CaracMehnires')
    
    esCaracMenhier = models.BooleanField('13.7.2 Menhires')
    sonPiedrasVerticales = models.BooleanField('26.0.. Piedras Verticales')
    cantidadPiedrasVerticales = models.IntegerField('26.3.. Cantidad', blank = True, null = True, )
    conPuntosAcoplados = models.BooleanField('13.7.2.1. Con Puntos Acoplados')
    cantidadConPuntosAcoplados = models.IntegerField('26.4.. Cantidad', blank = True, null = True, )
    ConPetroglifo = models.BooleanField('13.7.2.2. Con Petroglifo')
    cantidadConPetroglifo = models.IntegerField('26.5.. Cantidad', blank = True, null = True, )
    conPinturas = models.BooleanField('13.7.2.3. Con Pinturas')
    cantidadConPinturas = models.IntegerField('26.6.. Cantidad', blank = True, null = True, )
    distanciamiento = models.IntegerField('26.7.. Distanciamiento (en cm)', blank = True, null = True, )
    
    abbr = 'men'

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class CaracDolmenArt(models.Model):
   
    yacimiento = models.OneToOneField(Yacimiento, related_name='CaracDolmenArt')
    
    esCaracDolmen = models.BooleanField('13.7.3 Dolmen')
    ConPetroglifo = models.BooleanField('13.7.3.1. Con Petroglifo')
    cantidadConPetroglifo = models.IntegerField('26.8.. Cantidad', blank = True, null = True, )
    conPinturas = models.BooleanField('13.7.3.2. Con Pinturas')
    cantidadConPinturas = models.IntegerField('26.9.. Cantidad', blank = True, null = True, )
    
    abbr = 'dol'

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class NotasYacimiento(models.Model) :

    yacimiento = models.OneToOneField(Yacimiento, related_name='NotasYacimiento')
    notas = CharField('26.10. Notas', blank = True)

    abbr = 'dol'

    class Meta:
        verbose_name = '26.10 Notas'
        verbose_name_plural = '26.10 Notas'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)


class EstadoConserYac(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='EstadoConserYac')
   
    enBuenEstado = models.BooleanField('27.1. Bueno')
    estadoModificado = models.BooleanField('27.2. Modificado')
    trasladado = models.IntegerField('27.2.1. Trasladado', blank = True, null = True,
                                    validators=[MinValueValidator(1), MaxValueValidator(2)] )
    trasladadoPa = CharField('27.2.1. Trasladado Pa(s) Nro ', blank = True)
    sumergido = models.IntegerField('27.2.2. Sumergido', blank = True, null = True,
                                    validators=[MinValueValidator(1), MaxValueValidator(2)] )
    sumergidoPa = CharField('27.2.2. Sumergido Pa(s) Nro ', blank = True)
    enterrado = models.IntegerField('27.2.3. Enterrado', blank = True, null = True,
                                    validators=[MinValueValidator(1), MaxValueValidator(2)] )
    enterradoPa = CharField('27.2.3. Enterrado Pa(s) Nro ', blank = True)
    perdido = models.IntegerField('27.2.4. Perdido', blank = True, null = True,
                                    validators=[MinValueValidator(1), MaxValueValidator(2)] )
    perdidoPa = CharField('27.2.4. Perdido Pa(s) Nro ', blank = True)
    destruido = models.IntegerField('27.2.5. Destruido', blank = True, null = True,
                                     validators=[MinValueValidator(1), MaxValueValidator(2)] )
    destruidoPa = CharField('27.2.5. Destruido Pa(s) Nro ', blank = True)
    crecimientoVeg = models.IntegerField('27.2.6. Crecimiento Vegetal', blank = True, null = True,
                                        validators=[MinValueValidator(1), MaxValueValidator(2)] )
    crecimientoVegPa = CharField('27.2.6. Crecimiento Vegetal Pa(s) Nro ', blank = True)
    patina = models.IntegerField('27.2.7. Pátina', blank = True, null = True,
                                    validators=[MinValueValidator(1), MaxValueValidator(2)] )
    patinaPa = CharField('27.2.7. Pátina Pa(s) Nro ', blank = True)
    erosion = models.IntegerField('27.2.8. Erosión ', blank = True, null = True,
                                     validators=[MinValueValidator(1), MaxValueValidator(2)] )
    erosionPa = CharField('27.2.8. Erosión Pa(s) Nro ', blank = True)
    
    estaDestruido = models.BooleanField('27.3. Grado de Destrucción del Sitio')
    esPorCausaNatural = models.BooleanField('27.3.1. Natural')
    enPorCausaNaturalLigera = models.BooleanField('27.3.1.1. Ligera')
    enPorCausaNaturalAguda = models.BooleanField('27.3.1.2. Aguda')
    enPorCausaHumana = models.BooleanField('27.3.2. Humana')
    enPorCausaHumanaLigera = models.BooleanField('27.3.2.1. Ligera')
    enPorCausaHumanaAguda = models.BooleanField('27.3.2.1. Aguda')
    especificar = CharField('27.4. Especificar Causa y Efecto', blank = True)
    destruccionPotencial = models.BooleanField('27.5. Destrucción Potencial del Sitio. Causas:')
    
    abbr = 'ecy'

    class Meta:
        verbose_name = '27. Estado de la Conservación'
        verbose_name_plural = '27. Estado de la Conservación'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class CausasDestruccionYac(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='CausasDestruccionYac')
	
    porAsentamientoHumand = models.BooleanField('27.5.1. Asentamiento Humano')
    porObraCortoPlazo = models.BooleanField('27.5.2. Obra Infraestructura a Corto Plazo')
    porObraMedianoPlazo = models.BooleanField('27.5.3. Obra Infraestructura a Mediano Plazo')
    porObraLargoPlazo = models.BooleanField('27.5.4. Obra Infraestructura a Largo Plazo')
    porNivelacion = models.BooleanField('27.5.5. Nivelación del Terreno Como Obra Agrícola')
    porExtraccionFamiliar = models.BooleanField('27.5.6. Extracción Como Actividad Familiar')
    porExtraccionMayor = models.BooleanField('27.5.7. Extracción Como Actividad Mayor')
    porVandalismo = models.BooleanField('27.5.8. Vandalismo')
    porErosion = models.BooleanField('27.5.9. Erosión')
    porErosionParModerada = models.BooleanField('27.5.9.1. Erosión Parcial Moderada')
    porErosionParSevera = models.BooleanField('27.5.9.2. Erosión Parcial Severa')
    porErosionExtModerada = models.BooleanField('27.5.9.3. Erosión Extensiva Moderada')
    porErosionExtSevera = models.BooleanField('27.5.9.4. Erosión Extensiva Severa')
    otros = CharField('27.5.10  Otros', blank = True)
	
    abbr = 'cdy'

    class Meta:
        verbose_name = '27.5.1. Causas'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class IntensidadDestruccionYac(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='IntensidadDestruccionYac')
    observaciones = CharField('27.6. Observaciones Sobre Intensidad de Destrucción del Sitio, y Otros Procesos No Descritos', blank = True)	
    esDeTiempo = models.BooleanField('27.6.1. Tiempo')
    esInmediato = models.BooleanField('27.6.1.1. Inmediato')
    unAno = models.BooleanField('27.6.1.2. Un Año')
    dosAno = models.BooleanField('27.6.1.3.  Dos Años')
    tresAno = models.BooleanField('27.6.1.4. Tres Años')
    cuatroAno = models.BooleanField('27.6.1.5. Cuatro Años')
    cincoAno = models.BooleanField('27.6.1.6. Cinco Años')
    mas = CharField('27.6.1.7. Más', blank = True)
	
    abbr = 'idy'

    class Meta:
        verbose_name = '27.6.1. Tiempo'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)
	
class ConsiderTemp(models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='ConsiderTemp')
    
    cincoAno = models.BooleanField('28.1. Patina')
    otros = CharField('28.2. Otros', blank = True)
    
    abbr = 'tem'
        
    class Meta:
        verbose_name = '28. Consideración sobre Temporalidad'
        verbose_name_plural = '28. Consideración sobre Temporalidad'
    
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class CronologiaTentativa(models.Model):
    
    yacimiento = models.ForeignKey(Yacimiento, related_name='CronologiaTentativa')
    
    esCrono1 = models.BooleanField('29.1. Anterior a 5000 a.p.')
    esCrono2 = models.BooleanField('29.2. 5000 - 1500 a.p.')
    esCrono3 = models.BooleanField('29.3. 1500 a.p. - 200 n.e.')
    esCrono4 = models.BooleanField('29.4. 200 - 650/900 n.e.')
    esCrono5 = models.BooleanField('29.5. 650/900 - 1200 n.e.')
    esCrono6 = models.BooleanField('29.6. 1200 - 1521 n.e.')
    esCrono7 = models.BooleanField('29.7. Post 1521 n.e.')
    autor = CharField('29.8.  Autor', blank = True)
    fecha = CharField('29.8.1. Fecha', blank = True)
    institucion = CharField('29.8.2. Institución', blank = True)
    pais = CharField('29.8.3. País', blank = True)
    direccion = CharField('29.8.4. Dirección', blank = True)
    telefono = CharField('29.8.5. Tel/Fax', blank = True)
    mail = CharField('29.8.6. Correo Electrónico', blank = True)
    tecnica = CharField('29.8.7. Técnica', blank = True)
    bibliografia = CharField('29.8.8. Bibliografía', blank = True)
    twitter = CharField('29.8.9. Twitter', blank = True)
    facebook = CharField('29.8.10. Facebook', blank = True)

    abbr = 'cte'
    
    class Meta:
        verbose_name = '29. Cronología Tentativa'
        verbose_name_plural = '29. Cronología Tentativa'
    
    def __unicode__(self):
        return '' # '# ' + str(self.id)
	
class ManifestacionesAsociadas(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ManifestacionesAsociadas')
	 
    esLitica = models.BooleanField('30.1. Lítica')
    descripcionLitica = CharField('30.1. Descripción Lítica', blank = True)
    esCeramica = models.BooleanField('30.2. Cerámica')
    descripcionCeramica = CharField('30.2. Descripción Cerámica', blank = True)
    esOseo = models.BooleanField('30.3. Oseo')
    descripcionOseo = CharField('30.3. Descripción Oseo', blank = True)
    esConcha = models.BooleanField('30.4. Concha')
    descripcionConcha = CharField('30.4. Descripción Concha', blank = True)
    esCarbon = models.BooleanField('30.5. Carbón No Superficial', help_text='Se refiere a antiguos fogones encontrados en la estratigrafía.')
    descripcionCarbon = CharField('30.5. Descripción Carbón No Superficial', blank = True)
    esMito = models.BooleanField('30.6. Mitos')
    descripcionMito = CharField('30.6. Descripción Mitos', blank = True)
    esCementerio = models.BooleanField('30.7. Cementerios')
    descripcionCementerio = CharField('30.7. Descripción Cementerios', blank = True)
    esMonticulo = models.BooleanField('30.8. Montículos')
    descripcionMonticulo = CharField('30.8. Descripción Montículos', blank = True)
    otros = CharField('30.9. Otros', blank = True)
     
    abbr = 'mso'
 
    class Meta:
        verbose_name = '30. Manifestaciones Asociadas'
        verbose_name_plural = '30. Manifestaciones Asociadas'
         
    def __unicode__(self):
        return '' # '# ' + str(self.id)
		 
class ManifestacionesLitica(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ManifestacionesLitica')    
    esLitica = models.BooleanField('30.1. Lítica')
    descripcionLitica = CharField('Descripción', blank = True)
    
    abbr = 'mal'

    class Meta:
        verbose_name = '30. Manifestaciones Asociadas'
        verbose_name_plural = '30. Manifestaciones Asociadas'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)		

class ManifestacionesCeramica(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ManifestacionesCeramica')    
    esCeramica = models.BooleanField('30.2. Cerámica')
    descripcionCeramica = CharField('Descripción', blank = True)    
    
    abbr = 'mac'

    class Meta:
        verbose_name = '30. Manifestaciones Asociadas'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)	

class ManifestacionesOseo(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ManifestacionesOseo')    
    esOseo = models.BooleanField('30.3. Oseo')
    descripcionOseo = CharField('Descripción', blank = True)

    abbr = 'mao'

    class Meta:
        verbose_name = '30. Manifestaciones Asociadas'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)	
		
class ManifestacionesConcha(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ManifestacionesConcha')    
    esConcha = models.BooleanField('30.4. Concha')
    descripcionConcha = CharField('Descripción', blank = True)

    abbr = 'mco'

    class Meta:
        verbose_name = '30. Manifestaciones Asociadas'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)	
		
class ManifestacionesCarbon(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ManifestacionesCarbon')    
    esCarbon = models.BooleanField('30.5. Carbón No Superficial')
    descripcionCarbon = CharField('Descripción', blank = True)

    abbr = 'mcar'

    class Meta:
        verbose_name = '30. Manifestaciones Asociadas'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)	

class ManifestacionesMito(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ManifestacionesMito')    
    esMito = models.BooleanField('30.6. Mitos')
    descripcionMito = CharField('Descripción', blank = True)

    abbr = 'mami'

    class Meta:
        verbose_name = '30. Manifestaciones Asociadas'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)			

class ManifestacionesCementerio(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ManifestacionesCementerio')    
    esCementerio = models.BooleanField('30.7. Cementerios')
    descripcionCementerio = CharField('Descripción', blank = True)

    abbr = 'macm'

    class Meta:
        verbose_name = '30. Manifestaciones Asociadas'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)	

class ManifestacionesMonticulo(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ManifestacionesMonticulo')    
    esMonticulo = models.BooleanField('30.8. Montículos')
    descripcionMonticulo = CharField('Descripción', blank = True)

    abbr = 'mamn'

    class Meta:
        verbose_name = '30. Manifestaciones Asociadas'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)	

class ManifestacionesOtros(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ManifestacionesOtros')    
    otros = CharField('30.9. Otros', blank = True)

    abbr = 'maot'

    class Meta:
        verbose_name = '30. Manifestaciones Asociadas'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)		
		
########################################################################################
# Diagrama de piedra
########################################################################################

class Piedra(models.Model):

    """Representa la información de la ficha pa, recoge la información básica"""

    yacimiento = models.ForeignKey(Yacimiento, related_name='Yacimiento')
    
    codigo = models.CharField('0- Codigo de la roca', unique = True, max_length=20)#, primary_key=True)        
    nombre = CharField('1- Nombre de la roca',null=True,blank=True)
    
    def __unicode__(self):
        return short_text('Pa-' + self.codigo + '-' + self.nombre)
    
    abbr = 'pdr'

    class Meta:
        verbose_name = 'Roca'
        verbose_name_plural = 'Rocas'
		
class FotografiaPiedra (models.Model):
    
    piedra = models.ForeignKey(Piedra, related_name='FotografiaPiedra')
    aerea = models.BooleanField('1.2.1. Aerea')
    noEsAerea = models.BooleanField('1.2.2. No Aerea')
    satelital = models.BooleanField('1.2.3. Satelital')
    fecha = models.CharField('1.2.4. Fecha', blank = True, null= True, max_length=100)
    archivo = models.ImageField('1.2.5. Fotografía - Archivo', 
                                upload_to='piedra/%Y_%m', 
                                null=True, 
                                blank=True)
    
    abbr = 'ftp'  

    class Meta:
        verbose_name = ''
        verbose_name_plural = '1.2. Fotografias'
		
    def __unicode__(self):
        return '' # '# ' + str(self.id)		

class Piedra2(models.Model):
    """Continuacion de informacion de piedras """

    yacimiento = models.ForeignKey(Piedra, related_name='Piedra2')

    nombreFiguras = CharField('2- Nombre de las figuras', blank=True)    
    estado = models.ForeignKey(Estado, related_name='EstadoPied', verbose_name = '3- Estado', blank = True, null = True)
    numeroCaras = models.IntegerField('4- Numero de Caras')
    numeroCarasTrajabadas = models.IntegerField('5- Numero de caras trabajadas')

    abbr = 'pd2'  

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id) 


class DimensionPiedra(models.Model):

    """Representa la información de las dimensiones de la piedra"""

    piedra = models.ForeignKey(Piedra, related_name='DimensionPiedra')
    
    dimensiones = CharField('6a. Número de cara trabajada')
    alto =  CharField('7.1. Alto ' , blank = True)
    largo = CharField('7.2. Largo ', blank = True)
    ancho = CharField('7.3. Ancho ', blank = True)
                                        
    abbr = 'dip'
    
    def __unicode__(self):
        return '' # '# ' + str(self.id)
		
    class Meta:
        verbose_name = ''
        verbose_name_plural = '7. Dimensiones de la piedra'

class CaraTrabajada(models.Model):

    """Representa la información de la ficha pa, referente a las caras trabajadas """
    
    ORIENTACION_CARA_TRABAJADA = (
        (0, '0 - Tope'),
        (1, '1 - Norte'),
        (2, '2 - Noreste'),
        (3, '3 - Este'),
        (4, '4 - Sureste'),
        (5, '5 - Sur'),
        (6, '6 - Suroeste'),
        (7, '7 - Oeste'),
        (8, '8 - Noroeste'),
        (9, '9 - Piso o plano inclinado'),
		(10, 'n - Desconocida')
    )

    AYUDA_OCT='En caso de no conocerse la orientación cardinal úsese la letra "n" (no conocido) en lugar del número respectivo. Para más de una cara trabajada sin orientación cardinal conocida, úsese n1, n2, n3 y así sucesivamente según el número de caras trabajadas, por roca. Usese estas mismas denominaciones en todos los casos en que se pida el número de la cara trabajada. (Punto 6, 7, 9 y 10).'

    AYUDA_NCT='En rocas al aire libre se contarán únicamente las caras factibles de trabajar; no se cuenta la cara apoyada sobre el suelo. En cuevas se cuentan el piso, el techo y las paredes internas. En abrigos se pueden agregar paredes externas factibles de trabajar '
	
    piedra = models.ForeignKey(Piedra, related_name='CaraTrabajada')
    numero =  CharField('6a. Número de cara trabajada',help_text=AYUDA_NCT )
    orientacion = models.IntegerField('6b. Orientación de la cara', choices = ORIENTACION_CARA_TRABAJADA, help_text= AYUDA_OCT)
    
    abbr = 'cat'

    def __unicode__(self):
        return '' # '# ' + str(self.id)
	
    class Meta:
        verbose_name = ''
        verbose_name_plural = '6. Caras trabajadas'

class UbicacionCaras(models.Model):

    """Representa la información de la ficha pa, referente a la ubicacion
    de las  caras trabajadas """

    LUMINOSIDAD = (
        (0, 'No tiene'),
        (1, 'Fótico'),
        (2, 'Escótico'),
    )

    piedra = models.OneToOneField(Piedra, related_name='UbicacionCaras')
    
    todaLaCaverna = models.BooleanField('8.1. Toda la caverna')
    areasEspecificas = models.BooleanField('8.2. Áreas específicas')
    salaPrincipal = models.BooleanField('8.2.1. Sala principal')
    otraSala = models.BooleanField('8.2.2. Otra sala')
    lagoInterior = models.BooleanField('8.2.3. Lago interior')
    claraboya = models.BooleanField('8.2.4. Claraboya')

    principalMouth = CharField('8.3. Distancia Boca Principal',blank=True, null=True)
    luminosity = models.IntegerField('8.3.1. Luminosidad', choices = LUMINOSIDAD, blank=True, null=True)
    heights = CharField('8.3.2. Altura', blank=True, null=True)   
    requiereAndamiaje = models.BooleanField('8.3.2.1. ¿Requiere andamiaje?')
    
    abbr = 'uca'
	
    def __unicode__(self):
        return '' # '# ' + str(self.id)    
	
    class Meta:
        verbose_name = ''
        verbose_name_plural = '8. Ubicación caras trabajadas (Cuevas/Abrigos)'
        

class FigurasPorTipo(models.Model):

    """Representa la información de la ficha pa, referente a los conjuntos de
    figuras por tipo presentes en cada cara"""

    TIPO_FIGURA = (
        (1, '9.1 - Antropomorfas'),
        (2, '9.2 - Zoomorfas'),
        (3, '9.3 - Geométricas'),
        (4, '9.4 - Puntos Acoplados'),
        (5, '9.5 - Cupulas'),
        (6, '9.6 - Zoo-antropomorfas'),
        (7, '9.7 - Antropo-geométricas'),
        (8, '9.8 - Zoo-geométricas'),
        (9, '9.9 - Amoladores'),
        (10, '9.10 - Bateas'),
    )

    AYUDA_CID= 'Utilícese la letra "i" (incompleto) delante del número, para los casos en que la cantidad de figuras, sea mayor que la expuesta, pero no se pueda cuantificar con exactitud, que sea mayor por la altura de los grabados, por efectos de erosión u otros. \n Por ejemplo, en la cara 4 de una roca hay más de 25 puntos, sin poderse cuantificar con exactitud esa cifra. Se coloca entonces: i-25.\nPara aquellos casos en que se desconozcan las cantidades totalmente, se usará "i" en lugar de números.'

   
    piedra = models.ForeignKey(Piedra, related_name='FigurasPorTipo')    
    numero =  CharField( '6.a. Número de cara trabajada') 
    tipoFigura = models.IntegerField('9. Figuras',choices = TIPO_FIGURA)	
    cantidad = CharField('9.a. Cantidad', blank=True)  
    esCantidadInexacta = models.CharField('9.b. Cantidad Inexacta O Desconocida', max_length=10 ,help_text= AYUDA_CID,blank = True, null = True)	
    descripcion = CharField('9.c. Descripcion', blank=True)
    abbr = 'fpt'    
    
    def __unicode__(self):
        return '' # '# ' + str(self.id)
		
    class Meta:
        verbose_name = ''
        verbose_name_plural = '9. Figuras'

class EsquemaPorCara(models.Model):

    """Representa la información de la ficha pa, referente al esquema
    de la cara de la piedra"""

    piedra = models.ForeignKey(Piedra, related_name='EsquemaPorCara')    
    numero =  CharField( '6.a. Número de cara trabajada ')  
    textoCara = CharField('10.1. Cara') 
    posicion = CharField('10.2. Posicion de las figuras en la cara', ) 
    
    def __unicode__(self):
        return '' # '# ' + str(self.id)
		
    abbr = 'epc'

    class Meta:
        verbose_name = 'Esquema por cara'
        verbose_name_plural = '10. Esquemas por caras'

class ConexionFiguras(models.Model):

    """Representa la información de la ficha pa, referente a la conexion
    de las figuras en la piedra"""
    CONEXION_FIGURAS = (
        (1, '1 - Presencia de una sola figura'),
        (2, '2 - Menos del 10% interconectadas'),
        (3, '3 - 50% interconectadas'),
        (4, '4 - Mas del 80% interconectadas'),
    )    
    piedra = models.ForeignKey(Piedra, related_name='ConexionFiguras')    
    conexionFiguras = models.IntegerField('11. Conexion de figuras', choices = CONEXION_FIGURAS)
    
    def __unicode__(self):
        return '' # '# ' + str(self.id)
		
    abbr = 'cnx'
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

class Manifestaciones(models.Model):

    """Representa la información de la ficha pa, indicando el tipo de manifestacion"""

    piedra = models.ForeignKey(Piedra, related_name='Manifestaciones')
    
    tienePetroglifos = models.BooleanField('1.2.1. Petroglifos', blank=True)
    tieneRupestres = models.BooleanField('1.2.2. Pintura Rupestre', blank=True)
    tieneAmoladore = models.BooleanField('1.2.3. Amoladores', blank=True)
    tienePuntosAc = models.BooleanField('1.2.4. Puntos Acoplados', blank=True)
    tieneCupula = models.BooleanField('1.2.5. Cupulas', blank=True)
    hasMitos = CharField('1.2.6. Mitos', blank=True) 
    hasOtros = CharField('1.2.7. Otros', blank=True)
    
    def __unicode__(self):
        return '' # '# ' + str(self.id)
	
    abbr = 'man'
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = '1.2 Manifestaciones Asociadas'
        

########################################################################################
# Tipos bases de multimedia
# Las clases que heredan de ella y son especificas a piedra o yacimiento
########################################################################################

# Tratamiento fotografico

class TratFoto(models.Model):

    """Representa el tratamiento dado a las fotografias recopiladas"""
    
    limpiezaCon = CharField('12.1. Limpieza con', blank=True)
    rellenoSurcos = CharField('12.2. Relleno de surcos con', blank=True)
    tratamientoDigital = CharField('12.3. Tratamiento digital', blank=True)
    programaVersion = CharField('12.4. Programa/versión', blank=True)
    otrosTratamientos = CharField('12.5. Otros', blank=True)

    def __unicode__(self):
        return '' # '# ' + str(self.id)
		
class TratFotoPiedra (TratFoto):

    """Representa el tratamiento dado a las fotografias recopiladas
    de las piedras"""

    piedra = models.OneToOneField(Piedra, related_name='TratFotoPiedra')
    
    abbr = 'tpp'
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = '12. Tratamiento para fotografías'

# Fotografia

class Foto (models.Model):

    """Representa la información de la fotografia"""
    
    TIPO_FOTOGRAFIA = (
        (1, 'Aerea'),
        (2, 'No aerea'),
        (3, 'Satelital'),
    )

    foto = models.ImageField('13.1 Fotografías', 
                                upload_to='piedra/apoyos/fotografia/%Y_%m', 
                                null=True, 
                                blank=True)
    foto2 = models.ImageField('13.1.0.0 Fotografía 2', 
                                upload_to='piedra/apoyos/fotografia/%Y_%m', 
                                null=True, 
                                blank=True)
    foto3 = models.ImageField('13.1.0.1 Fotografía 3', 
                                upload_to='piedra/apoyos/fotografia/%Y_%m',
                                null=True,
                                blank=True)
    foto4 = models.ImageField('13.1.0.2 Fotografía 4', 
                                upload_to='piedra/apoyos/fotografia/%Y_%m',
                                null=True,
                                blank=True)
    foto5 = models.ImageField('13.1.0.3 Fotografía 5', 
                                upload_to='piedra/apoyos/fotografia/%Y_%m',
                                null=True,
                                blank=True)





    tipoFotoA  = models.BooleanField(' Aerea')
    tipoFotoNA = models.BooleanField(' No Aerea')
    tipoFotoS  = models.BooleanField(' Satelital')
    tipoFotoNeg = models.BooleanField(' Negativo')
    fecha = models.CharField('13.1.1. Fecha', blank = True, null= True, max_length=100)
    fotografo  = CharField('13.1.2. Fotógrafo',blank = True, null= True)
    institucion  = CharField('13.1.3. Institucion ',blank = True, null= True)
    numReferencia = CharField('13.1.4. Nro de referencia',blank=True,null=True)
    numRollo = CharField('13.1.5. Nro de rollo',blank=True,null=True)
    numFoto = CharField('13.1.6. Nro de foto',blank=True,null=True)
    numMarcaNegativo = CharField('13.1.7. Nro marca en negativo',blank=True,null=True,default=None)
    esDeAnar = models.BooleanField('13.1.8. ¿Es de Anar?')
    numCopiaAnarFotoAN = CharField('13.1.8.1. Num Copia',blank=True,null=True)

    def __unicode__(self):
        return '' # '# ' + str(self.id)

class FotoPiedra (Foto):

    piedra = models.ForeignKey(Piedra, related_name='FotoPiedra')
    
    abbr = 'fop'
    
    class Meta:
        verbose_name =  ''
        verbose_name_plural = '13 Apoyos'

# Representación gráfica de la piedra

class RepGrafPiedra (models.Model):

    """Representa la información de la ficha pa, agrupa los distintos tipos
    de reproducciones gráficas a escala natural y reducida"""

    piedra = models.ForeignKey(Piedra, related_name='RepGrafPiedra')
	
    def __unicode__(self):
        return '' # '# ' + str(self.id)
    
    abbr = 'rgp'

class EscNatPiedra(RepGrafPiedra):

    TIPO_REPRODUCCION_NATURAL = (
        (1, '1 - Plana'),
        (2, '2 - Frotage'),
        (3, '3 - Calco'),
        (4, '4 - Tridimensional'),
        (5, '5 - Resina'),
        (6, '6 - Yeso'),
        (7, '7 - Papel de arroz'),
    )
    esEscNatPiedra = models.BooleanField('13.2.1. Reproducción gráfica escala natural')
    tipoReproduccione = models.IntegerField('13.2.1.1. Reproducción gráfica', choices = TIPO_REPRODUCCION_NATURAL,blank=True, null=True,default = None)
    numPiezasP = models.IntegerField('13.2.1.2. Número de piezas',blank=True, null=True,default = None)
    institutoP  = CharField('13.2.1.3. Institución ',blank=True, null=True,default = None)
    personaP  = CharField('13.2.1.4. Persona ',blank=True, null=True,default = None)

    abbr = 'enp'

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
    
class EscRedPiedra(RepGrafPiedra):

    """Representa la información de la ficha pa, de reproducciones gráficas
    a escala reducida"""
        
    TIPO_REPRODUCCION_REDUCIDA = (
        (1, '1 - Dibujo'),
        (2, '2 - Matriz'),
    )
    esEscNatPiedra = models.BooleanField('13.3.1. Reproducción gráfica escala reducida')
    tipoReproduccion = models.IntegerField('13.3.1.1. Reproducción gráfica', choices = TIPO_REPRODUCCION_REDUCIDA,blank=True, null=True,default = None)
    numPiezasP = models.IntegerField('13.3.1.2. Número de piezas',blank=True, null=True,default = None)
    institutoP  = CharField('13.3.1.3. Institución ',blank=True, null=True,default = None)
    personaP  = CharField('13.3.1.4. Persona ',blank=True, null=True,default = None)
    
    abbr = 'erp'

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

# Bibliografia

class Bibliografia(models.Model):

    TIPO_MAPA = (
        (1, '1 - Radar'),
        (2, '2 - Satelital'),
    )

    """Representa la bibliografia de un yacimiento o una piedra """
	
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class BibYacimiento(Bibliografia):

    yacimiento = models.ForeignKey(Yacimiento, related_name='BibYacimiento')
    
    esBibliografia = models.BooleanField('31.1 Bibliografía', default = True)
    conPdf = models.BooleanField('31.1.0 PDF')
    tienePDF = models.FileField('31.1.0.0. Archivo - PDF', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tienePDF1 = models.FileField('31.1.0.2. Archivo - PDF', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tienePDF2 = models.FileField('31.1.0.3. Archivo - PDF', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)
    conWord = models.BooleanField('31.1.0.0. Documento Word')
    tieneWord = models.FileField('31.1.0.0.1. Archivo - Word', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneWord1 = models.FileField('31.1.0.0.2. Archivo - Word', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)

    codigo = CharField('31.1.1. Código', blank = True)
    titulo = CharField('31.1.2. Título', blank = True)
    autor  = CharField('31.1.3. Autor ', blank = True)
    ano = CharField('31.1.4. Año', blank = True)
    institucion  = CharField('31.1.5. Institución', blank = True)
    conDibujo = models.BooleanField('31.1.6. Con dibujo',)
    archivo = models.FileField('31.1.6.1. Dibujo - Archivo', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)
    archivo1 = models.FileField('31.1.6.2. Dibujo - Archivo', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)
    archivo2 = models.FileField('31.1.6.3. Dibujo - Archivo', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)
    archivo3 = models.FileField('31.1.6.4. Dibujo - Archivo', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)
    archivo4 = models.FileField('31.1.6.5. Dibujo - Archivo', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)

    esFotografia = models.BooleanField('31.1.7. Con fotografía')
    tieneFotografia = models.FileField('31.1.7.0.0. Fotografía - Archivo', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneFotografia1 = models.FileField('31.1.7.0.1. Fotografía - Archivo', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneFotografia2 = models.FileField('31.1.7.0.2. Fotografía - Archivo', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneFotografia3 = models.FileField('31.1.7.0.3. Fotografía - Archivo', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneFotografia4 = models.FileField('31.1.7.0.4. Fotografía - Archivo', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)
    escolor = models.BooleanField('31.1.7.1. Color')
    esBlancoYNegro = models.BooleanField('31.1.7.2. B/N')
    esDiapositiva = models.BooleanField('31.1.7.3. Diapositiva')
    esPapel = models.BooleanField('31.1.7.4. Papel')
    esDigital = models.BooleanField('31.1.7.5. Digital')
    esNegativo = models.BooleanField('31.1.7.6. Negativo')
    description = models.BooleanField('31.1.8. Con mapa')
    tieneMapa = models.FileField('31.1.8.0.0. Mapa - Archivo', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneMapa1 = models.FileField('31.1.8.0.1. Mapa - Archivo', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneMapa2 = models.FileField('31.1.8.0.2. Mapa - Archivo', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneMapa3 = models.FileField('31.1.8.0.3. Mapa - Archivo', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneMapa4 = models.FileField('31.1.8.0.4. Mapa - Archivo', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tipoMapa = models.IntegerField('31.1.8.1. Tipo de mapa', choices = Bibliografia.TIPO_MAPA, blank = True,null = True)
	
    abbr = 'biy'
    
    class Meta:
        verbose_name = 'Bibliografía'
        verbose_name_plural = '31. Apoyos'

class BibPiedra(Bibliografia):

    piedra = models.ForeignKey(Piedra, related_name='BibPiedra')
    esbilbio = models.BooleanField('13.4. Bibliografía')
    tienePDF = models.BooleanField('13.4.0. PDF')
    pdfarchivo = models.FileField('13.4.0.1. Archivo - PDF',
                            upload_to='bibliografia_piedra/%Y_%m', 
                            null=True, 
                            blank=True)
    pdfarchivo1 = models.FileField('13.4.0.2. Archivo - PDF',
                            upload_to='bibliografia_piedra/%Y_%m', 
                            null=True, 
                            blank=True)
    pdfarchivo2 = models.FileField('13.4.0.3. Archivo - PDF',
                            upload_to='bibliografia_piedra/%Y_%m', 
                            null=True, 
                            blank=True)
    tieneWord = models.BooleanField('13.4.0. Word')
    wordarchivo = models.FileField('13.4.0.1. Archivo - Word',
                            upload_to='bibliografia_piedra/%Y_%m', 
                            null=True, 
                            blank=True)
    wordarchivo1 = models.FileField('13.4.0.2. Archivo - Word',
                            upload_to='bibliografia_piedra/%Y_%m', 
                            null=True, 
                            blank=True)        
    codigo = CharField('13.4.1. Código', blank = True)
    titulo = CharField('13.4.2. Título', blank = True)
    autor  = CharField('13.4.3. Autor ', blank = True)
    ano = CharField('13.4.4. Fecha', blank = True)	
    institucion  = CharField('13.4.5. Institución', blank = True)
    conDibujo = models.BooleanField('13.4.6. Con dibujo')
    archivo = models.FileField('13.4.6.1. Dibujo - Archivo', 
                                upload_to='bibliografia_piedra/%Y_%m', 
                                null=True, 
                                blank=True)
    archivo1 = models.FileField('13.4.6.2. Dibujo - Archivo', 
                                upload_to='bibliografia_piedra/%Y_%m', 
                                null=True, 
                                blank=True)
    archivo2 = models.FileField('13.4.6.3. Dibujo - Archivo', 
                                upload_to='bibliografia_piedra/%Y_%m', 
                                null=True, 
                                blank=True)
    archivo3 = models.FileField('13.4.6.4. Dibujo - Archivo', 
                                upload_to='bibliografia_piedra/%Y_%m', 
                                null=True, 
                                blank=True)
    archivo4 = models.FileField('13.4.6.5. Dibujo - Archivo', 
                                upload_to='bibliografia_piedra/%Y_%m', 
                                null=True, 
                                blank=True)
    esFotografia = models.BooleanField('13.4.7. Con fotografía')
    tieneFotografia = models.FileField('13.4.7.0.0. Fotografía - Archivo', 
                                 upload_to='bibliografia_piedra/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneFotografia1 = models.FileField('13.4.7.0.1. Fotografía - Archivo', 
                                 upload_to='bibliografia_piedra/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneFotografia2 = models.FileField('13.4.7.0.2. Fotografía - Archivo', 
                                 upload_to='bibliografia_piedra/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneFotografia3 = models.FileField('13.4.7.0.3. Fotografía - Archivo', 
                                 upload_to='bibliografia_piedra/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneFotografia4 = models.FileField('13.4.7.0.4. Fotografía - Archivo', 
                                 upload_to='bibliografia_piedra/%Y_%m', 
                                 null=True, 
                                 blank=True)
    escolor = models.BooleanField('13.4.7.1. Color')
    esBlancoYNegro = models.BooleanField('13.4.7.2. B/N')
    esDiapositiva = models.BooleanField('13.4.7.3. Diapositiva')
    esPapel = models.BooleanField('13.4.7.4. Papel')
    esDigital = models.BooleanField('13.4.7.5. Digital')
    esNegativo = models.BooleanField('13.4.7.6. Negativo')
    description  = models.BooleanField('13.4.8. Con mapa ')
    tieneMapa = models.FileField('13.4.8.0.0. Mapa - Archivo', 
                                 upload_to='bibliografia_pie/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneMapa1 = models.FileField('13.4.8.0.1. Mapa - Archivo', 
                                 upload_to='bibliografia_pie/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneMapa2 = models.FileField('13.4.8.0.2. Mapa - Archivo', 
                                 upload_to='bibliografia_pie/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneMapa3 = models.FileField('13.4.8.0.3. Mapa - Archivo', 
                                 upload_to='bibliografia_pie/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneMapa4 = models.FileField('13.4.8.0.4. Mapa - Archivo', 
                                 upload_to='bibliografia_pie/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tipoMapa = models.IntegerField('13.4.8.1. Tipo de mapa', choices = Bibliografia.TIPO_MAPA,blank = True,null = True)
	
    abbr = 'bip'
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = ''




# Material audiovisual     

class MatAudioVisual (models.Model):
	
    def __unicode__(self):
        return '' # '# ' + str(self.id)	

class MatAVYacimiento(MatAudioVisual):

    yacimiento = models.ForeignKey(Yacimiento, related_name='MatAVYacimiento')
    ismatavy = models.BooleanField('31.2. Material audiovisual')
    format = CharField('31.2.1. Formato', null=True, blank=True)
    archive = models.FileField('31.2.2. Material AV - Archivo', upload_to='audiovisual/%Y_%m', null=True, blank=True)
    
    abbr = 'avy'
    
    class Meta:
        verbose_name = 'Material audiovisual'
        verbose_name_plural = ''

class MatAVPiedra(MatAudioVisual):

    piedra = models.ForeignKey(Piedra, related_name='MatAVPiedra')
    ismatavy = models.BooleanField('13.5. Material audiovisual')
    format = CharField('13.5.1. Formato', null=True, blank=True)
    archive = models.FileField('13.5.2. Material AV - Archivo', upload_to='audiovisual/%Y_%m', null=True, blank=True)
    
    abbr = 'avp'

    class Meta:
        verbose_name = 'Material audiovisual'
        verbose_name_plural = ''
    
# Videos 

class Video (models.Model):    
    
    def __unicode__(self):
        return '' # '# ' + str(self.id) 
    
class VideoYacimiento (Video) :

    yacimiento = models.ForeignKey(Yacimiento, related_name='VideoYacimiento')
    isvidyac = models.BooleanField('31.3. Videos')
    anioy = models.IntegerField('31.3.0. Año', blank=True, null=True,default = None)
    formatoy = CharField('31.3.1. Formato',blank = True, null = True)
    tituloy = CharField('31.3.2. Titulo',blank = True, null = True)
    autory = CharField('31.3.3. Autor',blank = True, null = True)    
    instituciony = CharField('31.3.4. Institucion',blank = True, null = True )
    numReferenciayAN = CharField('31.3.5. Nro de referencia', null = True, blank = True)
    isFromAnary = models.BooleanField('31.3.6. ¿Es de ANAR?')
    numCopiaANy = CharField('31.3.6.1. Nro de copia',blank = True, null = True)
    archivoy = models.FileField('31.3.7. Video - Archivo', upload_to='video/%Y_%m', null=True, blank=True)
    
    abbr = 'vdy'
    
    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = ''

class VideoPiedra (Video) :

    piedra = models.ForeignKey(Piedra, related_name='VideoPiedra')
    isvidyac = models.BooleanField('13.6. Videos')
    anioy = models.IntegerField('13.6.0. Año', blank = True, null=True)
    formatoy = CharField('13.6.1. Formato',blank = True, null=True)
    tituloy = CharField('13.6.2. Titulo',blank = True, null=True)
    autory = CharField('13.6.3. Autor',blank = True, null=True, default = None)    
    instituciony = CharField('13.6.4. Institucion',blank = True, null=True)
    numReferenciayAN = CharField('13.6.5 Nro de referencia',blank = True, null = True)
    isFromAnary = models.BooleanField('13.6.6. ¿Es de ANAR?')
    numCopiaPiedraAN = CharField('13.6.6.1. Nro de copia', blank = True, null = True)
    archivoy = models.FileField('13.6.7. Video - Archivo', upload_to='video/%Y_%m', null=True, blank=True)

    abbr = 'vdp'
    
    
    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = ''

# Película

class Pelicula (Video):
    
    def __unicode__(self):
        return '' # '# ' + str(self.id)	

class PeliYacimiento (Pelicula):
    
    yacimiento = models.ForeignKey(Yacimiento, related_name='PeliYacimiento')
    isvidyac = models.BooleanField('31.4. Películas')
    anioy = models.IntegerField('31.4.0. Año',blank = True, null = True)
    formatoy = CharField('31.4.1. Formato',blank = True, null = True)
    tituloy = CharField('31.4.2. Titulo',blank = True, null = True)
    autory = CharField('31.4.3. Autor',blank = True, null = True)    
    instituciony = CharField('31.4.4. Institucion',blank = True, null = True)
    numReferenciayAN = CharField('31.4.5. Nro de referencia',blank = True, null = True)
    isFromAnary = models.BooleanField('31.4.6. ¿Es de ANAR?')
    numCopiayacAN = CharField('31.4.1. Nro de copia', blank = True, null = True)
    archivoy = models.FileField('31.4.7. Video - Archivo', upload_to='video/%Y_%m', null=True, blank=True)
    
    abbr = 'ply'
    
    class Meta:
        verbose_name = 'Película'
        verbose_name_plural = ''

class PeliculaPiedra (Pelicula):

    piedra = models.ForeignKey(Piedra, related_name='PeliculaPiedra')
    isvidyac = models.BooleanField('13.7. Películas')
    anioy = models.IntegerField('13.7.0. Año',blank = True, null = True)
    formatoy = CharField('13.7.1. Formato',blank = True, null = True)
    tituloy = CharField('13.7.2. Titulo',blank = True, null = True)
    autory = CharField('13.7.3. Autor',blank = True, null = True)    
    instituciony = CharField('13.7.4. Institucion',blank = True, null=True)
    numReferenciayAN = CharField('13.7.5. Nro de referencia', blank = True, null = True)
    isFromAnary = models.BooleanField('13.7.6. ¿Es de ANAR?')
    numCopiaPiedraAN = CharField('13.7.6.1. Nro de copia', blank=True, null=True)
    archivoy = models.FileField('13.7.7. Video - Archivo', upload_to='video/%Y_%m', null=True, blank=True)
    
    abbr = 'plp'
    
    class Meta:
        verbose_name = 'Película'
        verbose_name_plural = ''

# Página Web

class PaginaWeb (models.Model):
	
    def __unicode__(self):
        return '' # '# ' + str(self.id)	

class PaginaWebYac (PaginaWeb):

    yacimiento = models.ForeignKey(Yacimiento, related_name='PaginaWebYac')
    tieneWb = models.BooleanField('31.5. Página Web')
    direccionURLy = models.URLField ('31.5.1. URL de página web')
    
    abbr = 'pwy'
    
    class Meta:
        verbose_name = 'Página Web'
        verbose_name_plural = ''

class PaginaWebPiedra (PaginaWeb):

    piedra = models.ForeignKey(Piedra, related_name='PaginaWebPiedra')
    tieneWb = models.BooleanField('13.8. Página Web')
    direccionURLP = models.URLField ('13.8.1. URL de página web')
    
    abbr = 'pwp'
    
    class Meta:
        verbose_name = 'Página Web'
        verbose_name_plural = ''

# Multimedia

class Multimedia (models.Model):

    def __unicode__(self):
        return '' # '# ' + str(self.id)	

class MultimediaYac (Multimedia):

    yacimiento = models.ForeignKey(Yacimiento, related_name='MultimediaYac')
    ismult = models.BooleanField('31.6. Multimedia')
    tecnicaY = CharField('31.6.1. Técnica',null = True, blank = True )
    archivoY = models.FileField('31.6.2. Multimedia - Archivo', upload_to='multimedia/%Y_%m', null=True, blank=True)

    abbr = 'mmy'
    
    class Meta:
        verbose_name = 'Multimedia'
        verbose_name_plural = ''

class MultimediaPiedra (Multimedia):

    piedra = models.ForeignKey(Piedra, related_name='MultimediaPiedra')
    ismult = models.BooleanField('13.9. Multimedia')
    tecnicaP = CharField('13.9.1. Técnica',blank = True, null = True )
    archivoP = models.FileField('13.9.2. Multimedia - Archivo', upload_to='multimedia/%Y_%m', null=True, blank=True)
    abbr = 'mmp'
    
    class Meta:
        verbose_name = 'Multimedia'
        verbose_name_plural = ''

# Obtencion de informacion

class ObtencionInfo (models.Model):

    def __unicode__(self):
        return '' # '# ' + str(self.id)	
	
class ObtInfoYac (ObtencionInfo):

    yacimiento = models.ForeignKey(Yacimiento, related_name='ObtInfoYac')
    isinfo = models.BooleanField('32. Información obtenida por')
    prospeccionY = models.BooleanField('32.1. Prospección sistemática')
    comunicacionY = models.BooleanField('32.2. Comunicación personal')
    nombreY = CharField('32.2.1. Nombre')
    direccionY = CharField('32.2.2. Dirección', blank = True)
    telefonoY = CharField('32.2.3. Telefono/Fax',  blank = True)
    telefonoCelY = CharField('32.2.4. Telefono celular',  blank = True)
    mailY = models.EmailField('32.2.5. Correo electrónico', blank = True)
    paginaWebY = models.URLField('32.2.6. Página Web', blank = True)
    twitterY = CharField('32.2.7. Twitter',  blank = True)
    nombreFacebookY = CharField('32.2.8. Perfil Facebook',  blank = True)
    blogY = models.URLField('32.2.9. Blog', blank = True)
    fechaY = models.CharField('32.2.10. Fecha', blank = True, null= True, max_length=100)
    verificadoY = models.BooleanField('32.2.3. Verificado en el campo')
    
    abbr = 'oiy'
    
    class Meta:
        verbose_name = 'Información obtenida por'
        verbose_name_plural = ''

class ObtInfoPiedra (ObtencionInfo):

    piedra = models.ForeignKey(Piedra, related_name='ObtInfoPiedra')
    isinfo = models.BooleanField('14. Información obtenida por')
    prospeccionP = models.BooleanField('14.1. Prospección sistemática')
    comunicacionP = models.BooleanField('14.2. Comunicación personal')
    nombreP = CharField('14.2.1. Nombre', blank=True)
    direccionP = CharField('14.2.2. Dirección', blank = True)
    telefonoP = CharField('14.2.3. Telefono/Fax',  blank = True)
    telefonoCelP = CharField('14.2.4. Telefono celular',  blank = True)
    mailP = models.EmailField('14.2.5. Correo electrónico', blank = True)
    paginaWebP = models.URLField('14.2.6. Página Web', blank = True)
    twitterP = CharField('14.2.7. Twitter',  blank = True)
    nombreFacebookP = CharField('14.2.8. Perfil Facebook',  blank = True)
    blogP = models.URLField('14.2.9. Blog', blank = True)
    fechaP = models.CharField('14.2.10. Fecha', blank = True, null= True, max_length=100)
    verificadoP = models.BooleanField('14.2.3. Verificado en el campo')
    
    abbr = 'oip'

    class Meta:
        verbose_name = 'Información obtenida por'
        verbose_name_plural = ''
    
        
# Otros valores

class OtrosValores(models.Model):

    def __unicode__(self):
        return '' # '# ' + str(self.id)	

class OtrosValYac(OtrosValores):

    yacimiento = models.ForeignKey(Yacimiento, related_name='OtrosValYac')
    texto = CharField('33. Otros valores del sitio', blank = True)
    abbr = 'ovy'
    
    class Meta:
        verbose_name = 'Otros valores del sitio'
        verbose_name_plural = ''

class OtrosValPiedra(OtrosValores):

    piedra = models.ForeignKey(Piedra, related_name='OtrosValPiedra')
    texto = CharField('15.1. Otros valores de la roca', blank = True)
    abbr = 'ovp'
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = '15. Valores de la Roca'

# Observaciones

class Observaciones(models.Model):
	
    def __unicode__(self):
        return '' # '# ' + str(self.id)	

class ObservacionesYac(Observaciones):

    yacimiento = models.ForeignKey(Yacimiento, related_name='ObservacionesYac')
    textoY = CharField('34.1. Observaciones',)
    
    abbr = 'oya'
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = '34. Observaciones'

class ObservacPiedra(Observaciones):

    piedra = models.ForeignKey(Piedra, related_name='ObservacPiedra')
    textoP = CharField('16.1. Observaciones',)
    
    abbr = 'opi'
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = '16. Observaciones'

# Llenado de la ficha

class LlenadoPor(models.Model):

    def __unicode__(self):
        return '' # '# ' + str(self.id)	

class LlenadoYac(LlenadoPor):    

    yacimiento = models.ForeignKey(Yacimiento, related_name='LlenadoYac')
    nombreY = CharField('35.1. Llenada por: ', blank = True)
    fechaY = models.CharField('35.2. Fecha', blank = True, null= True, max_length=100)
    
    abbr = 'ypy'

    class Meta:
        verbose_name = ''
        verbose_name_plural = '35. Ficha llenada Por'
    
class LlenadoPiedra(LlenadoPor):    

    piedra = models.ForeignKey(Piedra, related_name='LlenadoPiedra')
    nombreP = CharField('17.1. Llenada por: ', blank = True)
    fechaP = models.CharField('17.2. Fecha', blank = True, null= True, max_length=100)
    
    abbr = 'ypp'
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = '17. Ficha llenada por'

# Supervision de la ficha

class SupervisadoPor(models.Model):
	
    def __unicode__(self):
        return '' # '# ' + str(self.id)	

class SupervisadoYac(SupervisadoPor):
    
    yacimiento = models.ForeignKey(Yacimiento, related_name='SupervisadoYac')
    nombreY = CharField('36.1. Supervisada por: ', blank = True)
    fechaY = models.CharField('36.2. Fecha', blank = True, null= True, max_length=100)

    abbr = 'spy'
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = '36. Ficha Supervisada Por'

class SupervisadoPiedra(SupervisadoPor):
    
    piedra = models.ForeignKey(Piedra, related_name='SupervisadoPiedra')
    nombreP = CharField('18.1. Supervisada por: ', blank = True)
    fechaP = models.CharField('18.2. Fecha', blank = True, null= True, max_length=100)
    
    abbr = 'spp'    

    class Meta:
        verbose_name = ''
        verbose_name_plural = '18. Ficha Supervisada Por'
