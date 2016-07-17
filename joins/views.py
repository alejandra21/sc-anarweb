# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render
from django.db.models import Q
from anarapp.models import Estado, Piedra, Yacimiento, \
							ManifestacionYacimiento,FotografiaYac, \
							Coordenadas,ConstitucionYacimiento,UbicacionYacimiento,\
							CaracSurcoPetroglifo,DescColores,MaterialYacimiento,\
							ManifestacionesAsociadas,TipoYacimiento,CaracDeLaPintura,\
							TecnicaParaMicroPetro,EstadoConserYac
from joins.forms import CrucesYYForm, CrucesYYFormAdmin



def index(request):

	return render(request, 'inicio-Sw-interactivo.html')

def cruceUsuario(request):

	forma = CrucesYYForm
	return render(request, 'sistema.html',{'forma':forma})

def tiposCruceAdmin(request):
	return render(request, 'tipo_consultaAdmin.html')

def consultaYacYac(request):
	form = CrucesYYFormAdmin
	return render(request, 'joins/yacimiento_yacimiento.html',{'form':form})

def consultaYacRoc(request):
	form = CrucesYYFormAdmin
	return render(request, 'joins/yacimiento_roca.html',{'form':form})

def consultaRocRoc(request):
	form = CrucesYYFormAdmin
	return render(request, 'joins/roca_roca.html',{'form':form})

def cruceAdmin(request):
	form = CrucesYYFormAdmin
	return render(request,'joins/index.html',{'form':form})

def cruces(request,cruce_id):
	entrada = "joins/cruce"+str(cruce_id)+".html"

	# print(cruce_id == "1")
	if (cruce_id == "1"):
		estado = request.GET['estado']

		if (estado != "Todos"):
			results=Yacimiento.objects.filter(estado__nombre__exact=estado)
		else:
			results = Yacimiento.objects.all()

		total = len(results)
		return render(request,entrada,{'total':total,'results':results,'estado':estado})

	elif (cruce_id in {"2","3","4","5","6","7","8"} ):

		codigo = request.GET['codigo']
		yacimiento=Yacimiento.objects.filter(codigo=codigo)
		return render(request,entrada,{'yacimiento':yacimiento,'codigo':codigo})

	elif (cruce_id == "9"):
		estado = request.GET['estado']
		results = ManifestacionYacimiento.objects.all()

		if (results):
			yacimiento = results.filter(Q(esMenhires=True)|Q(esCerroConDolmen=True))

			if (estado != "Todos"):
				yacimientoResult = yacimiento.filter(yacimiento__estado__nombre=estado)
			else:
				yacimientoResult = yacimiento

		else:
			yacimientoResult = ""

		return render(request,entrada,{'yacimiento':yacimientoResult,'estado':estado})

	elif (cruce_id == "10"):
		# Falta implementar
		listaYacimientos = []
		estado = request.GET['estado']

		if (estado != "Todos"):
			yacimiento = Yacimiento.objects.filter(estado__nombre__exact=estado)
		else:
			yacimiento = Yacimiento.objects.all()

		for y in yacimiento:

			nroPiedras = ConstitucionYacimiento.objects.filter(yacimiento__id = y.id)
			piedras = Piedra.objects.filter(yacimiento__id = y.id)
			listaYacimientos += [{'yacimiento':y,'nroPiedrasTrabajadas':nroPiedras,
								'nroPiedras': len(piedras)}]
			
		return render(request,entrada,{'listaYacimientos':listaYacimientos,'estado':estado})

	elif (cruce_id == "11"):
		# Falta implementar
		estado = request.GET['estado']
		codigo = request.GET['codigo']

		if (estado != "Todos"):
			manifestacion = \
			ManifestacionYacimiento.objects.filter(Q(yacimiento__estado__nombre=estado)|
				Q(yacimiento__codigo=codigo))

		else:

			if (codigo!=""):
				manifestacion = \
				ManifestacionYacimiento.objects.filter(yacimiento__codigo=codigo)

			else:
				manifestacion = \
				ManifestacionYacimiento.objects.all()

		geoglifo = manifestacion.filter(esGeoglifo=True)
		pinturasRupestres = manifestacion.filter(esPintura=True)
		micropetroglifos = manifestacion.filter(esMicroPetroglifo=True)
		petroglifo = manifestacion.filter(esPetroglifo = True)
		petroglifoPintado = manifestacion.filter(esPetroglifoPintado = True)
		PiedraMiticaNatural = manifestacion.filter(esPiedraMiticaNatural=True)
		CerroMiticoNatural = manifestacion.filter(esCerroMiticoNatural=True)
		Batea = manifestacion.filter(esBatea=True)
		Menhires = manifestacion.filter(esMenhires=True)
		Amoladores = manifestacion.filter(esAmolador=True)
		PuntosAcoplados = manifestacion.filter(esPuntosAcoplados=True)
		Cupula = manifestacion.filter(esCupulas = True)

		return render(request,entrada,{'estado':estado,'codigo':codigo,
			'geoglifo':geoglifo,'pinturasRupestres':pinturasRupestres,
			'micropetroglifos':micropetroglifos,'petroglifo':petroglifo,
			'petroglifoPintado': petroglifoPintado,'PiedraMiticaNatural':PiedraMiticaNatural,
			'CerroMiticoNatural':CerroMiticoNatural,'Batea':Batea,'Menhires':Menhires,
			'Amoladores':Amoladores,'PuntosAcoplados':PuntosAcoplados,'Cupula':Cupula})

	elif (cruce_id == "12"):

		ubicacion = request.GET['ubicacion']
		estado = request.GET['estado']

		if (ubicacion == "Cerro"):
			elementos = UbicacionYacimiento.objects.filter(enCerro=True)

		elif (ubicacion == "Cima"):
			elementos = UbicacionYacimiento.objects.filter(enCerroCima=True)

		elif (ubicacion == "Ladera"):
			elementos = UbicacionYacimiento.objects.filter(enCerroLadera=True)

		elif (ubicacion == "Pie de montana"):
			elementos = UbicacionYacimiento.objects.filter(enCerroPieDeMonte=True)

		elif (ubicacion == "Barranco"):
			elementos = UbicacionYacimiento.objects.filter(enCerroBarranco=True)

		elif (ubicacion == "Acantilado"):
			elementos = UbicacionYacimiento.objects.filter(enCerroAcantilado=True)

		elif (ubicacion == "Valle"):
			elementos = UbicacionYacimiento.objects.filter(enValle=True)

		elif (ubicacion == "Rio"):
			elementos = UbicacionYacimiento.objects.filter(enRio=True)

		elif (ubicacion == "Lecho"):
			elementos = UbicacionYacimiento.objects.filter(enRioLecho=True)

		elif (ubicacion == "Margen derecha"):
			elementos = UbicacionYacimiento.objects.filter(enRioMargenDerecha=True)

		elif (ubicacion == "Margen izquierda"):
			elementos = UbicacionYacimiento.objects.filter(enRioMargenIzquierda=True)

		elif (ubicacion == "Isla"):
			elementos = UbicacionYacimiento.objects.filter(enRioIsla=True)

		elif (ubicacion == "Raudal"):
			elementos = UbicacionYacimiento.objects.filter(enRioRaudal=True)

		elif (ubicacion == "Costa"):
			elementos = UbicacionYacimiento.objects.filter(enRioCosta=True)

		if (estado != "Todos"):
			elementos = elementos.filter(yacimiento__estado__nombre=estado)

		else:
			pass

		return render(request,entrada,{'listaManifestaciones':elementos,'ubicacion':ubicacion})
	
	elif (cruce_id == "14"):
		caracteristica = request.GET['caracteristicaSurco']
		listaYacimientos = []

		if (caracteristica == "Base redonda"):
			caracPetroglifo = CaracSurcoPetroglifo.objects.filter(esBase=True)

		elif (caracteristica == "Base aguda"):
			caracPetroglifo = CaracSurcoPetroglifo.objects.filter(esBaseAguda=True)

		else :
			caracPetroglifo = CaracSurcoPetroglifo.objects.filter(esBaseAguda=True)


		petroglifo = ManifestacionYacimiento.objects.filter(esPetroglifo = True)

		for c in caracPetroglifo:

			objetoAgregar = petroglifo.filter(yacimiento__id=c.yacimiento.id)

			if (len(objetoAgregar)!=0):

				for objeto in objetoAgregar:
					listaYacimientos += [{'nombre':objeto.yacimiento.nombre,'id':objeto.yacimiento.id,
										'estado':objeto.yacimiento.estado.nombre,'codigo':objeto.yacimiento.id}]
					

		total =  len(listaYacimientos)

		return render(request,entrada,{'listaYacimientos':listaYacimientos,'total':total})


	elif (cruce_id == "15"):

		estado = request.GET['estado']
		surco = request.GET['carasurcopetrotipo']
		listaYacimientos = []
		caracPetroglifo = []

		if (estado != "Todos"):
			petroglifo = ManifestacionYacimiento.objects.filter(esPetroglifo=True,yacimiento__estado__nombre=estado)

		else:
			petroglifo = ManifestacionYacimiento.objects.filter(esPetroglifo=True)

		for p in petroglifo:

			if (surco == "Bajo relieve lineal"):
				caracPetroglifo = CaracSurcoPetroglifo.objects.filter(esBajoRelieveLineal=True,yacimiento__id=p.yacimiento.id)

			elif (surco == "Bajo relieve planar"):
				caracPetroglifo = CaracSurcoPetroglifo.objects.filter(esBajoRelievePlanar=True,yacimiento__id=p.yacimiento.id)

			elif (surco == "Bajo relieve planar y lineal"):
				caracPetroglifo = CaracSurcoPetroglifo.objects.filter(esBajoRelieveLineal=True,esBajoRelievePlanar=True,yacimiento__id=p.yacimiento.id)

			elif (surco == "Alto relieve lineal"):
				caracPetroglifo = CaracSurcoPetroglifo.objects.filter(esAltoRelieveLineal=True,yacimiento__id=p.yacimiento.id)

			elif (surco == "Alto relieve planar"):
				caracPetroglifo = CaracSurcoPetroglifo.objects.filter(esAltoRelievePlanar=True,yacimiento__id=p.yacimiento.id)

			if (len(caracPetroglifo)!=0):

				for yac in caracPetroglifo:
					listaYacimientos += [{'nombre':yac.yacimiento.nombre,
										'estado':yac.yacimiento.estado.nombre,'codigo':yac.yacimiento.id}]

		total =  len(listaYacimientos)
		return render(request,entrada,{'listaYacimientos':listaYacimientos,'total':total,'surco':surco,'estado':estado})

	elif (cruce_id=="16"):

		estado = request.GET['estado']
		pinturas = request.GET['tipoPintura']
		yacPintura = []
		listaResultado = []

		pinturasRupestres =  ManifestacionYacimiento.objects.filter(esPintura=True)

		if (estado != "Todos"):

			pinturasRupestres =  pinturasRupestres.filter(yacimiento__estado__nombre=estado)

		if (pinturas == "---"):

			for y in pinturasRupestres:
				listaResultado += [{'yacimiento':y}]

		else:

			if (pinturas in {'Pintura positiva negra','Pintura positiva blanca',\
							'Pintura positiva amarilla','Pintura positiva roja',\
							'Pintura positiva dos rojos','Pintura positiva tres rojos'}):

				yacPintura = DescColores.objects.filter(esPositiva=True)

			elif (pinturas in {'Pintura negativa negra','Pintura negativa blanca',\
								'Pintura negativa amarilla','Pintura negativa roja',\
								'Pintura negativa dos rojos','Pintura negativa tres rojos'}):

				yacPintura = DescColores.objects.filter(esNegativa=True)

		for y in yacPintura:

			result = pinturasRupestres.filter(yacimiento__id=y.yacimiento.id)
			if (len(result)!=0):
				for objeto in result:
					listaResultado += [{'yacimiento':objeto}]

		total = len(listaResultado)

		return render(request,entrada,{'total':total,'tipo':pinturas,'listaResultado':listaResultado})

	elif (cruce_id=="17"):

		caracteristica = request.GET['carasurcopetrotipo2']
		listaResultado = []
		caractYac = ""
	
		petroglifo = ManifestacionYacimiento.objects.filter(esPetroglifo=True)

		if (caracteristica == "Areas interlineales pulidas"):
			caractYac = CaracSurcoPetroglifo.objects.filter(esAreaInterlinealPulida=True)

		elif (caracteristica == "Areas interlineales rebajadas"):
			caractYac = CaracSurcoPetroglifo.objects.filter(esAreaInterlinealRebajada=True)

		elif (caracteristica == "Grabados superpuestos"):
			caractYac = CaracSurcoPetroglifo.objects.filter(esGrabadoSuperpuesto=True)

		elif (caracteristica == "Grabados rebajados"):
			caractYac = CaracSurcoPetroglifo.objects.filter(esGrabadoRebajado=True)

		for result in caractYac:
			resultadoBusq = petroglifo.filter(yacimiento__id=result.yacimiento.id)  

			if (len(resultadoBusq)!=0):
				for resultado in resultadoBusq:
					listaResultado += [{'result':resultado}]

		return render(request,entrada,{'listaResultado':listaResultado,'tipo':caracteristica})

	elif (cruce_id=="18"):
		estado = request.GET['estado']
		material = request.GET['material']
		yacPetroglifo = ""
		listaResultado = []

		petroglifo = ManifestacionYacimiento.objects.filter(esPetroglifo=True)

		if (estado != "Todos"):

			petroglifo =  petroglifo.filter(yacimiento__estado__nombre=estado)

		if (material == "---"):
			for y in petroglifo:
				listaResultado += [{'petroglifo':y}]

		if (material != "---"):

			if (material == "Roca ignea"):
				yacPetroglifo = MaterialYacimiento.objects.filter(esIgnea=True)

			elif (material == "Roca metamorfica"):
				yacPetroglifo = MaterialYacimiento.objects.filter(esMetamor=True)

			elif (material == "Roca sedimentaria"):
				yacPetroglifo = MaterialYacimiento.objects.filter(esSedimentaria=True)


		for y in yacPetroglifo:

			result = petroglifo.filter(yacimiento__id=y.yacimiento.id)

			for objeto in result:
				listaResultado += [{'petroglifo':objeto}]

		return render(request,entrada,{'listaResultado':listaResultado,'estado':estado,'tipo':material})


	elif (cruce_id=="20"):

		estado = request.GET['estado']
		manifestacion = request.GET['manifAsociadas']

		if (manifestacion == "Litica"):
			yacimientoResult = ManifestacionesAsociadas.objects.filter(esLitica=True)

		elif (manifestacion == "Ceramica"):
			yacimientoResult = ManifestacionesAsociadas.objects.filter(esCeramica=True)

		elif (manifestacion == "Oseo"):
			yacimientoResult = ManifestacionesAsociadas.objects.filter(esOseo=True)

		elif (manifestacion == "Concha"):
			yacimientoResult = ManifestacionesAsociadas.objects.filter(esConcha=True)

		elif (manifestacion == "Carbon no superficial"):
			yacimientoResult = ManifestacionesAsociadas.objects.filter(esCarbon=True)

		elif (manifestacion == "Mitos"):
			yacimientoResult = ManifestacionesAsociadas.objects.filter(esMito=True)

		elif (manifestacion == "Cementerios"):
			yacimientoResult = ManifestacionesAsociadas.objects.filter(esCementerio=True)

		elif (manifestacion == "Monticulos"):
			yacimientoResult = ManifestacionesAsociadas.objects.filter(esMonticulo=True)

		if (estado != "Todos"):
			yacimientoResult = yacimientoResult.filter(yacimiento__estado__nombre=estado)

		return render(request,entrada,{'yacimiento':yacimientoResult,'manifestacion':manifestacion})

	elif (cruce_id=="21"):

		ubicacion = request.GET['ubicacion']
		caracteristica = request.GET['carasurcopetrotipo3']

		listaResultado = []

		if (ubicacion != "---"):

			if (ubicacion == "Cerro"):
				elementos = UbicacionYacimiento.objects.filter(enCerro=True)

			elif (ubicacion == "Cima"):
				elementos = UbicacionYacimiento.objects.filter(enCerroCima=True)

			elif (ubicacion == "Ladera"):
				elementos = UbicacionYacimiento.objects.filter(enCerroLadera=True)

			elif (ubicacion == "Pie de montana"):
				elementos = UbicacionYacimiento.objects.filter(enCerroPieDeMonte=True)

			elif (ubicacion == "Barranco"):
				elementos = UbicacionYacimiento.objects.filter(enCerroBarranco=True)

			elif (ubicacion == "Acantilado"):
				elementos = UbicacionYacimiento.objects.filter(enCerroAcantilado=True)

			elif (ubicacion == "Valle"):
				elementos = UbicacionYacimiento.objects.filter(enValle=True)

			elif (ubicacion == "Rio"):
				elementos = UbicacionYacimiento.objects.filter(enRio=True)

			elif (ubicacion == "Lecho"):
				elementos = UbicacionYacimiento.objects.filter(enRioLecho=True)

			elif (ubicacion == "Margen derecha"):
				elementos = UbicacionYacimiento.objects.filter(enRioMargenDerecha=True)

			elif (ubicacion == "Margen izquierda"):
				elementos = UbicacionYacimiento.objects.filter(enRioMargenIzquierda=True)

			elif (ubicacion == "Isla"):
				elementos = UbicacionYacimiento.objects.filter(enRioIsla=True)

			elif (ubicacion == "Raudal"):
				elementos = UbicacionYacimiento.objects.filter(enRioRaudal=True)

			elif (ubicacion == "Costa"):
				elementos = UbicacionYacimiento.objects.filter(enRioCosta=True)

			if (caracteristica == "---"):

				for y in elementos:
					listaResultado += [{'result':y}]

		if (caracteristica != "---"):

			if (caracteristica == "Base redonda"):
				elementosCar = CaracSurcoPetroglifo.objects.filter(esBaseRedonda=True)

			elif (caracteristica == "Base aguda"):
				elementosCar = CaracSurcoPetroglifo.objects.filter(esBaseAguda=True)

			elif (caracteristica == "Base relieve lineal"):
				elementosCar = CaracSurcoPetroglifo.objects.filter(esBajoRelieveLineal=True)

			elif (caracteristica == "Base relieve planar"):
				elementosCar = CaracSurcoPetroglifo.objects.filter(esBajoRelievePlanar=True)

			elif (caracteristica == "Alto relieve planar"):
				elementosCar = CaracSurcoPetroglifo.objects.filter(esAltoRelievePlanar=True)

			elif (caracteristica == "Alto relieve lineal"):
				elementosCar = CaracSurcoPetroglifo.objects.filter(esAltoRelieveLineal=True)


			if (ubicacion == "---"):
				for y in elementosCar:
					listaResultado += [{'result':y}]

			else:
				for result in elementos:
					resultadoBusq = elementosCar.filter(yacimiento__id=result.yacimiento.id)

					for elem in resultadoBusq:
						listaResultado += [{'result':elem}]


		return render(request,entrada,{'listaResultado':listaResultado,'ubicacion':ubicacion})

	elif (cruce_id == "22"):
		ubicacion = request.GET['ubicacion2']
		clasificacion = request.GET['clasificacion']

		elementos = ""
		listaResultados = []

		if (ubicacion != "---"):

			if (ubicacion == "Abrigo"):
				elementos = TipoYacimiento.objects.filter(esAbrigo=True)

			elif (ubicacion == "Cueva"):
				elementos = TipoYacimiento.objects.filter(esCueva=True)

			elif (ubicacion == "Cueva de recubrimiento"):
				elementos = TipoYacimiento.objects.filter(esCuevadeRec=True)

			if (clasificacion == "---"):
				for elem in elementos:
					listaResultados += [{'result':elem}]

		if (clasificacion != "---"):

			if (clasificacion == "Linea sencilla"):

				elementosCar = CaracDeLaPintura.objects.filter(esLineaSencilla=True)

			elif (clasificacion == "Linea compuesta"):
				elementosCar = CaracDeLaPintura.objects.filter(esLineaCompuesta=True)

			elif (clasificacion == "Figura rellena"):
				elementosCar = CaracDeLaPintura.objects.filter(esFiguraRellena=True)

			elif (clasificacion == "Impresion de manos positivo"):
				elementosCar = CaracDeLaPintura.objects.filter(esImpresionDeManosPositivo=True)

			elif (clasificacion == "Impresion de manos negativo"):
				elementosCar = CaracDeLaPintura.objects.filter(esImpresionDeManosNegativo=True)

			if (ubicacion == "---"):
				for elem in elementosCar:
					listaResultados += [{'result':elem}]

			else:
				for result in elementos:
					resultadoBusq = elementosCar.filter(yacimiento__id=result.yacimiento.id)

					for elem in resultadoBusq:
						listaResultados += [{'result':elem}]


		return render(request,entrada,{'listaResultados':listaResultados,'ubicacion':ubicacion})

	elif (cruce_id == "23"):

		caracteristica = request.GET['surco']
		listaResultados = []

		if (caracteristica == "Abrasion"):
			elementos = TecnicaParaMicroPetro.objects.filter(Q(esAbrasion=True)|\
															Q(esAbrasionPiedra=True)|\
															Q(esAbrasionArena=True))
			
		elif (caracteristica == "Percusion"):
			elementos = TecnicaParaMicroPetro.objects.filter(Q(esGrabadoPercusion=True)|\
															Q(esGrabadoPercusionDirecta=True)|\
															Q(esGrabadoPercusionIndirecta=True))
		for elem in elementos:
			listaResultados += [{'result':elem}]

		return render(request,entrada,{'listaResultados':listaResultados,'surco':caracteristica})

	elif (cruce_id == "24"):

		material = request.GET['material']
		conservacion = request.GET['estadoConservacion']
		listaResultados = []


		if (material != "---"):

			if (material == "Roca ignea"):
				yacPetroglifo = MaterialYacimiento.objects.filter(esIgnea=True)

			elif (material == "Roca metamorfica"):
				yacPetroglifo = MaterialYacimiento.objects.filter(esMetamor=True)

			elif (material == "Roca sedimentaria"):
				yacPetroglifo = MaterialYacimiento.objects.filter(esSedimentaria=True)


		if (conservacion == "Bueno"):
			elementos = EstadoConserYac.objects.filter(enBuenEstado=True)

		elif (conservacion == "Modificado"):
			elementos = EstadoConserYac.objects.filter(estadoModificado=True)

		for result in yacPetroglifo:

			resultadoBusq = elementos.filter(yacimiento__id=result.yacimiento.id)

			for elem in resultadoBusq:
				listaResultados += [{'result':elem}]

		return render(request,entrada,{'listaResultados':listaResultados,'material':material,'conservacion':conservacion})

	elif (cruce_id == "25"):


		caracteristica = request.GET['carasurcopetrotipo3']
		clasificacion = request.GET['caracteristicaPintura']
		listaResultados = []

		if (caracteristica != "---"):

			if (caracteristica == "Base redonda"):
				elementosCar = CaracSurcoPetroglifo.objects.filter(esBaseRedonda=True)

			elif (caracteristica == "Base aguda"):
				elementosCar = CaracSurcoPetroglifo.objects.filter(esBaseAguda=True)

			elif (caracteristica == "Base relieve lineal"):
				elementosCar = CaracSurcoPetroglifo.objects.filter(esBajoRelieveLineal=True)

			elif (caracteristica == "Base relieve planar"):
				elementosCar = CaracSurcoPetroglifo.objects.filter(esBajoRelievePlanar=True)

			elif (caracteristica == "Alto relieve planar"):
				elementosCar = CaracSurcoPetroglifo.objects.filter(esAltoRelievePlanar=True)

			elif (caracteristica == "Alto relieve lineal"):
				elementosCar = CaracSurcoPetroglifo.objects.filter(esAltoRelieveLineal=True)

			if (clasificacion == "---"):
				for elem in elementosCar:
					listaResultados += [{'result':elem}]

		if (clasificacion != "---"):

			if (clasificacion == "Linea sencilla"):

				elementos = CaracDeLaPintura.objects.filter(esLineaSencilla=True)

			elif (clasificacion == "Linea compuesta"):
				elementos = CaracDeLaPintura.objects.filter(esLineaCompuesta=True)

			elif (clasificacion == "Figura rellena"):
				elementos = CaracDeLaPintura.objects.filter(esFiguraRellena=True)

			elif (clasificacion == "Impresion de manos positivo"):
				elementos = CaracDeLaPintura.objects.filter(esImpresionDeManosPositivo=True)

			elif (clasificacion == "Impresion de manos negativo"):
				elementos = CaracDeLaPintura.objects.filter(esImpresionDeManosNegativo=True)

			if (caracteristica == "---"):
				for elem in elementos:
					listaResultados += [{'result':elem}]

			else:
				for result in elementosCar:
					resultadoBusq = elementos.filter(yacimiento__id=result.yacimiento.id)

					for elem in resultadoBusq:
						listaResultados += [{'result':elem}]

		return render(request,entrada,{'listaResultados':listaResultados,'clasificacion':clasificacion,'caracteristica':caracteristica})


	if (cruce_id == "26"):

		surco = request.GET['surcoGrabado']
		listaResultados = []

		manifestacion =  ManifestacionYacimiento.objects.filter(esMicroPetroglifo=True)

		if (surco == "Base redonda"):
			elementosCar = CaracSurcoPetroglifo.objects.filter(esBaseRedonda=True)

		elif (surco == "Base aguda"):
			elementosCar = CaracSurcoPetroglifo.objects.filter(esBaseAguda=True)

		elif (surco == "Base relieve lineal"):
			elementosCar = CaracSurcoPetroglifo.objects.filter(esBajoRelieveLineal=True)

		elif (surco == "Base relieve planar"):
			elementosCar = CaracSurcoPetroglifo.objects.filter(esBajoRelievePlanar=True)

		elif (surco == "Alto relieve planar"):
			elementosCar = CaracSurcoPetroglifo.objects.filter(esAltoRelievePlanar=True)

		elif (surco == "Alto relieve lineal"):
			elementosCar = CaracSurcoPetroglifo.objects.filter(esAltoRelieveLineal=True)

		elif (surco == "Bateas"):
			elementosCar = CaracSurcoPetroglifo.objects.filter(esAltoRelieveLineal=True)


		for result in manifestacion:
			resultadoBusq = elementosCar.filter(yacimiento__id=result.yacimiento.id)

			for elem in resultadoBusq:
				listaResultados += [{'result':elem}]

		return render(request,entrada,{'listaResultados':listaResultados,'surco':surco})



	return render(request,entrada)

def consulta(request):
	# Se realiza la consula:
	estadoElegido = request.GET['estado']
	nombreElegido = request.GET['nombre']
	manifestacionElegida = request.GET['manifestacion']

	forma = CrucesYYForm
	yacimiento=""
	manifestacion=""
	mapa=""
	if(manifestacionElegida!="---"):
	 	
	 	# Se seleccionan las manifestaciones correspondientes
		if(manifestacionElegida=="Pinturas Rupestres"):
			manifestacion = ManifestacionYacimiento.objects.filter(esPintura=True)
			mapa = "/upload/PinturaRupestre.jpg"

		elif(manifestacionElegida=="Cerros y Piedras Miticas Naturales"):

			manifestacion = ManifestacionYacimiento.objects.filter(
				Q(esPiedraMiticaNatural=True)| Q(esCerroMiticoNatural=True))

			mapa = "/upload/Cerros.jpg"

		elif(manifestacionElegida=='Amoladores,Cupula,Puntos Acoplados'):
			manifestacion = ManifestacionYacimiento.objects.filter(
				Q(esAmolador=True)|Q(esCupulas=True)|Q(esPuntosAcoplados=True) )

			#FALTA
			mapa = "/upload/Amoladores.jpg"
			
		elif(manifestacionElegida=="Geoglifo"):
			manifestacion = ManifestacionYacimiento.objects.filter(esGeoglifo=True)
			mapa = "/upload/Geoglifos.jpg"

		elif(manifestacionElegida=="Micropentoglifos"):
			# Hay que agregar este atributo en el modelo de datos
			manifestacion = \
			ManifestacionYacimiento.objects.filter(esMonumentosMegaliticos=True)
			#FALTA
			mapa = "/upload/Micropetroglifos.jpg"
			
		elif(manifestacionElegida=="Monumentos megaliticos"):
			manifestacion = \
			ManifestacionYacimiento.objects.filter(esMonumentosMegaliticos=True)
			mapa = "/upload/Monumentos.jpg"

		elif(manifestacionElegida=="Petroglifos"):
			manifestacion = ManifestacionYacimiento.objects.filter(esPetroglifo=True)
			#FALTA
			mapa = "/upload/Petroglifos.jpg"

		########################################################################	

		if(nombreElegido=="" and estadoElegido=="Todos"):
			pass

		elif(nombreElegido!="" and estadoElegido=="Todos"):

			manifestacion =\
			 manifestacion.filter(yacimiento__nombre__icontains=nombreElegido)

		elif(nombreElegido=="" and estadoElegido!="Todos"):

			manifestacion=\
			manifestacion.filter(yacimiento__estado__nombre=estadoElegido)

		elif(nombreElegido!="" and estadoElegido!="Todos"):

			# Conculta encadenada
			manifestacion = \
			manifestacion.filter(yacimiento__nombre__icontains=nombreElegido,
				yacimiento__estado__nombre=estadoElegido)

	else:

		if(nombreElegido=="" and estadoElegido=="Todos"):
			# Se supone que tiene que redireccionar a un .html
			yacimiento=Yacimiento.objects.all()
			#yacimiento=Yacimiento.objects.filter(estado__nombre__exact=estadoElegido)

		elif(nombreElegido!="" and estadoElegido=="Todos"):

			yacimiento=Yacimiento.objects.filter(nombre__icontains=nombreElegido)

		elif(nombreElegido=="" and estadoElegido!="Todos"):

			yacimiento=Yacimiento.objects.filter(estado__nombre__exact=estadoElegido)

		elif(nombreElegido!="" and estadoElegido!="Todos"):

			# Conculta encadenada
			yacimiento = Yacimiento.objects.filter(nombre__icontains=nombreElegido,
				estado__nombre__exact=estadoElegido)

	

	return render(request,'joins/salidaConsulta.html', 
		{'yacimiento':yacimiento,'mapa':mapa,
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
