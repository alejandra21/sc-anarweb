# Create your views here.
from django.shortcuts import render



def index(request):
    return render(request, 'index.html')

#def imagenes1(request):
#    return render(request, 'imagenes/1.html')

def inicio(request):
    return render(request, 'inicio.html')

def sistema(request):
    return render(request, 'sistema.html')

def inicioen(request):
    return render(request, 'en/inicioen.html')

def quienessomosOrigenytrayectoria(request):
	return render(request, 'quienessomos/origenytrayectoria.html')

def quienessomosAreasdeespecializacion(request):
	return render(request, 'quienessomos/areasdeespecializacion.html')

def quienessomosOrganigrama(request):
    return render(request, 'quienessomos/organigrama.html')

def quienessomosProyectosactuales(request):
	return render(request, 'quienessomos/proyectosactuales.html')

def quienessomosProfesionalesadjuntos(request):
	return render(request, 'quienessomos/profesionalesadjuntos.html')

def patrimoniorupestreNota(request):
	return render(request, 'patrimoniorupestrevenezolano/nota.html')

def patrimoniorupestreLeydeproteccion(request):
	return render(request, 'patrimoniorupestrevenezolano/leydeproteccion.html')

def patrimoniorupestrePinturasrupestres(request):
	return render(request, 'patrimoniorupestrevenezolano/pinturasrupestres.html')

def patrimoniorupestreGeoglifo(request):
	return render(request, 'patrimoniorupestrevenezolano/geoglifo.html')

def patrimoniorupestrePetroglifo(request):
	return render(request, 'patrimoniorupestrevenezolano/petroglifo.html')

def patrimoniorupestreAmoladores(request):
	return render(request, 'patrimoniorupestrevenezolano/amoladores.html')

def patrimoniorupestreMonumentosmegaliticos(request):
	return render(request, 'patrimoniorupestrevenezolano/monumentosmegaliticos.html')

def patrimoniorupestreMicropetroglifos(request):
	return render(request, 'patrimoniorupestrevenezolano/micropetroglifos.html')

def patrimoniorupestrePiedrasycerrosmiticos(request):
	return render(request, 'patrimoniorupestrevenezolano/piedrasycerrosmiticos.html')

def patrimoniorupestreGeoportal(request):
	return render(request, 'patrimoniorupestrevenezolano/geoportal.html')

def programadeeducacionLasmanifestacionesylaescuela(request):
	return render(request, 'programadeeducacion/manifestacionesylaescuela.html')

def programadeeducacionComunidadAcademica(request):
	return render(request, 'programadeeducacion/comunidadacademica.html')

def programadeeducacionConvenios(request):
	return render(request, 'programadeeducacion/convenios.html')

def programadeeducacionMaterialdidactico(request):
	return render(request, 'programadeeducacion/materialdidactico.html')

def productosyserviciosPublicaciones(request):
	return render(request, 'productosyservicios/publicaciones.html')

def productosyserviciosProductos(request):
	return render(request, 'productosyservicios/productos.html')

def productosyserviciosAsesorias(request):
	return render(request, 'productosyservicios/asesorias.html')

def productosyserviciosVisitasguiadas(request):
	return render(request, 'productosyservicios/visitasguiadas.html')

def contacto(request):
	return render(request, 'contacto.html')
