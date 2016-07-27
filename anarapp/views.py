 #Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response



def index(request):
    return render(request, 'index.html')

def inicio(request):
    return render(request, 'inicio.html')

def sistema(request):
    return render(request, 'sistema.html')

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

def juegos(request):
	return render(request, 'juegosdidacticos/juegos.html')

def ruedadidactica(request):
	return render(request, 'juegosdidacticos/rueda.html')
	
	

def en(request):
	return render(request, 'en/inicio.html')

def enquienessomosOrigenytrayectoria(request):
	return render(request, 'en/quienessomos/origenytrayectoria.html')

def enquienessomosAreasdeespecializacion(request):
	return render(request, 'en/quienessomos/areasdeespecializacion.html')
	
def enquienessomosOrganigrama(request):
    return render(request, 'en/quienessomos/organigrama.html')	

def enquienessomosProyectosactuales(request):
	return render(request, 'en/quienessomos/proyectosactuales.html')

def enquienessomosProfesionalesadjuntos(request):
	return render(request, 'en/quienessomos/profesionalesadjuntos.html')

def enpatrimoniorupestreNota(request):
	return render(request, 'en/patrimoniorupestrevenezolano/nota.html')

def enpatrimoniorupestreLeydeproteccion(request):
	return render(request, 'en/patrimoniorupestrevenezolano/leydeproteccion.html')

def enpatrimoniorupestrePinturasrupestres(request):
	return render(request, 'en/patrimoniorupestrevenezolano/pinturasrupestres.html')

def enpatrimoniorupestreGeoglifo(request):
	return render(request, 'en/patrimoniorupestrevenezolano/geoglifo.html')

def enpatrimoniorupestrePetroglifo(request):
	return render(request, 'en/patrimoniorupestrevenezolano/petroglifo.html')

def enpatrimoniorupestreAmoladores(request):
	return render(request, 'en/patrimoniorupestrevenezolano/amoladores.html')

def enpatrimoniorupestreMonumentosmegaliticos(request):
	return render(request, 'en/patrimoniorupestrevenezolano/monumentosmegaliticos.html')

def enpatrimoniorupestreMicropetroglifos(request):
	return render(request, 'en/patrimoniorupestrevenezolano/micropetroglifos.html')

def enpatrimoniorupestrePiedrasycerrosmiticos(request):
	return render(request, 'en/patrimoniorupestrevenezolano/piedrasycerrosmiticos.html')

def enpatrimoniorupestreGeoportal(request):
	return render(request, 'en/patrimoniorupestrevenezolano/geoportal.html')

def enprogramadeeducacionLasmanifestacionesylaescuela(request):
	return render(request, 'en/programadeeducacion/manifestacionesylaescuela.html')

def enprogramadeeducacionComunidadAcademica(request):
	return render(request, 'en/programadeeducacion/comunidadacademica.html')

def enprogramadeeducacionConvenios(request):
	return render(request, 'en/programadeeducacion/convenios.html')

def enprogramadeeducacionMaterialdidactico(request):
	return render(request, 'en/programadeeducacion/materialdidactico.html')

def enproductosyserviciosPublicaciones(request):
	return render(request, 'en/productosyservicios/publicaciones.html')

def enproductosyserviciosProductos(request):
	return render(request, 'en/productosyservicios/productos.html')

def enproductosyserviciosAsesorias(request):
	return render(request, 'en/productosyservicios/asesorias.html')

def enproductosyserviciosVisitasguiadas(request):
	return render(request, 'en/productosyservicios/visitasguiadas.html')

def encontacto(request):
	return render(request, 'en/contacto.html')
