# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render
from django.db.models import Q
from anarapp.models import Estado, Piedra, Yacimiento, \
							ManifestacionYacimiento,FotografiaYac, \
							Coordenadas,ConstitucionYacimiento,UbicacionYacimiento,\
							CaracSurcoPetroglifo,DescColores,MaterialYacimiento,ManifestacionesAsociadas
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
		results=Yacimiento.objects.filter(estado__nombre__exact=estado)
		total = len(results)
		return render(request,entrada,{'total':total,'results':results,'estado':estado})

	elif (cruce_id in {"2","3","4","5","6","7","8"} ):

		codigo = request.GET['codigo']
		yacimiento=Yacimiento.objects.filter(codigo=codigo)
		return render(request,entrada,{'yacimiento':yacimiento,'codigo':codigo})

	elif (cruce_id == "9"):
		estado = request.GET['estado']
		results = ManifestacionYacimiento.objects.filter(yacimiento__estado__nombre=estado)

		if (results):
			yacimiento = results.filter(Q(esMenhires=True)|Q(esCerroConDolmen=True))
		else:
			yacimiento = ""

		return render(request,entrada,{'yacimiento':yacimiento,'estado':estado})

	elif (cruce_id == "10"):
		# Falta implementar
		listaYacimientos = []
		estado = request.GET['estado']
		yacimiento = Yacimiento.objects.filter(estado__nombre__exact=estado)

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

		manifestacion = \
		ManifestacionYacimiento.objects.filter(Q(yacimiento__estado__nombre=estado)|
			Q(yacimiento__codigo=codigo))
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

	# elif (cruce_id == "12"):
	# 	ubicacion = request.GET['ubicacion']

	# 	estados = ['Amazonas','Anzoategui','Apure','Aragua','Barinas','Bolvar', 
	# 			'Carabobo','Cojedes', 'Delta Amacuro', 'Falcn', 'Gurico','Lara',
	# 			'Mrida','Miranda','Monagas','Nueva Esparta','Portuguesa','Sucre',
	# 			'Tachira','Trujillo','Vargas','Yaracuy','Zulia']

	# 	listaManifestaciones = ["geoglifo","pinturasRupestres","micropetroglifos",
	# 							"petroglifo","petroglifoPintado","piedraMiticaNatural",
	# 							"cerroMiticoNatural","batea","menhires","amoladores",
	# 							"puntosAcoplados","cupula"]
	
	# 	diccionario = {}
	# 	diccionarioAux = {}

	# 	for manif in listaManifestaciones:
	# 		diccionarioAux[manif] = 0

	# 	for i in estados:
	# 		diccionario[i] = diccionarioAux

	# 	if (ubicacion == "Cerro"):
	# 		elementos = UbicacionYacimiento.objects.filter(enCerro=True)


	# 	elif (ubicacion == "Cima"):
	# 		elementos = UbicacionYacimiento.objects.filter(enCerroCima=True)

	# 	elif (ubicacion == "Ladera"):
	# 		elementos = UbicacionYacimiento.objects.filter(enCerroLadera=True)

	# 	elif (ubicacion == "Pie de montana"):
	# 		elementos = UbicacionYacimiento.objects.filter(enCerroPieDeMonte=True)

	# 	elif (ubicacion == "Barranco"):
	# 		elementos = UbicacionYacimiento.objects.filter(enCerroBarranco=True)

	# 	elif (ubicacion == "Acantilado"):
	# 		elementos = UbicacionYacimiento.objects.filter(enCerroAcantilado=True)

	# 	elif (ubicacion == "Valle"):
	# 		elementos = UbicacionYacimiento.objects.filter(enValle=True)

	# 	elif (ubicacion == "Rio"):
	# 		elementos = UbicacionYacimiento.objects.filter(enRio=True)

	# 	elif (ubicacion == "Lecho"):
	# 		elementos = UbicacionYacimiento.objects.filter(enRioLecho=True)

	# 	elif (ubicacion == "Margen derecha"):
	# 		elementos = UbicacionYacimiento.objects.filter(enRioMargenDerecha=True)

	# 	elif (ubicacion == "Margen izquierda"):
	# 		elementos = UbicacionYacimiento.objects.filter(enRioMargenIzquierda=True)

	# 	elif (ubicacion == "Isla"):
	# 		elementos = UbicacionYacimiento.objects.filter(enRioIsla=True)

	# 	elif (ubicacion == "Raudal"):
	# 		elementos = UbicacionYacimiento.objects.filter(enRioRaudal=True)

	# 	elif (ubicacion == "Costa"):
	# 		elementos = UbicacionYacimiento.objects.filter(enRioCosta=True)

	# 	for e in elementos:

	# 		y = e.yacimiento
	# 		print(y)
	# 		i = 0
	# 		manifestacion = ManifestacionYacimiento.objects.filter(yacimiento__id=y.id)
	# 		geoglifo = manifestacion.filter(esGeoglifo=True)
	# 		pinturasRupestres = manifestacion.filter(esPintura=True)
	# 		micropetroglifos = manifestacion.filter(esMicroPetroglifo=True)
	# 		petroglifo = manifestacion.filter(esPetroglifo = True)
	# 		petroglifoPintado = manifestacion.filter(esPetroglifoPintado = True)
	# 		piedraMiticaNatural = manifestacion.filter(esPiedraMiticaNatural=True)
	# 		cerroMiticoNatural = manifestacion.filter(esCerroMiticoNatural=True)
	# 		batea = manifestacion.filter(esBatea=True)
	# 		menhires = manifestacion.filter(esMenhires=True)
	# 		amoladores = manifestacion.filter(esAmolador=True)
	# 		puntosAcoplados = manifestacion.filter(esPuntosAcoplados=True)
	# 		cupula = manifestacion.filter(esCupulas = True)

	# 		arregloManifestaciones=[geoglifo,pinturasRupestres,micropetroglifos,
	# 								petroglifo,petroglifoPintado,piedraMiticaNatural,
	# 								cerroMiticoNatural,batea,menhires,amoladores,
	# 								puntosAcoplados,cupula]

	# 		a = y.estado.nombre
	# 		print(a)
	# 		cantidadManifestaciones = diccionario[y.estado.nombre]

	# 		for m in listaManifestaciones:

	# 			cantidadManifestaciones[m] = cantidadManifestaciones[m]+len(arregloManifestaciones[i])
	# 			i += 1
					

	# 	return render(request,entrada,{'diccionario':diccionario,'estados':estados,
	# 									'listaManifestaciones':listaManifestaciones})
	
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

		if (estado != "---"):

			pinturasRupestres =  pinturasRupestres.filter(yacimiento__estado__nombre=estado)

			if (pinturas == "---"):

				for y in pinturasRupestres:
					listaResultado += [{'yacimiento':y}]

		if (pinturas != "---"):

			if (pinturas in {'Pintura positiva negra','Pintura positiva blanca',\
							'Pintura positiva amarilla','Pintura positiva roja',\
							'Pintura positiva dos rojos','Pintura positiva tres rojos'}):

				yacPintura = DescColores.objects.filter(esPositiva=True)

			elif (pinturas in {'Pintura negativa negra','Pintura negativa blanca',\
								'Pintura negativa amarilla','Pintura negativa roja',\
								'Pintura negativa dos rojos','Pintura negativa tres rojos'}):

				yacPintura = DescColores.objects.filter(esNegativa=True)

			if (estado == "---"):

				for y in yacPintura:
					listaResultado += [{'yacimiento':y}]

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

		if (estado != "---"):

			petroglifoResult =  petroglifo.filter(yacimiento__estado__nombre=estado)

			if (material == "---"):
				for y in petroglifoResult:
					listaResultado += [{'petroglifo':y}]

		if (material != "---"):

			if (material == "Roca ignea"):
				yacPetroglifo = MaterialYacimiento.objects.filter(esIgnea=True)

			elif (material == "Roca metamorfica"):
				yacPetroglifo = MaterialYacimiento.objects.filter(esMetamor=True)

			elif (material == "Roca sedimentaria"):
				yacPetroglifo = MaterialYacimiento.objects.filter(esSedimentaria=True)


		for y in yacPetroglifo:

			if (estado != "---"):
				result = petroglifoResult.filter(yacimiento__id=y.yacimiento.id)

			else:
				result = petroglifo.filter(yacimiento__id=y.yacimiento.id)

			if (len(result)!=0):
				for objeto in result:
					listaResultado += [{'petroglifo':objeto}]

		return render(request,entrada,{'listaResultado':listaResultado,'estado':estado,'tipo':material})


	elif (cruce_id=="20"):

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

		return render(request,entrada,{'yacimiento':yacimientoResult,'manifestacion':manifestacion})

	elif (cruce_id=="21"):

		ubicacion = request.GET['ubicacion']
		caracteristica = request.GET['carasurcopetrotipo3']

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

		return render(request,entrada,{'yacimiento':elementos,'ubicacion':ubicacion})

	elif (cruce_id == "22"):
		ubicacion = request.GET['ubicacion']
		elementos = ""

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
		return render(request,entrada,{'yacimiento':elementos,'ubicacion':ubicacion})

	elif (cruce_id == "23"):

		manifestacion = request.GET['manifestacion']

	 	# Se seleccionan las manifestaciones correspondientes
		if(manifestacionElegida=="Pinturas Rupestres"):
			manifestacion = Yacimiento.ManifestacionYacimiento.objects.filter(esPintura=True)

		elif(manifestacionElegida=="Cerros y Piedras Miticas Naturales"):

			manifestacion = Yacimiento.ManifestacionYacimiento.objects.filter(
				Q(esPiedraMiticaNatural=True)| Q(esCerroMiticoNatural=True))

		elif(manifestacionElegida=='Amoladores,Cupula,Puntos Acoplados'):
			manifestacion = Yacimiento.ManifestacionYacimiento.objects.filter(
				Q(esAmolador=True)|Q(esCupulas=True)|Q(esPuntosAcoplados=True) )

			
		elif(manifestacionElegida=="Geoglifo"):
			manifestacion = Yacimiento.ManifestacionYacimiento.objects.filter(esGeoglifo=True)


		elif(manifestacionElegida=="Micropentoglifos"):
			# Hay que agregar este atributo en el modelo de datos
			manifestacion = \
			Yacimiento.ManifestacionYacimiento.objects.filter(esMonumentosMegaliticos=True)

			
		elif(manifestacionElegida=="Monumentos megaliticos"):
			manifestacion = \
			Yacimiento.ManifestacionYacimiento.objects.filter(esMonumentosMegaliticos=True)


		elif(manifestacionElegida=="Petroglifos"):
			manifestacion = Yacimiento.ManifestacionYacimiento.objects.filter(esPetroglifo=True)

		return render(request,entrada,{'yacimiento':elementos,'manifestacion':manifestacion})

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
