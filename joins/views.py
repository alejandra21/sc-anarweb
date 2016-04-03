# Create your views here.
from django.shortcuts import render
from django.db.models import Q
from anarapp.models import Estado, Piedra, Yacimiento, ManifestacionYacimiento,FotografiaYac
from joins.forms import CrucesYYForm


def index(request):

	forma = CrucesYYForm
	return render(request, 'sistema.html',{'forma':forma})

# def cruces(request,cruce_id):
# 	entrada = "joins/cruce"+str(cruce_id)+".html"
# 	return render(request,entrada)

def consulta(request):
	# Se realiza la consula:
	estadoElegido = request.GET['estado']
	nombreElegido = request.GET['nombre']
	manifestacionElegida = request.GET['manifestacion']

	forma = CrucesYYForm
	yacimiento=""
	manifestacion=""
	if(manifestacionElegida!="---"):
	 	
	 	# Se seleccionan las manifestaciones correspondientes
		if(manifestacionElegida=="Pinturas Rupestres"):
			manifestacion = ManifestacionYacimiento.objects.filter(esPintura=True)

		elif(manifestacionElegida=="Cerros y Piedras Miticas Naturales"):

			manifestacion = ManifestacionYacimiento.objects.filter(
				Q(esPiedraMiticaNatural=True)| Q(esCerroMiticoNatural=True))
			
		elif(manifestacionElegida=='Amoladores,Cupula,Puntos Acoplados'):
			manifestacion = ManifestacionYacimiento.objects.filter(
				Q(esAmolador=True)|Q(esCupulas=True)|Q(esPuntosAcoplados=True) )
			
		elif(manifestacionElegida=="Geoglifo"):
			manifestacion = ManifestacionYacimiento.objects.filter(esGeoglifo=True)

		elif(manifestacionElegida=="Micropentoglifos"):
			# Hay que agregar este atributo en el modelo de datos
			manifestacion = \
			ManifestacionYacimiento.objects.filter(esMonumentosMegaliticos=True)

		elif(manifestacionElegida=="Monumentos megaliticos"):
			manifestacion = \
			ManifestacionYacimiento.objects.filter(esMonumentosMegaliticos=True)

		elif(manifestacionElegida=="Petroglifos"):
			manifestacion = ManifestacionYacimiento.objects.filter(esPetroglifo=True)

		########################################################################	

		if(nombreElegido=="" and estadoElegido=="---"):
			pass

		elif(nombreElegido!="" and estadoElegido=="---"):

			manifestacion =\
			 manifestacion.filter(yacimiento__nombre__icontains=nombreElegido)

		elif(nombreElegido=="" and estadoElegido!="---"):

			manifestacion=\
			manifestacion.filter(yacimiento__estado__nombre=estadoElegido)

		elif(nombreElegido!="" and estadoElegido!="---"):

			# Conculta encadenada
			manifestacion = \
			manifestacion.filter(yacimiento__nombre__icontains=nombreElegido,
				yacimiento__estado__nombre=estadoElegido)

	else:

		if(nombreElegido=="" and estadoElegido=="---"):
			# Se supone que tiene que redireccionar a un .html
			return render(request, 'sistema.html',{'forma':forma})
			#yacimiento=Yacimiento.objects.filter(estado__nombre__exact=estadoElegido)

		elif(nombreElegido!="" and estadoElegido=="---"):

			yacimiento=Yacimiento.objects.filter(nombre__icontains=nombreElegido)

		elif(nombreElegido=="" and estadoElegido!="---"):

			yacimiento=Yacimiento.objects.filter(estado__nombre__exact=estadoElegido)

		elif(nombreElegido!="" and estadoElegido!="---"):

			# Conculta encadenada
			yacimiento = Yacimiento.objects.filter(nombre__icontains=nombreElegido,
				estado__nombre__exact=estadoElegido)

	

	return render(request,'joins/salidaConsulta.html', 
		{'yacimiento':yacimiento,
		'manifestacion':manifestacion,'forma':forma,
		'estadoElegido':estadoElegido,
		'manifestacionElegida':manifestacionElegida,
		'nombreElegido':nombreElegido})


	


# def imagenes1(request):
#     return render(request, 'imagenes/1.html')

# def inicio(request):
#     return render(request, 'inicio.html')

# def quienessomosOrigenytrayectoria(request):
# 	return render(request, 'quienessomos/origenytrayectoria.html')

# def quienessomosAreasdeespecializacion(request):
# 	return render(request, 'quienessomos/areasdeespecializacion.html')

# def quienessomosProyectosactuales(request):
# 	return render(request, 'quienessomos/proyectosactuales.html')

# def quienessomosProfesionalesadjuntos(request):
# 	return render(request, 'quienessomos/profesionalesadjuntos.html')

# def patrimoniorupestreNota(request):
# 	return render(request, 'patrimoniorupestrevenezolano/nota.html')

# def patrimoniorupestreLeydeproteccion(request):
# 	return render(request, 'patrimoniorupestrevenezolano/leydeproteccion.html')

# def patrimoniorupestrePinturasrupestres(request):
# 	return render(request, 'patrimoniorupestrevenezolano/pinturasrupestres.html')

# def patrimoniorupestreGeoglifo(request):
# 	return render(request, 'patrimoniorupestrevenezolano/geoglifo.html')

# def patrimoniorupestrePetroglifo(request):
# 	return render(request, 'patrimoniorupestrevenezolano/petroglifo.html')

# def patrimoniorupestreAmoladores(request):
# 	return render(request, 'patrimoniorupestrevenezolano/amoladores.html')

# def patrimoniorupestreMonumentosmegaliticos(request):
# 	return render(request, 'patrimoniorupestrevenezolano/monumentosmegaliticos.html')

# def patrimoniorupestreMicropetroglifos(request):
# 	return render(request, 'patrimoniorupestrevenezolano/micropetroglifos.html')

# def patrimoniorupestrePiedrasycerrosmiticos(request):
# 	return render(request, 'patrimoniorupestrevenezolano/piedrasycerrosmiticos.html')

# def patrimoniorupestreGeoportal(request):
# 	return render(request, 'patrimoniorupestrevenezolano/geoportal.html')

# def programadeeducacionLasmanifestacionesylaescuela(request):
# 	return render(request, 'programadeeducacion/manifestacionesylaescuela.html')

# def programadeeducacionComunidadAcademica(request):
# 	return render(request, 'programadeeducacion/comunidadacademica.html')

# def programadeeducacionConvenios(request):
# 	return render(request, 'programadeeducacion/convenios.html')

# def programadeeducacionMaterialdidactico(request):
# 	return render(request, 'programadeeducacion/materialdidactico.html')

# def productosyserviciosPublicaciones(request):
# 	return render(request, 'productosyservicios/publicaciones.html')

# def productosyserviciosProductos(request):
# 	return render(request, 'productosyservicios/productos.html')

# def productosyserviciosAsesorias(request):
# 	return render(request, 'productosyservicios/asesorias.html')

# def productosyserviciosVisitasguiadas(request):
# 	return render(request, 'productosyservicios/visitasguiadas.html')

# def contacto(request):
# 	return render(request, 'contacto.html')
