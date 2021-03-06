from django.conf.urls import patterns, url, include

from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

#from AnarWeb.apps.yacimientos import views
from . import views

urlpatterns = patterns('',
    # ex: /polls/
    #url(r'imagenes/1', views.imagenes1, name='1'),
    # Las expresiones regulares agrupan desde la mas pequena hasta la mas grande.
    # por esto, si tienes inicio e iniciosw tienes que poner iniciosw antes.
    url(r'^$', views.index, name='inicio'),
    
    url(r'cruces/', include('joins.urls')),
    url(r'^upload/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),

	# Uncomment the admin/doc line below to enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:        
	url(r'^admin/', include(admin.site.urls)),
    
    url(r'es/inicio-Sw-interactivo', views.inicioswinteractivo, name='inicioswinteractivo'),
    url(r'en/inicio-Sw-interactivo', views.eninicioswinteractivo, name='eninicioswinteractivo'),
    url(r'es/inicio', views.inicio, name='index'),
    url(r'en/inicio', views.en, name='en'),
    
    url(r'es/juegosdidacticos/juegos', views.juegosdidacticosJuegos, name='juegosdidacticos'),
    url(r'es/juegosdidacticos/rueda', views.juegosdidacticosRuedaDidactica, name='ruedadidactica'),
    url(r'es/quienessomos/origen', views.quienessomosOrigenytrayectoria, name='origenytrayectoria'),
    url(r'es/quienessomos/areas', views.quienessomosAreasdeespecializacion, name='areasdeespecializacion'),
    url(r'es/quienessomos/organigrama', views.quienessomosOrganigrama, name='organigrama'),
    url(r'es/quienessomos/proyectos', views.quienessomosProyectosactuales, name='proyectosactuales'),
    url(r'es/quienessomos/adjuntos', views.quienessomosProfesionalesadjuntos, name='profesionalesadjuntos'),
    url(r'es/patrimonio/nota', views.patrimoniorupestreNota, name='nota'),
    url(r'es/patrimonio/ley', views.patrimoniorupestreLeydeproteccion, name='leydeproteccion'),
    url(r'es/patrimonio/pinturas', views.patrimoniorupestrePinturasrupestres, name='pinturasrupestres'),
    url(r'es/patrimonio/geoglifo', views.patrimoniorupestreGeoglifo, name='geoglifo'),
    url(r'es/patrimonio/petroglifo', views.patrimoniorupestrePetroglifo, name='petroglifo'),
    url(r'es/patrimonio/amoladores', views.patrimoniorupestreAmoladores, name='amoladores'),
    url(r'es/patrimonio/monumentos', views.patrimoniorupestreMonumentosmegaliticos, name='monumentosmegaliticos'),
    url(r'es/patrimonio/micropetroglifos', views.patrimoniorupestreMicropetroglifos, name='micropetroglifos'),
    url(r'es/patrimonio/piedrasycerros', views.patrimoniorupestrePiedrasycerrosmiticos, name='piedrasycerrosmiticos'),
    url(r'es/patrimonio/geoportal', views.patrimoniorupestreGeoportal, name='geoportal'),
    url(r'es/educacion/escuela', views.programadeeducacionLasmanifestacionesylaescuela, name='manifestacionesylaescuela'),
    url(r'es/educacion/comunidad', views.programadeeducacionComunidadAcademica, name='comunidadacademica'),
    url(r'es/educacion/convenios', views.programadeeducacionConvenios, name='convenios'),
    url(r'es/educacion/material', views.programadeeducacionMaterialdidactico, name='materialdidactico'),
    url(r'es/educacion/enlacesrelacionados', views.programadeeducacionEnlacesrelacionados, name='enlacesrelacionados'),
    url(r'es/productosyservicios/publicaciones', views.productosyserviciosPublicaciones, name='publicaciones'),
    url(r'es/productosyservicios/productos', views.productosyserviciosProductos, name='productos'),
    url(r'es/productosyservicios/asesorias', views.productosyserviciosAsesorias, name='asesorias'),
    url(r'es/productosyservicios/visitas', views.productosyserviciosVisitasguiadas, name='visitasguiadas'),
    url(r'es/productosyservicios/serviciosinformacion', views.productosyserviciosServiciosinformacion, name='serviciosinformacion'),
    url(r'es/contacto', views.contacto, name='contacto'),
    
    
    
    url(r'en/juegosdidacticos/juegos', views.enjuegosdidacticosJuegos, name='enjuegosdidacticos'),
    url(r'en/juegosdidacticos/rueda', views.enjuegosdidacticosRuedaDidactica, name='enruedadidactica'),
    url(r'en/quienessomos/origen', views.enquienessomosOrigenytrayectoria, name='enorigenytrayectoria'),
    url(r'en/quienessomos/areas', views.enquienessomosAreasdeespecializacion, name='enareasdeespecializacion'),
    url(r'en/quienessomos/organigrama', views.enquienessomosOrganigrama, name='enorganigrama'),
    url(r'en/quienessomos/proyectos', views.enquienessomosProyectosactuales, name='enproyectosactuales'),
    url(r'en/quienessomos/adjuntos', views.enquienessomosProfesionalesadjuntos, name='enprofesionalesadjuntos'),
    url(r'en/patrimonio/nota', views.enpatrimoniorupestreNota, name='ennota'),
    url(r'en/patrimonio/ley', views.enpatrimoniorupestreLeydeproteccion, name='enleydeproteccion'),
    url(r'en/patrimonio/pinturas', views.enpatrimoniorupestrePinturasrupestres, name='enpinturasrupestres'),
    url(r'en/patrimonio/geoglifo', views.enpatrimoniorupestreGeoglifo, name='engeoglifo'),
    url(r'en/patrimonio/petroglifo', views.enpatrimoniorupestrePetroglifo, name='enpetroglifo'),
    url(r'en/patrimonio/amoladores', views.enpatrimoniorupestreAmoladores, name='enamoladores'),
    url(r'en/patrimonio/monumentos', views.enpatrimoniorupestreMonumentosmegaliticos, name='enmonumentosmegaliticos'),
    url(r'en/patrimonio/micropetroglifos', views.enpatrimoniorupestreMicropetroglifos, name='enmicropetroglifos'),
    url(r'en/patrimonio/piedrasycerros', views.enpatrimoniorupestrePiedrasycerrosmiticos, name='enpiedrasycerrosmiticos'),
    url(r'en/patrimonio/geoportal', views.enpatrimoniorupestreGeoportal, name='engeoportal'),
    url(r'en/educacion/escuela', views.enprogramadeeducacionLasmanifestacionesylaescuela, name='enmanifestacionesylaescuela'),
    url(r'en/educacion/comunidad', views.enprogramadeeducacionComunidadAcademica, name='encomunidadacademica'),
    url(r'en/educacion/convenios', views.enprogramadeeducacionConvenios, name='enconvenios'),
    url(r'en/educacion/material', views.enprogramadeeducacionMaterialdidactico, name='enmaterialdidactico'),
    url(r'en/educacion/enlacesrelacionados', views.enprogramadeeducacionEnlacesrelacionados, name='enenlacesrelacionados'),    
    url(r'en/productosyservicios/publicaciones', views.enproductosyserviciosPublicaciones, name='enpublicaciones'),
    url(r'en/productosyservicios/productos', views.enproductosyserviciosProductos, name='enproductos'),
    url(r'en/productosyservicios/asesorias', views.enproductosyserviciosAsesorias, name='enasesorias'),
    url(r'en/productosyservicios/visitas', views.enproductosyserviciosVisitasguiadas, name='envisitasguiadas'),
    url(r'en/productosyservicios/serviciosinformacion', views.enproductosyserviciosServiciosinformacion, name='enserviciosinformacion'),
    url(r'en/contacto', views.encontacto, name='encontacto'),

    url(r'en', views.landing_en, name='landing_en'),
    url(r'', views.landing_es, name='landing_es'),
    )
