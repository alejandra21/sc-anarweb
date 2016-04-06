#coding: latin-1
from django.conf.urls import patterns, url
from django.views.generic import TemplateView, DetailView

from joins import views
import anarapp
import os

urlpatterns = patterns('',    
    url(r'^$', views.index, name='inicio'),
    url(r'cruceAdmin', views.cruceAdmin, name='cruceAdmin'),
    url(r'^(?P<cruce_id>[0-9]+)/$', views.cruces, name='cruces'),
    url(r'consulta', views.consulta, name='consulta'),
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root':os.path.join(os.path.dirname(__file__), 'static')}),


    #url(r'imagenes/1', views.imagenes1 name='1'),
    # url(r'inicio', views.inicio, name='index'),
    #url(r'^$', views.index, name='index'),
    #url(r'^cruce(?P<cruce_id>\d+)$', views.cruces, name='cruces'),
    #url(r'^patrimonio$', anarapp.views.patrimonio),
    #url(r'^quienes/', TemplateView.as_view(template_name="anarapp/quienes.html"),
	#),
    # url(r'quienessomos/origen', views.quienessomosOrigenytrayectoria, name='origenytrayectoria'),
    # url(r'quienessomos/areas', views.quienessomosAreasdeespecializacion, name='areasdeespecializacion'),
    # url(r'quienessomos/proyectos', views.quienessomosProyectosactuales, name='proyectosactuales'),
    # url(r'quienessomos/adjuntos', views.quienessomosProfesionalesadjuntos, name='profesionalesadjuntos'),
    # url(r'patrimonio/nota', views.patrimoniorupestreNota, name='nota'),
    # url(r'patrimonio/ley', views.patrimoniorupestreLeydeproteccion, name='leydeproteccion'),
    # url(r'patrimonio/pinturas', views.patrimoniorupestrePinturasrupestres, name='pinturasrupestres'),
    # url(r'patrimonio/geoglifo', views.patrimoniorupestreGeoglifo, name='geoglifo'),
    # url(r'patrimonio/petroglifo', views.patrimoniorupestrePetroglifo, name='petroglifo'),
    # url(r'patrimonio/amoladores', views.patrimoniorupestreAmoladores, name='amoladores'),
    # url(r'patrimonio/monumentos', views.patrimoniorupestreMonumentosmegaliticos, name='monumentosmegaliticos'),
    # url(r'patrimonio/micropetroglifos', views.patrimoniorupestreMicropetroglifos, name='micropetroglifos'),
    # url(r'patrimonio/piedrasycerros', views.patrimoniorupestrePiedrasycerrosmiticos, name='piedrasycerrosmiticos'),
    # url(r'patrimonio/geoportal', views.patrimoniorupestreGeoportal, name='geoportal'),
    # url(r'educacion/escuela', views.programadeeducacionLasmanifestacionesylaescuela, name='manifestacionesylaescuela'),
    # url(r'educacion/comunidad', views.programadeeducacionComunidadAcademica, name='comunidadacademica'),
    # url(r'educacion/convenios', views.programadeeducacionConvenios, name='convenios'),
    # url(r'educacion/material', views.programadeeducacionMaterialdidactico, name='materialdidactico'),
    # url(r'productosyservicios/publicaciones', views.productosyserviciosPublicaciones, name='publicaciones'),
    # url(r'productosyservicios/productos', views.productosyserviciosProductos, name='productos'),
    # url(r'productosyservicios/asesorias', views.productosyserviciosAsesorias, name='asesorias'),
    # url(r'productosyservicios/visitas', views.productosyserviciosVisitasguiadas, name='visitasguiadas'),
    # url(r'contacto', views.contacto, name='contacto'),

)
