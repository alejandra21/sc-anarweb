#coding: latin-1
from django.conf.urls import patterns, url
from django.views.generic import TemplateView, DetailView

from joins import views
import anarapp

urlpatterns = patterns('',    
    url(r'^$', views.index, name='index'),
    url(r'^cruce(?P<cruce_id>\d+)$', views.cruces, name='cruces'),
    url(r'^patrimonio$', anarapp.views.patrimonio),
    url(r'^quienes/', TemplateView.as_view(template_name="anarapp/quienes.html"),
	),

)
