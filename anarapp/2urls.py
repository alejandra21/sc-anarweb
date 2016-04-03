from django.conf.urls import patterns, include, url
from haystack.views import SearchView,search_view_factory
from haystack.forms import SearchForm
from anarapp.forms import BasicForm, AdvancedForm, PiedraForm
from haystack.query import SearchQuerySet
from anarapp import views
from django.views.generic import TemplateView, DetailView
from anarapp.models import Yacimiento, Piedra

yacimiento = SearchQuerySet().models(Yacimiento)
piedra = SearchQuerySet().models(Piedra)

urlpatterns = patterns('',
    # url(r'^$', views.index, name='index'),
	# url(r'^results/$', views.results, name='results'),

   	url(r'^$', SearchView(
		form_class=BasicForm,
		template='anarapp/index.html'),
	),

	url(r'^quienes/', TemplateView.as_view(template_name="anarapp/quienes.html"),
	),

	url(r'^results/', SearchView(
        template='anarapp/results.html',
        searchqueryset=SearchQuerySet(),
        form_class=AdvancedForm,
		results_per_page=10),
		name='results'
	),
	
   	url(r'^advanced/$', SearchView(
   		searchqueryset=SearchQuerySet(),
		form_class=AdvancedForm,
		template='anarapp/advanced.html'),
	),
	
    url(r'^yacimiento/(?P<pk>\d+)$', views.yacimiento , name='detail'),
    url(r'^piedra/(?P<pk>\d+)$', views.piedra , name='piedra'),

   	url(r'^piedras/$', SearchView(
        searchqueryset=piedra,
		form_class=PiedraForm,
		template='anarapp/piedras.html'),
		name='piedras'
	),

     url(r'^patrimonio$', views.patrimonio),


)
