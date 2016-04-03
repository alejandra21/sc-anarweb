
	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (0, 0, 'Venezuela', 'Yacimiento 0', 'Municipio 13', 'Miranda'); 

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (True, True, True, True, False, 'anchoDe 12', 'anchoDeComp 1', 'anchoA 18', 0, False, 'anchoAComp 7', True, True, 'otros 17', False);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (2, False, NULL, False, False, NULL, 0, NULL, False, 22);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 0, 19, 36);

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 7', 0, 'diametro 15', 'ancho 19', '');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 2', 0, 'ancho 8');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, False, True, False, True, True, True, True, True, 'produndidadDe 19', 'anchoA 4', 'profundidadA 11', 0, False, True, 'anchoDe 9', False, True, True);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('', True, 0, 'diametro 2', 'profundidad 14');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (0, '');

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 19', 0);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (0, 'direcciones 15', '');

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (0, 1);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, False, 'orientacion 20', 0, True, False, True, 'otros 12');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, 'tecnicas 11', False, 0, 'otros 6', True);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (False, False, 'esTenenciaOtros 2', 0, False, False, False);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, True, False, 'mixto 17', 0, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (0, 40);

---------- Fin Insert Yacimiento 0

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (1, 1, 'Venezuela', 'Yacimiento 1', 'Municipio 1', 'Miranda'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 19', '', 'texto 6', 1, 'superficie 4', 'altura 6');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (True, False, True, False, False, 'anchoDe 2', 'anchoDeComp 19', 'anchoA 18', 1, False, 'anchoAComp 1', True, False, 'otros 4', True);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, True, NULL, True, True, NULL, 1, 37, False, NULL);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 1, NULL, 24);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 2', 1, 'diametro 19', 'ancho 20');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 4', 1, 'diametro 18', 'ancho 14', 'profundidad 15');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 8', 1, 'ancho 4');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 16', False, 1, 'diametro 20', '');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 1, 'otros 9');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (1, 17, 38, NULL, 'otros 17', 3);

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (1, 'urlImagen 1');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, True, 4, True, 34, 'perdidoPa 9', '', True, False, True, True, 'otros 9', 'especificar 3', False, 31, False, NULL, 9, True, 1, False, True, True, 14, True, False, '', False, False, 'observaciones 9', True, True, False, False, False, 'destruidoPa 2', True, False, True, False, '', False, '', '', False, False, NULL, True, '', True, 'crecimientoVegPa 4');

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 10', 1);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (False, '2013-08-08', 1, True, True, 'urlImagen 18');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', True, True, 1, 'nombrePoblado 6', False, False, False);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (1, NULL);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (1, '');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, True, 'orientacion 5', 1, False, False, True, 'otros 3');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (1, 'tecnicas 10');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, True, True, 1, False, True, 'otros 4', True);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, 'tecnicas 18', True, 1, 'otros 2', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, '', 1, False, False);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (True, False, True, 'mixto 10', 1, True);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, '', 1, False, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, True, False, True, True, 1, False, False, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (1, 20);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 1, True, False, False, True, False);

---------- Fin Insert Yacimiento 1

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (2, 2, 'Venezuela', 'Yacimiento 2', 'Municipio 11', 'Yaracuy'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', 'desnivel 16', 'texto 5', 2, 'superficie 19', 'altura 16');

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (22, False, 29, True, True, 11, 2, NULL, True, 28);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 2, 3, 2);

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 11', 2, 'diametro 15', 'ancho 10', 'profundidad 19');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, True, False, True, True, True, False, False, True, '', 'anchoA 17', 'profundidadA 16', 2, True, True, 'anchoDe 1', False, False, False);

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (2, NULL, NULL, 25, '', NULL);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 2', 'utmAdicional 6', 2, 'longitud 12');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (5, False, NULL, True, 16, 'perdidoPa 9', 'sumergidoPa 11', False, True, True, True, '', 'especificar 8', True, NULL, True, 2, 21, False, 2, True, False, True, NULL, False, False, '', False, False, 'observaciones 17', False, False, True, False, False, '', False, True, True, True, '', True, 'trasladadoPa 14', '', True, False, 36, True, 'erosionPa 11', False, '');

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (False, '2013-08-03', 2, True, True, '');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 11', '', True, 2, False, False, 'nombre 20', False, True, '', True);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (2, '', 'puntoDatum 14');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', True, True, 2, 'nombrePoblado 20', True, False, False);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, '', False, True, False, True, 2, False, True, '', False);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (2, '');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, True, 'orientacion 11', 2, True, True, True, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (2, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (2, 'tecnicas 19');

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, False, False, 2, True, True, 'otros 11', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, 'otros 1', 2, False, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, False, True, '', 2, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, 'observaciones 12', 2, True, True);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 2, True, True, False, False, False);

---------- Fin Insert Yacimiento 2

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (3, 3, 'Venezuela', 'Yacimiento 3', 'Municipio 7', 'Carabobo'); 

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (40, False, 15, True, True, 25, 3, NULL, True, 7);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 3, NULL, 1);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 11', 3, 'diametro 17', 'ancho 14');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 18', 3, 'diametro 8', 'ancho 6', '');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 4', '', 'diametro 8', 3, 'otros 19', 'largo 13');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 13', 3, 'ancho 8');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (3, 19, NULL, 1, 'otros 6', NULL);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 12', '', 3, 'longitud 16');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('fauna 8', 3);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 15', '', True, 3, True, False, 'nombre 4', True, False, 'otros 3', True);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (3, '', 'puntoDatum 7');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', False, False, 3, 'nombrePoblado 19', False, True, False);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 3', 'descripcionCementerio 12', False, '', True, False, True, 'descripcionCeramica 3', 'descripcionMonticulo 16', 3, '', 'descripcionOseo 8', True, False, '', 'descripcionLitica 10', True, False);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (True, 'tipo 6', False, False, False, False, 3, True, True, '', True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (3, '');

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (False, True, '', 3, False, True, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, True, True, False, True, 3, True, True, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (3, NULL);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 3, False, True, False, True, False);

---------- Fin Insert Yacimiento 3

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (4, 4, 'Venezuela', 'Yacimiento 4', 'Municipio 14', 'Zulia'); 

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, True, False, True, False, 'anchoDe 20', 'anchoDeComp 3', 'anchoA 11', 4, False, 'anchoAComp 8', False, True, 'otros 5', True);

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (True, 4, NULL, 29, True);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, True, 11, True, True, 22, 4, 30, True, 4);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 4, NULL, 11);

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (True, True, False, False, False, False, False, True, True, 'produndidadDe 3', 'anchoA 7', 'profundidadA 9', 4, True, True, 'anchoDe 18', False, False, False);

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 4, 'otros 16');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (4, NULL, 25, NULL, 'otros 12', NULL);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 7', '', 4, 'longitud 20');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', 'autor 1', True, 'institucion 13', True, 'fecha 18', True, False, False, 4, 'facebook 14', False, '', '', 'pais 5', True, '', 'twitter 10', '');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (4, 'urlImagen 10');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('', 4);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 14', 'observaciones 9', False, 4, False, True, 'nombre 15', False, True, 'otros 12', True);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (4, 'direcciones 5', 'puntoDatum 6');

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 18', 'descripcionCementerio 6', True, 'descripcionMito 7', True, False, True, '', 'descripcionMonticulo 7', 4, '', 'descripcionOseo 14', False, True, 'otros 3', 'descripcionLitica 20', True, False);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (True, 'tipo 1', False, False, True, True, 4, False, True, '', False);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, True, 'orientacion 9', 4, False, False, False, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, True, False, False, 4, False, True, '', True);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, True, True, 4, True, True, 'otros 5', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, '', 4, True, False);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, False, '', 4, True, False, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, 'observaciones 5', 4, False, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (4, 9);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 4, True, False, True, True, True);

---------- Fin Insert Yacimiento 4

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (5, 5, 'Venezuela', 'Yacimiento 5', 'Municipio 15', 'Barinas'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', '', 'texto 20', 5, 'superficie 7', 'altura 20');

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (40, False, 27, True, False, NULL, 5, 10, True, 11);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 5, NULL, 22);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 7', 5, 'diametro 11', 'ancho 10');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 4', 5, 'diametro 5', 'ancho 12', 'profundidad 7');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 10', 5, 'ancho 17');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('', False, 5, 'diametro 14', 'profundidad 14');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 5, '');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', '', False, '', True, 'fecha 7', True, False, False, 5, 'facebook 3', True, '', 'direccion 12', '', True, 'telefono 17', '', 'bibliografia 6');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (40, False, 3, True, 27, '', 'sumergidoPa 4', True, False, True, False, '', 'especificar 17', False, NULL, False, 22, 16, False, 5, False, True, False, 10, False, True, 'mas 14', False, False, '', False, True, False, True, True, '', True, True, False, False, '', False, 'trasladadoPa 16', 'enterradoPa 6', False, False, NULL, True, '', True, 'crecimientoVegPa 1');

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-02-20', 5, True, True, 'urlImagen 15');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 2', '', False, 5, False, False, 'nombre 12', True, True, 'otros 18', True);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (5, '', '');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', False, True, 5, '', False, False, False);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (5, 3);

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (5, 'numeroPlano 18');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (5, 'tecnicas 14');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (False, 'tecnicas 4', True, 5, '', True);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, False, False, 5, True, False, 'otros 15', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, '', 5, True, True);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (False, False, '', 5, False, False, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (True, False, True, '', 5, True);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, 'observaciones 16', 5, False, True);

---------- Fin Insert Yacimiento 5

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (6, 6, 'Venezuela', 'Yacimiento 6', 'Municipio 17', 'Nueva Esparta'); 

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 6, NULL, NULL, True);

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 5', 6, 'ancho 10');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, True, True, True, True, True, True, True, True, 'produndidadDe 4', 'anchoA 16', 'profundidadA 1', 6, True, False, 'anchoDe 1', False, True, False);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 15', False, 6, 'diametro 9', 'profundidad 2');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 7', 'autor 4', True, 'institucion 15', False, 'fecha 9', False, False, True, 6, 'facebook 1', False, 'mail 1', 'direccion 20', 'pais 10', True, 'telefono 3', 'twitter 16', 'bibliografia 19');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (6, 'urlImagen 10');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (NULL, 6);

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, False, NULL, True, 6, 'perdidoPa 3', 'sumergidoPa 1', False, True, False, True, '', 'especificar 1', False, NULL, False, 18, 35, False, 6, False, False, True, 18, True, True, '', True, True, '', False, False, True, False, True, 'destruidoPa 15', True, True, True, True, 'patinaPa 19', True, 'trasladadoPa 7', 'enterradoPa 7', False, False, 30, True, 'erosionPa 8', True, 'crecimientoVegPa 2');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('', 6);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 6);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-07-19', 6, False, True, 'urlImagen 6');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 13', '', True, 6, False, False, 'nombre 7', True, False, 'otros 20', False);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (6, '', '');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('nombreNoPoblado 10', False, False, 6, '', False, True, True);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, 'tipo 8', False, False, False, False, 6, True, False, 'otros 8', True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (6, 'notas 14');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (6, 'numeroPlano 14');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, 'tecnicas 2', False, 6, 'otros 20', False);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, True, True, 6, True, True, '', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, '', 6, True, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (True, False, False, 'mixto 19', 6, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, '', 6, False, False);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 6, True, True, True, False, True);

---------- Fin Insert Yacimiento 6

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (7, 7, 'Venezuela', 'Yacimiento 7', 'Municipio 5', 'Amazonas'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 18', '', 'texto 8', 7, 'superficie 1', 'altura 6');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (True, True, False, False, True, 'anchoDe 6', 'anchoDeComp 16', 'anchoA 2', 7, True, 'anchoAComp 9', True, False, 'otros 18', False);

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 7, NULL, 16, False);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 7, NULL, 39);

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 14', 7, 'diametro 2', 'ancho 6', 'profundidad 18');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 9', 7, 'ancho 8');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 7, 'otros 3');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', 'autor 2', True, 'institucion 15', False, 'fecha 16', False, True, True, 7, 'facebook 17', False, 'mail 4', 'direccion 18', 'pais 11', False, '', '', 'bibliografia 13');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (2, 7);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 4', 7);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (False, '2013-09-01', 7, False, False, 'urlImagen 11');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 16', 'observaciones 6', True, 7, False, False, 'nombre 4', False, True, '', False);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('', '', True, 'descripcionMito 10', True, False, True, 'descripcionCeramica 6', 'descripcionMonticulo 9', 7, 'descripcionCarbon 17', '', True, False, '', 'descripcionLitica 16', True, False);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (7, 'notas 19');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, True, 'orientacion 20', 7, False, False, True, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (7, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (7, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, True, True, 7, False, True, '', False);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, True, True, True, 7, False, False, '', True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, True, False, False, False, 7, True, True, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (7, 11);

---------- Fin Insert Yacimiento 7

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (8, 8, 'Venezuela', 'Yacimiento 8', 'Municipio 13', 'Lara'); 

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 8, NULL, 23, True);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 8, NULL, 14);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 7', 8, 'diametro 4', 'ancho 10');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 16', 8, 'diametro 20', 'ancho 9', '');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 6', 'profundidad 4', 'diametro 12', 8, '', 'largo 17');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, True, False, True, True, True, True, False, False, 'produndidadDe 10', 'anchoA 9', 'profundidadA 4', 8, False, True, 'anchoDe 6', True, False, True);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 9', 'utmAdicional 7', 8, 'longitud 16');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (39, False, 15, True, NULL, 'perdidoPa 7', 'sumergidoPa 20', False, False, True, False, '', 'especificar 18', True, 5, False, NULL, 36, True, 8, True, False, False, 10, False, False, 'mas 5', True, False, 'observaciones 4', True, True, True, True, False, '', False, True, True, True, 'patinaPa 18', True, 'trasladadoPa 16', 'enterradoPa 1', True, True, NULL, True, 'erosionPa 1', False, '');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('', 8);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 8);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 7', 'observaciones 3', True, 8, True, False, 'nombre 1', False, False, 'otros 16', False);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (8, 'direcciones 12', '');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('nombreNoPoblado 11', False, True, 8, '', False, False, True);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, '', True, False, True, False, 8, False, False, '', False);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (8, '');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, True, 'orientacion 10', 8, False, False, False, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (8, 'numeroPlano 2');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (8, 'tecnicas 6');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, True, False, 8, True, False, '', False);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (False, 'tecnicas 11', False, 8, '', True);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, True, False, 8, False, False, '', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, 'otros 7', 8, True, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (8, 2);

---------- Fin Insert Yacimiento 8

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (9, 9, 'Venezuela', 'Yacimiento 9', 'Municipio 11', 'Trujillo'); 

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, True, NULL, True, True, 22, 9, NULL, True, 7);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 9, NULL, 17);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 3', False, 9, 'diametro 9', 'profundidad 6');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 7', '', 9, 'longitud 2');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 7', '', False, 'institucion 14', True, 'fecha 7', True, False, False, 9, '', False, '', '', '', False, '', '', '');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (9, '');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('', 9);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (9, '', '');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, True, 'orientacion 17', 9, False, True, False, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (9, 'tecnicas 6');

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, '', 9, False, False);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (False, False, '', 9, True, True, True);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, '', 9, False, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, False, False, False, True, 9, True, False, False);

---------- Fin Insert Yacimiento 9

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (10, 10, 'Venezuela', 'Yacimiento 10', 'Municipio 1', 'Aragua'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 15', '', 'texto 15', 10, 'superficie 20', 'altura 18');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, True, True, False, True, 'anchoDe 18', 'anchoDeComp 5', 'anchoA 15', 10, False, 'anchoAComp 4', False, True, '', False);

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 10, NULL, NULL, False);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (24, True, NULL, True, False, NULL, 10, NULL, True, NULL);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 2', 10, 'diametro 3', 'ancho 20');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 10, 'otros 3');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 16', 'utmAdicional 14', 10, 'longitud 2');

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 10);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 13', 'observaciones 17', True, 10, False, True, 'nombre 15', False, True, 'otros 5', False);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (10, 'direcciones 15', '');

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, 'tipo 9', True, False, True, False, 10, True, True, 'otros 2', False);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (10, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (10, '');

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, True, True, 10, False, True, 'otros 17', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, '', 10, False, True);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (False, False, '', 10, True, False, False);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, False, False, '', 10, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, False, False, False, False, 10, True, True, False);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 10, True, True, True, False, True);

---------- Fin Insert Yacimiento 10

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (11, 11, 'Venezuela', 'Yacimiento 11', 'Municipio 7', 'Apure'); 

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 11, 15, NULL, True);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 11, 35, 6);

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 16', 11, 'diametro 13', 'ancho 14', '');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 11, '');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', '', True, 'institucion 7', True, 'fecha 19', False, True, True, 11, 'facebook 14', True, 'mail 3', 'direccion 15', '', True, 'telefono 19', 'twitter 8', 'bibliografia 1');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (5, 11);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 9', 11);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 2', '', True, 11, True, True, 'nombre 16', True, False, 'otros 20', True);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (11, '', 'puntoDatum 19');

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (11, 'notas 4');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, True, False, 11, True, True, 'otros 2', True);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, True, False, True, 11, False, True, '', True);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, True, 'esTenenciaOtros 9', 11, False, False, True);

---------- Fin Insert Yacimiento 11

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (12, 12, 'Venezuela', 'Yacimiento 12', 'Municipio 5', 'Barinas'); 

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 12, 14, 25, True);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, True, NULL, True, False, NULL, 12, 17, False, NULL);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 12, 29, 15);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 6', 12, 'diametro 15', 'ancho 13');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 10', 12, 'diametro 9', 'ancho 3', '');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 18', 12, 'ancho 12');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('', True, 12, 'diametro 16', 'profundidad 18');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 12, 'otros 9');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (12, NULL, 27, NULL, 'otros 6', NULL);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 17', '', 12, 'longitud 12');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, False, 40, True, NULL, '', '', True, False, False, True, 'otros 9', '', False, 31, True, 32, 3, False, 12, False, True, False, NULL, False, True, '', False, True, '', True, False, False, False, False, '', False, True, False, False, 'patinaPa 2', False, 'trasladadoPa 18', 'enterradoPa 8', True, True, NULL, False, '', False, '');

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (False, '2013-03-23', 12, False, True, '');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 9', 'observaciones 6', False, 12, False, True, 'nombre 18', True, False, '', False);

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', False, False, 12, '', False, False, True);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 16', '', True, 'descripcionMito 17', False, True, True, 'descripcionCeramica 12', '', 12, '', '', True, True, '', '', False, True);

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (12, 'numeroPlano 15');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (12, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, False, True, 12, True, True, '', False);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (False, 'tecnicas 18', True, 12, '', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, '', 12, True, False);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (False, False, 'esTenenciaOtros 13', 12, True, False, True);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, '', 12, False, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, True, True, True, False, 12, True, True, False);

---------- Fin Insert Yacimiento 12

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (13, 13, 'Venezuela', 'Yacimiento 13', 'Municipio 19', 'Anzoategui'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', '', 'texto 11', 13, 'superficie 12', 'altura 10');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 6', 13, 'diametro 6', 'ancho 14', '');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 4', 'profundidad 1', 'diametro 1', 13, '', 'largo 10');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 14', 13, 'ancho 14');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, True, True, True, True, False, False, True, True, 'produndidadDe 11', 'anchoA 13', 'profundidadA 11', 13, False, True, 'anchoDe 5', False, True, False);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 2', True, 13, 'diametro 7', '');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 13, '');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (13, NULL, NULL, NULL, '', NULL);

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (13, 'urlImagen 15');

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 13);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-09-10', 13, True, False, '');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 12', 'observaciones 18', True, 13, True, True, 'nombre 9', True, False, '', False);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (13, '', 'puntoDatum 16');

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('', '', False, 'descripcionMito 17', True, False, True, 'descripcionCeramica 14', '', 13, 'descripcionCarbon 13', 'descripcionOseo 2', True, False, '', '', True, False);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, True, 'orientacion 10', 13, False, True, False, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (13, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (13, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, True, False, 13, False, False, '', False);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, 'tecnicas 3', False, 13, '', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, 'otros 19', 13, False, True);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (False, True, '', 13, False, True, True);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (True, 'observaciones 14', 13, False, False);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 13, False, True, True, False, True);

---------- Fin Insert Yacimiento 13

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (14, 14, 'Venezuela', 'Yacimiento 14', 'Municipio 11', 'Portuguesa'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 1', 'desnivel 20', 'texto 8', 14, 'superficie 7', 'altura 18');

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (True, 14, 38, 10, False);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, False, NULL, False, True, NULL, 14, 10, False, 12);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 14, NULL, 7);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 3', 14, 'diametro 16', 'ancho 10');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 5', 14, 'diametro 4', 'ancho 3', '');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 3', '', 'diametro 12', 14, 'otros 10', 'largo 19');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('', False, 14, 'diametro 17', '');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 14, 'otros 18');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (14, 39, NULL, NULL, '', NULL);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 12', 'utmAdicional 7', 14, 'longitud 15');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (14, 'urlImagen 3');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('', 14);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 6', 14);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-09-06', 14, True, False, '');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 10', 'observaciones 3', True, 14, True, False, 'nombre 3', True, False, 'otros 16', False);

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('nombreNoPoblado 15', True, False, 14, '', False, True, True);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 3', '', True, '', False, False, False, 'descripcionCeramica 5', 'descripcionMonticulo 13', 14, '', '', False, False, '', '', False, True);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (False, 'tecnicas 9', True, 14, 'otros 15', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, '', 14, True, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, False, False, 'mixto 20', 14, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, True, True, True, False, 14, False, False, True);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 14, True, True, True, True, False);

---------- Fin Insert Yacimiento 14

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (15, 15, 'Venezuela', 'Yacimiento 15', 'Municipio 2', 'Tachira'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', '', 'texto 4', 15, 'superficie 3', 'altura 9');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, False, True, True, True, 'anchoDe 2', 'anchoDeComp 9', 'anchoA 7', 15, False, 'anchoAComp 6', True, False, '', True);

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 15, NULL, 20, True);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, True, NULL, False, True, NULL, 15, 38, True, NULL);

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 14', 'profundidad 14', 'diametro 9', 15, '', 'largo 8');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 16', 15, 'ancho 3');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (True, False, True, True, False, False, False, True, False, '', 'anchoA 2', 'profundidadA 20', 15, True, False, 'anchoDe 11', True, True, True);

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (15, NULL, NULL, NULL, '', NULL);

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', 'autor 9', True, 'institucion 5', False, 'fecha 2', True, False, False, 15, 'facebook 16', True, '', '', 'pais 1', False, '', 'twitter 1', 'bibliografia 18');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (25, False, 9, True, NULL, 'perdidoPa 1', '', False, True, True, False, '', 'especificar 9', False, 17, False, NULL, NULL, False, 15, True, False, True, 6, True, True, '', True, True, 'observaciones 15', True, False, False, False, False, '', True, False, True, False, '', True, '', '', False, False, 29, False, '', False, '');

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-05-03', 15, False, True, 'urlImagen 2');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 15', 'observaciones 16', False, 15, True, False, 'nombre 1', True, True, 'otros 12', True);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (15, 'direcciones 11', 'puntoDatum 9');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('nombreNoPoblado 12', False, True, 15, 'nombrePoblado 6', True, False, False);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (15, 15);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 5', 'descripcionCementerio 4', False, '', True, True, False, 'descripcionCeramica 5', '', 15, '', 'descripcionOseo 5', False, False, 'otros 9', '', True, False);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, False, 'orientacion 12', 15, False, False, False, 'otros 17');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (15, 'numeroPlano 8');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (15, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, True, True, 15, False, True, 'otros 5', True);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, True, True, 15, True, False, '', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, '', 15, True, True);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (True, '', 15, True, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, False, True, False, True, 15, True, True, False);

---------- Fin Insert Yacimiento 15

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (16, 16, 'Venezuela', 'Yacimiento 16', 'Municipio 14', 'Lara'); 

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 16, NULL, NULL, True);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (39, False, 6, True, False, 7, 16, 33, True, NULL);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 16, NULL, 21);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 4', 16, 'diametro 15', 'ancho 11');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 1', '', 'diametro 9', 16, 'otros 5', 'largo 11');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 16, '');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (16, 'urlImagen 7');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, False, 27, False, 27, 'perdidoPa 3', 'sumergidoPa 14', True, True, False, True, '', '', False, NULL, False, 14, 39, True, 16, True, False, False, 39, True, True, '', True, False, '', True, True, True, False, False, 'destruidoPa 16', False, False, True, False, '', True, '', '', True, True, NULL, True, '', True, 'crecimientoVegPa 6');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 4', '', True, 16, True, False, 'nombre 14', False, False, 'otros 10', True);

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', False, True, 16, '', False, False, True);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 8', 'descripcionCementerio 18', False, 'descripcionMito 18', False, False, False, 'descripcionCeramica 9', 'descripcionMonticulo 17', 16, '', 'descripcionOseo 17', True, False, 'otros 18', 'descripcionLitica 12', False, False);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, False, 'orientacion 17', 16, False, False, True, 'otros 6');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (16, 'numeroPlano 4');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (16, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, False, True, 16, False, False, '', False);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, True, False, 16, True, True, 'otros 9', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, 'otros 11', 16, True, False);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (False, False, '', 16, False, True, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, False, True, '', 16, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (True, 'observaciones 2', 16, False, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, False, True, False, False, 16, True, True, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (16, NULL);

---------- Fin Insert Yacimiento 16

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (17, 17, 'Venezuela', 'Yacimiento 17', 'Municipio 6', 'Zulia'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', '', 'texto 6', 17, 'superficie 16', 'altura 19');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, False, True, True, False, 'anchoDe 1', 'anchoDeComp 16', 'anchoA 5', 17, True, 'anchoAComp 8', False, True, '', False);

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 17, 37, NULL, True);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (7, True, NULL, True, True, 38, 17, NULL, False, 17);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 17, NULL, 32);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 9', 17, 'diametro 6', 'ancho 15');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 17', '', 'diametro 11', 17, 'otros 1', 'largo 1');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 11', 17, 'ancho 8');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('', True, 17, 'diametro 19', 'profundidad 8');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 17, '');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (17, 19, NULL, NULL, '', 1);

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (17, '');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('', 17);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 17);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 11', '', True, 17, True, True, 'nombre 10', True, True, '', False);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (17, '', '');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', True, False, 17, 'nombrePoblado 20', True, True, True);

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, True, True, 17, True, False, '', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, 'otros 10', 17, False, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (True, True, True, 'mixto 7', 17, True);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (True, '', 17, True, True);

---------- Fin Insert Yacimiento 17

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (18, 18, 'Venezuela', 'Yacimiento 18', 'Municipio 14', 'Sucre'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', 'desnivel 19', 'texto 9', 18, 'superficie 20', 'altura 3');

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 18, 14, 17, False);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (23, True, 24, True, False, 28, 18, NULL, True, 20);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 18, NULL, 5);

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 13', 18, 'diametro 3', 'ancho 11', 'profundidad 6');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 4', '', 'diametro 2', 18, 'otros 2', 'largo 17');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 14', 18, 'ancho 6');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 18, '');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (18, NULL, 26, 38, 'otros 15', 17);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 12', '', 18, 'longitud 1');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (18, '');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('fauna 14', 18);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 18);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 13', '', True, 18, False, False, 'nombre 4', False, False, 'otros 18', True);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (18, NULL);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, False, 'orientacion 10', 18, True, True, False, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (18, 'tecnicas 3');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, True, True, True, 18, True, True, 'otros 11', True);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, '', False, 18, 'otros 5', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, 'otros 13', 18, False, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, True, False, False, True, 18, True, True, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (18, NULL);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 18, True, False, False, True, True);

---------- Fin Insert Yacimiento 18

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (19, 19, 'Venezuela', 'Yacimiento 19', 'Municipio 2', 'Vargas'); 

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 14', 19, 'diametro 13', 'ancho 12');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 11', '', 'diametro 5', 19, 'otros 13', 'largo 1');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, False, True, True, False, False, False, False, True, '', 'anchoA 10', 'profundidadA 8', 19, False, False, 'anchoDe 14', False, False, True);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 8', True, 19, 'diametro 7', 'profundidad 17');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 19, '');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 20', '', 19, 'longitud 7');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', 'autor 7', False, '', True, 'fecha 12', False, True, True, 19, '', True, 'mail 4', 'direccion 7', '', False, '', 'twitter 1', '');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (14, False, NULL, False, 36, 'perdidoPa 20', '', True, False, False, True, '', 'especificar 6', False, NULL, True, NULL, NULL, True, 19, True, True, True, 5, False, False, 'mas 11', True, True, '', False, False, False, True, True, 'destruidoPa 10', True, True, True, False, '', False, '', '', False, False, NULL, False, 'erosionPa 15', True, 'crecimientoVegPa 2');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 8', '', True, 19, False, False, 'nombre 14', False, True, 'otros 9', True);

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', False, False, 19, '', False, True, True);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (19, NULL);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 11', '', True, 'descripcionMito 7', True, False, False, 'descripcionCeramica 18', 'descripcionMonticulo 9', 19, 'descripcionCarbon 17', 'descripcionOseo 9', True, True, '', '', False, True);

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (19, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (19, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, False, False, 19, True, True, 'otros 13', False);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, False, True, 19, False, True, '', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, '', 19, False, False);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (True, True, True, '', 19, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (19, NULL);

---------- Fin Insert Yacimiento 19

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (20, 20, 'Venezuela', 'Yacimiento 20', 'Municipio 4', 'Monagas'); 

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (True, 20, 9, NULL, True);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, False, 39, True, True, 1, 20, 7, False, 2);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 20, 3, 15);

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 9', 'profundidad 13', 'diametro 7', 20, 'otros 2', 'largo 14');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, False, True, True, False, False, True, True, True, '', 'anchoA 14', 'profundidadA 12', 20, True, True, 'anchoDe 10', False, True, False);

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 20, 'otros 4');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (20, NULL, 2, 7, '', NULL);

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (NULL, 20);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 20);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (20, 'notas 12');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (20, 'numeroPlano 1');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, True, True, 20, True, False, 'otros 5', False);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, True, False, 20, True, False, '', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, 'otros 10', 20, True, True);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, False, 'esTenenciaOtros 12', 20, True, True, True);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, 'observaciones 3', 20, False, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (20, 39);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 20, True, True, False, False, False);

---------- Fin Insert Yacimiento 20

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (21, 21, 'Venezuela', 'Yacimiento 21', 'Municipio 20', 'Tachira'); 

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 21, 34, 2);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 13', 21, 'diametro 6', 'ancho 9');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 6', '', 'diametro 4', 21, '', 'largo 5');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 20', 21, 'ancho 3');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, True, True, True, True, False, False, False, True, 'produndidadDe 6', 'anchoA 1', 'profundidadA 2', 21, False, True, 'anchoDe 6', False, False, False);

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (21, 14, 13, 3, '', NULL);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 14', 'utmAdicional 2', 21, 'longitud 14');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 9', '', True, 'institucion 4', False, 'fecha 17', True, True, False, 21, '', False, 'mail 20', '', '', False, '', 'twitter 4', '');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (NULL, 21);

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, False, NULL, True, NULL, 'perdidoPa 1', '', False, True, True, False, 'otros 11', '', False, 37, True, NULL, 4, True, 21, False, False, False, NULL, True, False, 'mas 19', False, True, 'observaciones 8', True, False, True, True, True, '', True, False, False, False, 'patinaPa 4', True, 'trasladadoPa 11', 'enterradoPa 20', False, False, 21, True, '', True, 'crecimientoVegPa 3');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('', 21);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (21, 21);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 17', 'descripcionCementerio 8', False, '', False, False, False, 'descripcionCeramica 9', '', 21, '', 'descripcionOseo 13', True, False, 'otros 6', 'descripcionLitica 13', True, True);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (True, 'tipo 17', True, False, True, True, 21, True, True, 'otros 6', False);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (21, '');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, False, 'orientacion 5', 21, True, False, True, 'otros 4');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (21, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, True, True, True, 21, False, True, '', False);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (False, '', True, 21, 'otros 19', False);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, False, True, 21, False, False, 'otros 7', True);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, False, 'esTenenciaOtros 10', 21, False, False, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, False, False, '', 21, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, True, True, False, True, 21, False, True, True);

---------- Fin Insert Yacimiento 21

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (22, 22, 'Venezuela', 'Yacimiento 22', 'Municipio 9', 'Portuguesa'); 

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (3, True, NULL, True, False, 27, 22, NULL, True, NULL);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 22, 21, 7);

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 6', 22, 'diametro 18', 'ancho 15', '');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 17', '', 'diametro 1', 22, '', 'largo 15');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 22, '');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (22, 8, NULL, NULL, 'otros 4', 7);

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 4', '', True, 'institucion 10', False, 'fecha 2', True, False, False, 22, '', False, '', 'direccion 16', '', False, 'telefono 3', '', '');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (14, 22);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (22, 'direcciones 13', '');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('nombreNoPoblado 1', True, False, 22, '', False, True, False);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (22, 34);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, True, 'orientacion 4', 22, False, False, False, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (22, 'tecnicas 7');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, '', True, 22, 'otros 4', True);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, True, True, 22, True, True, 'otros 9', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, 'otros 16', 22, True, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, False, False, True, False, 22, True, True, True);

---------- Fin Insert Yacimiento 22

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (23, 23, 'Venezuela', 'Yacimiento 23', 'Municipio 10', 'Delta Amacuro'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', 'desnivel 8', 'texto 16', 23, 'superficie 1', 'altura 19');

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 23, NULL, 12, False);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 23, NULL, 19);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 10', 23, 'diametro 11', 'ancho 8');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 2', 23, 'diametro 3', 'ancho 3', 'profundidad 5');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, False, True, True, False, True, False, True, True, 'produndidadDe 5', 'anchoA 13', 'profundidadA 8', 23, True, False, 'anchoDe 17', False, True, False);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('', False, 23, 'diametro 14', '');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 23, '');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 10', 'utmAdicional 15', 23, 'longitud 3');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (23, '');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (37, False, NULL, True, 39, '', 'sumergidoPa 17', True, False, False, True, 'otros 18', '', False, NULL, False, NULL, NULL, False, 23, False, True, True, 7, True, True, 'mas 16', True, False, '', False, True, True, False, False, '', True, False, False, True, '', False, 'trasladadoPa 6', '', True, True, 26, False, '', False, '');

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 12', 23);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 1', '', False, 23, True, False, 'nombre 10', True, True, '', True);

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('nombreNoPoblado 14', False, False, 23, '', True, False, False);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (23, 7);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('', 'descripcionCementerio 3', True, '', True, True, True, '', '', 23, 'descripcionCarbon 7', 'descripcionOseo 6', True, False, 'otros 16', 'descripcionLitica 19', False, False);

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (23, 'tecnicas 7');

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, False, False, 23, False, False, '', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, 'otros 7', 23, False, True);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, '', 23, False, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (23, 8);

---------- Fin Insert Yacimiento 23

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (24, 24, 'Venezuela', 'Yacimiento 24', 'Municipio 18', 'Tachira'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 19', 'desnivel 6', 'texto 20', 24, 'superficie 19', 'altura 4');

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (True, 24, NULL, 3, True);

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 5', 24, 'diametro 20', 'ancho 18', '');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 3', 'profundidad 18', 'diametro 2', 24, 'otros 9', 'largo 18');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 24, '');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (24, 29, 18, NULL, 'otros 7', 20);

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (24, 'urlImagen 7');

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 12', 24);

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', True, True, 24, 'nombrePoblado 8', False, False, False);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (24, 'notas 1');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, False, 'orientacion 17', 24, True, False, False, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (24, 'numeroPlano 4');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (24, 'tecnicas 13');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (False, '', True, 24, 'otros 4', True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (24, NULL);

---------- Fin Insert Yacimiento 24

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (25, 25, 'Venezuela', 'Yacimiento 25', 'Municipio 10', 'Anzoategui'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', 'desnivel 4', 'texto 13', 25, 'superficie 9', 'altura 12');

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (28, True, 36, False, True, 3, 25, 14, True, NULL);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 25, NULL, 39);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 3', 25, 'diametro 10', 'ancho 17');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 17', 25, 'ancho 1');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, False, True, True, True, False, True, False, True, 'produndidadDe 7', 'anchoA 9', 'profundidadA 10', 25, True, False, 'anchoDe 12', False, True, False);

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (25, 26, 19, 29, 'otros 16', 8);

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 9', '', False, 'institucion 3', False, 'fecha 3', False, True, True, 25, 'facebook 18', True, 'mail 1', 'direccion 11', '', False, '', '', '');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (25, 'urlImagen 15');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (NULL, 25);

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (5, True, NULL, False, NULL, '', 'sumergidoPa 14', False, False, True, True, '', '', True, NULL, True, 8, 15, True, 25, False, False, False, NULL, False, True, 'mas 1', False, True, '', False, False, True, False, False, '', False, False, True, False, 'patinaPa 5', False, '', 'enterradoPa 5', False, False, 5, True, 'erosionPa 17', True, '');

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 13', 25);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-04-24', 25, True, False, '');

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (25, 'direcciones 19', '');

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (25, 8);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, '', True, False, False, False, 25, False, False, '', True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (25, 'notas 11');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (25, 'tecnicas 11');

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, True, '', 25, True, False, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, False, True, True, True, 25, True, False, True);

---------- Fin Insert Yacimiento 25

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (26, 26, 'Venezuela', 'Yacimiento 26', 'Municipio 18', 'Cojedes'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', 'desnivel 7', 'texto 10', 26, 'superficie 19', 'altura 9');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, False, False, True, True, 'anchoDe 14', 'anchoDeComp 6', 'anchoA 17', 26, False, 'anchoAComp 8', True, False, 'otros 1', False);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, True, 21, False, False, 7, 26, NULL, True, 12);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 26, NULL, 35);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 10', 26, 'diametro 5', 'ancho 14');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 15', 26, 'diametro 1', 'ancho 18', 'profundidad 1');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 8', '', 'diametro 6', 26, 'otros 4', 'largo 19');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 6', 26, 'ancho 2');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, False, False, True, True, False, False, False, True, '', 'anchoA 2', 'profundidadA 1', 26, True, False, 'anchoDe 19', False, True, False);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('', True, 26, 'diametro 1', 'profundidad 6');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (26, NULL, 26, NULL, 'otros 9', NULL);

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', 'autor 4', True, 'institucion 4', True, 'fecha 1', False, True, True, 26, '', False, '', 'direccion 12', 'pais 19', False, 'telefono 15', '', 'bibliografia 15');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, False, 25, True, 19, 'perdidoPa 1', '', False, False, True, True, '', '', True, NULL, False, NULL, 1, False, 26, True, True, True, NULL, True, False, 'mas 12', True, False, 'observaciones 17', True, False, True, False, False, 'destruidoPa 20', False, False, False, True, '', False, 'trasladadoPa 14', '', True, False, NULL, True, '', False, 'crecimientoVegPa 15');

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (False, '2013-04-25', 26, True, True, 'urlImagen 9');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 1', 'observaciones 14', False, 26, False, False, 'nombre 6', True, True, '', True);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (26, '', '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (26, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (26, 'tecnicas 15');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (False, '', True, 26, '', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, '', 26, True, True);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, False, '', 26, False, False, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, True, True, False, False, 26, False, True, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (26, NULL);

---------- Fin Insert Yacimiento 26

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (27, 27, 'Venezuela', 'Yacimiento 27', 'Municipio 6', 'Bolívar'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', 'desnivel 6', 'texto 7', 27, 'superficie 10', 'altura 18');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (True, True, True, False, False, 'anchoDe 9', 'anchoDeComp 15', 'anchoA 2', 27, False, 'anchoAComp 14', True, False, 'otros 15', False);

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 27, 15, NULL, False);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (14, False, 7, True, False, 25, 27, NULL, False, NULL);

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, False, True, False, True, True, True, False, True, 'produndidadDe 9', 'anchoA 10', 'profundidadA 14', 27, False, False, 'anchoDe 2', True, True, False);

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 27, '');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (27, NULL, NULL, NULL, '', NULL);

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', 'autor 18', True, '', True, 'fecha 8', True, False, True, 27, 'facebook 5', True, '', '', '', True, '', '', 'bibliografia 11');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, True, NULL, False, 4, '', '', True, True, True, True, '', 'especificar 11', True, 38, False, 21, 25, False, 27, False, True, False, NULL, True, False, '', True, False, 'observaciones 11', False, False, True, True, True, '', True, True, False, False, '', False, '', '', False, True, NULL, False, '', True, '');

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (27, '', '');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('nombreNoPoblado 8', False, True, 27, '', True, True, True);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (27, 33);

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (27, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (27, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, True, False, 27, True, True, 'otros 19', True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (27, 28);

---------- Fin Insert Yacimiento 27

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (28, 28, 'Venezuela', 'Yacimiento 28', 'Municipio 5', 'Vargas'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 20', 'desnivel 4', 'texto 9', 28, 'superficie 12', 'altura 12');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, False, True, True, True, 'anchoDe 15', 'anchoDeComp 5', 'anchoA 13', 28, True, 'anchoAComp 19', False, False, 'otros 16', False);

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (True, 28, NULL, NULL, False);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, False, 18, False, False, 36, 28, NULL, True, 32);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 28, 11, 35);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 15', 28, 'diametro 17', 'ancho 8');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 5', 28, 'ancho 17');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, True, True, False, False, True, False, False, False, '', 'anchoA 14', 'profundidadA 7', 28, True, True, 'anchoDe 8', True, True, True);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 11', '', 28, 'longitud 5');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (2, 28);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (False, '2013-02-20', 28, True, False, 'urlImagen 13');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 7', '', True, 28, False, True, 'nombre 11', True, True, '', True);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (28, 3);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, False, 'orientacion 6', 28, True, False, True, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, True, True, 28, True, False, '', False);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, 'tecnicas 3', False, 28, 'otros 20', False);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, True, False, 28, True, False, '', True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (28, 39);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 28, True, False, True, False, False);

---------- Fin Insert Yacimiento 28

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (29, 29, 'Venezuela', 'Yacimiento 29', 'Municipio 13', 'Zulia'); 

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, True, True, True, False, 'anchoDe 9', 'anchoDeComp 12', 'anchoA 13', 29, True, 'anchoAComp 15', True, True, 'otros 15', False);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (16, True, 36, True, False, NULL, 29, NULL, False, 6);

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 10', 29, 'diametro 12', 'ancho 15', 'profundidad 15');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 16', 'profundidad 1', 'diametro 3', 29, '', 'largo 1');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 19', 29, 'ancho 10');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 29, '');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (29, NULL, NULL, 36, '', 20);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 4', '', 29, 'longitud 10');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (NULL, 29);

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (22, True, NULL, False, NULL, 'perdidoPa 13', '', False, False, True, True, '', '', False, NULL, False, NULL, 5, True, 29, False, False, False, NULL, True, True, 'mas 19', True, True, '', True, True, True, False, False, 'destruidoPa 16', True, False, False, True, '', True, 'trasladadoPa 13', 'enterradoPa 1', False, True, 34, True, 'erosionPa 15', True, '');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 1', '', True, 29, False, False, 'nombre 20', False, True, '', True);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (29, '', 'puntoDatum 7');

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('', '', False, '', False, True, False, 'descripcionCeramica 13', '', 29, 'descripcionCarbon 5', 'descripcionOseo 9', True, False, '', 'descripcionLitica 11', True, False);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (True, 'tipo 8', False, False, True, True, 29, True, True, '', True);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, False, 'orientacion 14', 29, True, False, True, 'otros 3');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (29, '');

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, 'otros 18', 29, False, False);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, False, '', 29, False, True, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, 'observaciones 20', 29, False, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, False, False, True, True, 29, False, True, False);

---------- Fin Insert Yacimiento 29

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (30, 30, 'Venezuela', 'Yacimiento 30', 'Municipio 2', 'Falcón'); 

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, False, NULL, False, False, 12, 30, NULL, False, NULL);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 30, 8, 18);

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 18', 'profundidad 6', 'diametro 1', 30, 'otros 5', 'largo 7');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, True, False, True, True, False, True, True, False, 'produndidadDe 9', 'anchoA 5', 'profundidadA 10', 30, True, False, 'anchoDe 10', False, True, True);

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 30, 'otros 17');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 8', '', 30, 'longitud 13');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (24, False, NULL, False, NULL, 'perdidoPa 18', 'sumergidoPa 13', False, False, True, True, 'otros 1', '', False, 3, False, 19, 27, False, 30, False, True, False, 12, True, True, 'mas 6', True, False, '', False, True, True, False, False, 'destruidoPa 1', True, True, True, True, 'patinaPa 2', False, 'trasladadoPa 6', 'enterradoPa 14', True, True, 9, True, '', True, 'crecimientoVegPa 5');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('fauna 4', 30);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 30);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (30, '', 'puntoDatum 3');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', False, True, 30, 'nombrePoblado 6', False, True, True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (30, '');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, False, 'orientacion 14', 30, True, False, True, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, False, True, 30, True, True, 'otros 2', False);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (False, '', False, 30, 'otros 20', True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (True, False, True, '', 30, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (True, 'observaciones 7', 30, False, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, False, False, False, True, 30, True, True, False);

---------- Fin Insert Yacimiento 30

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (31, 31, 'Venezuela', 'Yacimiento 31', 'Municipio 2', 'Trujillo'); 

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, False, True, True, True, 'anchoDe 16', 'anchoDeComp 14', 'anchoA 9', 31, True, 'anchoAComp 12', True, True, 'otros 17', False);

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 31, NULL, 3, False);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 17', 31, 'diametro 3', 'ancho 6');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (True, False, True, True, False, False, False, True, False, 'produndidadDe 7', 'anchoA 18', 'profundidadA 3', 31, True, True, 'anchoDe 4', False, True, False);

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 31, 'otros 10');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (19, 31);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 2', 31);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-09-14', 31, False, False, '');

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (31, 39);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, '', False, True, False, False, 31, False, False, 'otros 18', True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (31, '');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, False, 'orientacion 20', 31, False, False, True, '');

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, False, False, 31, True, True, '', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, 'otros 14', 31, True, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (True, True, True, '', 31, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (31, NULL);

---------- Fin Insert Yacimiento 31

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (32, 32, 'Venezuela', 'Yacimiento 32', 'Municipio 14', 'Cojedes'); 

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, True, True, False, True, 'anchoDe 16', 'anchoDeComp 7', 'anchoA 5', 32, True, 'anchoAComp 1', False, True, '', True);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (10, False, NULL, True, False, NULL, 32, NULL, True, NULL);

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 11', 'profundidad 14', 'diametro 20', 32, '', 'largo 19');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 7', 32, 'ancho 11');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 12', True, 32, 'diametro 9', '');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 6', 'utmAdicional 12', 32, 'longitud 18');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (32, '');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (NULL, 32);

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, True, 26, True, NULL, '', 'sumergidoPa 6', True, False, False, False, '', 'especificar 7', True, 9, False, NULL, NULL, True, 32, True, False, False, NULL, False, True, 'mas 16', False, False, 'observaciones 12', False, False, True, False, False, 'destruidoPa 15', True, True, True, False, 'patinaPa 15', False, '', '', True, False, 23, False, 'erosionPa 8', True, '');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('', 32);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 6', 'observaciones 1', True, 32, True, False, 'nombre 1', False, False, 'otros 10', False);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('', '', False, '', True, False, False, '', 'descripcionMonticulo 6', 32, 'descripcionCarbon 14', '', True, False, 'otros 5', 'descripcionLitica 1', False, False);

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, False, False, 32, False, False, 'otros 19', False);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, True, True, 32, True, False, 'otros 7', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, 'otros 11', 32, True, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, 'observaciones 2', 32, True, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, False, True, True, False, 32, False, False, True);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 32, True, False, False, True, False);

---------- Fin Insert Yacimiento 32

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (33, 33, 'Venezuela', 'Yacimiento 33', 'Municipio 9', 'Vargas'); 

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, False, True, False, True, 'anchoDe 6', 'anchoDeComp 7', 'anchoA 8', 33, True, 'anchoAComp 6', True, True, '', False);

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (True, 33, NULL, NULL, True);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (15, False, NULL, True, True, 22, 33, NULL, True, 24);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 33, NULL, 14);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 16', 33, 'diametro 6', 'ancho 5');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 11', 33, 'diametro 15', 'ancho 11', 'profundidad 14');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 3', 'profundidad 7', 'diametro 5', 33, 'otros 6', 'largo 11');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 12', 33, 'ancho 18');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, False, False, False, False, True, False, True, True, 'produndidadDe 2', 'anchoA 5', 'profundidadA 11', 33, True, True, 'anchoDe 17', False, False, True);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 13', False, 33, 'diametro 9', 'profundidad 3');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 17', '', 33, 'longitud 11');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', '', True, '', False, 'fecha 8', False, False, False, 33, 'facebook 20', True, 'mail 7', '', 'pais 16', True, 'telefono 18', '', 'bibliografia 16');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (33, '');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (17, 33);

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('fauna 5', 33);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 33);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-10-13', 33, True, True, '');

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (33, 'direcciones 9', '');

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('', '', False, 'descripcionMito 14', False, False, False, 'descripcionCeramica 13', 'descripcionMonticulo 15', 33, 'descripcionCarbon 5', '', False, True, 'otros 4', '', True, False);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, '', True, True, True, False, 33, False, False, '', True);

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (33, '');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (False, '', True, 33, '', False);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, False, 'esTenenciaOtros 11', 33, True, True, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, '', 33, False, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (33, 40);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 33, True, True, False, True, False);

---------- Fin Insert Yacimiento 33

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (34, 34, 'Venezuela', 'Yacimiento 34', 'Municipio 15', 'Barinas'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', 'desnivel 19', 'texto 14', 34, 'superficie 9', 'altura 8');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (True, False, False, True, True, 'anchoDe 16', 'anchoDeComp 1', 'anchoA 17', 34, False, 'anchoAComp 10', True, False, 'otros 7', False);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, True, 38, True, False, NULL, 34, 21, False, 34);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 34, 13, 1);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 16', 34, 'diametro 16', 'ancho 8');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 2', 'profundidad 7', 'diametro 20', 34, 'otros 19', 'largo 15');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 15', 34, 'ancho 19');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (True, False, True, False, False, True, True, True, False, '', 'anchoA 4', 'profundidadA 6', 34, False, False, 'anchoDe 14', False, True, False);

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 34, 'otros 14');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (34, 'urlImagen 20');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (26, False, NULL, True, NULL, 'perdidoPa 7', '', True, True, True, False, 'otros 20', '', False, 22, True, 27, NULL, True, 34, True, True, True, NULL, False, False, 'mas 20', False, True, '', True, False, False, True, True, '', True, False, False, False, 'patinaPa 15', False, 'trasladadoPa 12', 'enterradoPa 7', False, True, NULL, True, 'erosionPa 18', True, '');

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 12', 34);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (False, '2013-03-11', 34, False, True, '');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('nombreNoPoblado 13', True, True, 34, 'nombrePoblado 20', True, False, False);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (True, '', False, False, True, True, 34, False, False, '', True);

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (34, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (34, 'tecnicas 14');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (False, '', False, 34, 'otros 10', True);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, True, False, 34, False, True, '', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, '', 34, True, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (34, NULL);

---------- Fin Insert Yacimiento 34

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (35, 35, 'Venezuela', 'Yacimiento 35', 'Municipio 1', 'Guárico'); 

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 35, 34, 24, True);

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (True, False, False, False, False, True, False, True, False, 'produndidadDe 11', 'anchoA 20', 'profundidadA 10', 35, False, False, 'anchoDe 10', True, False, False);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 10', False, 35, 'diametro 20', 'profundidad 2');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 17', '', 35, 'longitud 10');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (30, 35);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 18', 'observaciones 5', False, 35, True, False, 'nombre 18', False, True, 'otros 18', False);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (35, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (35, 'tecnicas 14');

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, True, True, True, 35, True, False, '', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, '', 35, False, True);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (True, '', 35, True, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (35, 7);

---------- Fin Insert Yacimiento 35

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (36, 36, 'Venezuela', 'Yacimiento 36', 'Municipio 13', 'Portuguesa'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 11', 'desnivel 2', 'texto 14', 36, 'superficie 13', 'altura 11');

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (True, 36, NULL, NULL, True);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 36, 39, 16);

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 5', 36, 'diametro 5', 'ancho 2', '');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (True, False, True, True, True, True, False, False, True, 'produndidadDe 1', 'anchoA 7', 'profundidadA 9', 36, False, True, 'anchoDe 12', False, True, True);

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (36, NULL, NULL, 28, '', NULL);

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (36, '');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (8, 36);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (False, '2013-07-24', 36, False, True, 'urlImagen 6');

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('', 'descripcionCementerio 20', True, '', True, False, False, '', 'descripcionMonticulo 2', 36, 'descripcionCarbon 2', 'descripcionOseo 9', True, True, 'otros 12', 'descripcionLitica 11', False, True);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, '', False, True, False, False, 36, True, True, 'otros 8', True);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, False, 'orientacion 10', 36, False, True, True, 'otros 17');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (36, 'numeroPlano 5');

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, True, True, False, 36, False, False, '', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, 'otros 18', 36, False, False);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (False, True, 'esTenenciaOtros 20', 36, False, True, False);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (True, True, False, 'mixto 2', 36, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (True, '', 36, True, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (36, 22);

---------- Fin Insert Yacimiento 36

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (37, 37, 'Venezuela', 'Yacimiento 37', 'Municipio 7', 'Cojedes'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', 'desnivel 17', 'texto 3', 37, 'superficie 10', 'altura 14');

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (1, True, NULL, False, True, 3, 37, NULL, False, 5);

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 8', 'profundidad 17', 'diametro 6', 37, '', 'largo 12');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 5', 37, 'ancho 6');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (True, True, True, False, False, True, True, False, False, 'produndidadDe 2', 'anchoA 13', 'profundidadA 6', 37, False, False, 'anchoDe 14', True, True, False);

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 37, 'otros 19');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (37, 37, NULL, 18, 'otros 9', NULL);

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 14', '', True, 'institucion 12', False, 'fecha 20', True, True, False, 37, '', False, 'mail 2', 'direccion 19', 'pais 2', True, '', '', 'bibliografia 20');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (37, 'urlImagen 3');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (35, 37);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (False, '2013-07-28', 37, False, True, 'urlImagen 7');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 1', '', True, 37, True, True, 'nombre 1', True, True, 'otros 9', False);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (37, 22);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('', '', False, '', False, True, True, 'descripcionCeramica 7', '', 37, 'descripcionCarbon 14', 'descripcionOseo 15', False, False, '', '', True, False);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, 'tipo 7', True, False, False, False, 37, False, False, '', True);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, True, 'orientacion 10', 37, False, False, False, 'otros 12');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (37, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (37, 'tecnicas 2');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, 'tecnicas 6', True, 37, 'otros 9', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, '', 37, False, True);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, True, 'esTenenciaOtros 11', 37, True, True, True);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, 'observaciones 14', 37, True, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, False, False, True, False, 37, True, False, False);

---------- Fin Insert Yacimiento 37

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (38, 38, 'Venezuela', 'Yacimiento 38', 'Municipio 12', 'Carabobo'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', 'desnivel 10', 'texto 3', 38, 'superficie 17', 'altura 5');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (True, False, True, True, True, 'anchoDe 17', 'anchoDeComp 20', 'anchoA 5', 38, False, 'anchoAComp 13', True, False, '', True);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, True, NULL, True, False, NULL, 38, NULL, True, 28);

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 3', 38, 'diametro 5', 'ancho 9', '');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 2', 'profundidad 8', 'diametro 5', 38, 'otros 17', 'largo 1');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 38, '');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 11', 'utmAdicional 5', 38, 'longitud 4');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (38, 'urlImagen 18');

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-05-10', 38, False, False, 'urlImagen 18');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 4', '', True, 38, False, True, 'nombre 8', False, True, 'otros 18', False);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (38, '', '');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', False, False, 38, 'nombrePoblado 20', True, True, False);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (38, NULL);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('', 'descripcionCementerio 1', True, 'descripcionMito 15', True, True, False, 'descripcionCeramica 7', '', 38, '', '', True, True, '', 'descripcionLitica 8', False, True);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, '', True, True, True, False, 38, False, True, '', True);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, False, 'orientacion 5', 38, False, False, True, 'otros 17');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (38, '');

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, '', 38, True, False);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, True, '', 38, False, False, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, False, True, True, False, 38, False, False, False);

---------- Fin Insert Yacimiento 38

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (39, 39, 'Venezuela', 'Yacimiento 39', 'Municipio 4', 'Monagas'); 

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (True, True, False, True, True, 'anchoDe 2', 'anchoDeComp 15', 'anchoA 11', 39, False, 'anchoAComp 4', True, True, '', True);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 10', 39, 'diametro 7', 'ancho 6');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 16', 39, 'diametro 20', 'ancho 5', 'profundidad 10');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 10', 'profundidad 3', 'diametro 12', 39, '', 'largo 17');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 2', False, 39, 'diametro 8', 'profundidad 9');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 18', 'autor 6', True, '', True, 'fecha 13', True, False, True, 39, 'facebook 4', False, 'mail 14', '', '', True, '', 'twitter 12', '');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (39, '');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('fauna 2', 39);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 12', 39);

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', True, False, 39, '', True, True, True);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 17', 'descripcionCementerio 2', True, 'descripcionMito 19', False, True, False, '', 'descripcionMonticulo 3', 39, 'descripcionCarbon 3', '', True, False, 'otros 1', '', True, False);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, '', True, True, True, True, 39, False, False, '', True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (39, 'notas 4');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (39, 'tecnicas 2');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, True, False, True, 39, True, False, '', True);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, '', True, 39, '', True);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, True, False, 39, False, True, '', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, 'otros 1', 39, False, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, False, False, '', 39, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (True, 'observaciones 6', 39, True, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, True, False, True, False, 39, True, True, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (39, 16);

---------- Fin Insert Yacimiento 39

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (40, 40, 'Venezuela', 'Yacimiento 40', 'Municipio 9', 'Guárico'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 1', '', 'texto 3', 40, 'superficie 19', 'altura 15');

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 40, NULL, 30);

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 2', 'profundidad 9', 'diametro 15', 40, 'otros 17', 'largo 6');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (40, 20, NULL, NULL, '', 13);

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', 'autor 9', True, 'institucion 18', True, 'fecha 14', False, True, True, 40, 'facebook 10', False, '', '', 'pais 6', True, 'telefono 13', '', '');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (33, False, NULL, False, 36, 'perdidoPa 11', '', True, True, True, False, 'otros 7', 'especificar 10', False, NULL, True, 31, NULL, True, 40, True, True, False, NULL, False, True, '', False, False, 'observaciones 17', False, True, False, False, False, 'destruidoPa 1', False, True, False, True, '', True, 'trasladadoPa 3', '', True, True, 24, False, 'erosionPa 4', True, 'crecimientoVegPa 3');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('', 40);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 40);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 6', '', True, 40, False, False, 'nombre 19', False, False, '', True);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (40, 'direcciones 2', '');

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 13', 'descripcionCementerio 6', True, 'descripcionMito 13', False, False, True, 'descripcionCeramica 11', '', 40, '', '', False, True, '', 'descripcionLitica 19', False, False);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, 'tipo 2', True, False, False, False, 40, False, True, 'otros 19', False);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (40, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (40, 'numeroPlano 13');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, True, False, 40, False, False, '', False);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, False, False, 40, True, False, '', False);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (True, False, True, '', 40, True);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 40, True, True, True, False, True);

---------- Fin Insert Yacimiento 40

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (41, 41, 'Venezuela', 'Yacimiento 41', 'Municipio 6', 'Yaracuy'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 2', '', 'texto 1', 41, 'superficie 8', 'altura 15');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, True, True, False, True, 'anchoDe 4', 'anchoDeComp 6', 'anchoA 17', 41, True, 'anchoAComp 7', False, False, '', False);

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 41, 4, 7, True);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 41, 1, 31);

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 3', 41, 'ancho 7');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 41, 'otros 7');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (41, 15, NULL, 12, '', NULL);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 19', '', 41, 'longitud 2');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', 'autor 15', True, '', True, 'fecha 15', True, True, False, 41, '', False, '', '', '', True, 'telefono 5', '', 'bibliografia 19');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (NULL, 41);

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, True, 40, True, 7, '', 'sumergidoPa 7', True, False, False, False, '', 'especificar 6', False, NULL, False, 10, 37, True, 41, True, True, True, NULL, False, False, '', False, False, '', False, True, False, False, True, '', False, False, True, True, 'patinaPa 7', True, '', '', True, False, 12, False, '', True, 'crecimientoVegPa 19');

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-05-26', 41, False, True, 'urlImagen 13');

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (41, 'direcciones 17', 'puntoDatum 3');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', False, False, 41, '', True, False, True);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, '', True, False, False, True, 41, False, False, 'otros 6', False);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (41, 'notas 2');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (41, 'numeroPlano 13');

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, 'otros 13', 41, False, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, False, False, 'mixto 15', 41, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (41, 10);

---------- Fin Insert Yacimiento 41

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (42, 42, 'Venezuela', 'Yacimiento 42', 'Municipio 5', 'Monagas'); 

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 3', '', 'diametro 20', 42, '', 'largo 15');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('', True, 42, 'diametro 20', 'profundidad 7');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (42, 11, NULL, 21, 'otros 15', NULL);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 1', '', 42, 'longitud 5');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, False, NULL, False, 40, 'perdidoPa 2', '', False, True, True, True, '', 'especificar 12', True, 8, False, 25, 29, True, 42, False, False, False, NULL, False, False, 'mas 8', False, True, 'observaciones 14', False, True, True, False, True, '', False, False, False, True, 'patinaPa 18', False, 'trasladadoPa 15', '', False, True, NULL, True, 'erosionPa 12', True, 'crecimientoVegPa 5');

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 1', 42);

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', True, True, 42, 'nombrePoblado 8', False, True, False);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 7', 'descripcionCementerio 9', True, 'descripcionMito 9', True, True, True, 'descripcionCeramica 15', 'descripcionMonticulo 13', 42, '', 'descripcionOseo 4', False, False, 'otros 9', 'descripcionLitica 10', True, True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (42, '');

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, True, False, True, 42, True, True, '', False);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (True, True, False, 'mixto 10', 42, True);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, '', 42, False, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (42, NULL);

---------- Fin Insert Yacimiento 42

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (43, 43, 'Venezuela', 'Yacimiento 43', 'Municipio 18', 'Sucre'); 

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (True, 43, 33, 13, True);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 12', 43, 'diametro 2', 'ancho 12');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 2', 43, 'diametro 20', 'ancho 8', 'profundidad 6');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 9', 'profundidad 10', 'diametro 9', 43, 'otros 17', 'largo 15');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 4', 43, 'ancho 6');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 43, '');

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (False, '2013-01-05', 43, False, True, 'urlImagen 8');

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (43, '', '');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('nombreNoPoblado 12', False, False, 43, '', True, False, False);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (43, 26);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 3', 'descripcionCementerio 6', True, '', True, False, True, 'descripcionCeramica 3', '', 43, 'descripcionCarbon 1', '', False, True, '', 'descripcionLitica 7', True, False);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, False, 'orientacion 2', 43, False, False, True, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (43, 'numeroPlano 2');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (43, 'tecnicas 6');

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, '', 43, False, True);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (True, '', 43, False, False);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 43, False, True, True, True, False);

---------- Fin Insert Yacimiento 43

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (44, 44, 'Venezuela', 'Yacimiento 44', 'Municipio 6', 'Portuguesa'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 13', '', 'texto 17', 44, 'superficie 8', 'altura 16');

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 44, 15, 16, False);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 2', 44, 'diametro 11', 'ancho 18');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 10', 44, 'diametro 6', 'ancho 5', 'profundidad 8');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 19', 'profundidad 16', 'diametro 14', 44, 'otros 18', 'largo 2');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 4', 44, 'ancho 2');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('', True, 44, 'diametro 8', 'profundidad 15');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 44, '');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (44, 29, NULL, NULL, '', 12);

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 5', '', True, 'institucion 9', True, 'fecha 14', True, True, True, 44, 'facebook 10', True, 'mail 2', 'direccion 19', 'pais 17', False, 'telefono 5', 'twitter 9', 'bibliografia 10');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (39, 44);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 4', '', True, 44, True, False, 'nombre 6', False, True, '', False);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (44, '', 'puntoDatum 14');

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('', '', False, '', False, True, False, 'descripcionCeramica 9', 'descripcionMonticulo 12', 44, 'descripcionCarbon 2', '', False, True, 'otros 11', '', False, True);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (True, 'tipo 19', False, False, False, True, 44, False, False, '', True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (44, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (44, 'numeroPlano 7');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (False, 'tecnicas 3', False, 44, 'otros 15', True);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, False, False, 44, False, True, '', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, '', 44, True, True);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (False, False, '', 44, False, True, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, '', 44, True, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, True, False, True, True, 44, True, True, False);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 44, False, False, True, True, True);

---------- Fin Insert Yacimiento 44

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (45, 45, 'Venezuela', 'Yacimiento 45', 'Municipio 16', 'Yaracuy'); 

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, True, 27, False, False, NULL, 45, NULL, True, 35);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 3', 45, 'diametro 3', 'ancho 6');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 17', 45, 'diametro 3', 'ancho 15', 'profundidad 17');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 1', 'profundidad 6', 'diametro 15', 45, 'otros 16', 'largo 4');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, True, False, True, False, False, False, False, True, '', 'anchoA 14', 'profundidadA 7', 45, True, True, 'anchoDe 13', True, False, True);

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 45, 'otros 6');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (45, 10, 12, 14, '', NULL);

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (27, 45);

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, True, NULL, False, 12, '', 'sumergidoPa 9', False, True, True, True, '', '', True, 11, False, 32, 29, False, 45, False, True, True, 3, True, True, 'mas 1', False, False, 'observaciones 4', True, False, False, False, False, '', True, True, False, True, 'patinaPa 17', True, 'trasladadoPa 5', 'enterradoPa 11', True, False, 15, False, '', False, '');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('', 45);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 45);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (False, '2013-06-21', 45, False, False, 'urlImagen 1');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 9', '', True, 45, False, True, 'nombre 6', True, True, 'otros 11', True);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (45, '', 'puntoDatum 2');

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (45, NULL);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('', 'descripcionCementerio 17', False, '', False, False, False, '', 'descripcionMonticulo 6', 45, '', '', False, True, 'otros 20', 'descripcionLitica 5', False, True);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, '', True, False, True, False, 45, True, False, 'otros 4', True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (45, 'notas 16');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, False, 'orientacion 2', 45, True, False, True, 'otros 6');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (45, '');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (False, 'tecnicas 17', True, 45, '', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, 'otros 4', 45, False, False);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (False, False, '', 45, False, True, False);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, False, False, 'mixto 12', 45, False);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 45, True, True, False, True, False);

---------- Fin Insert Yacimiento 45

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (46, 46, 'Venezuela', 'Yacimiento 46', 'Municipio 12', 'Aragua'); 

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 46, NULL, 13);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 2', 46, 'diametro 7', 'ancho 2');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 11', 46, 'diametro 2', 'ancho 7', 'profundidad 16');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 3', 46, 'ancho 8');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 18', False, 46, 'diametro 1', '');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 46, '');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (46, NULL, 21, 5, 'otros 15', NULL);

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (46, 'urlImagen 13');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (29, False, NULL, False, NULL, '', 'sumergidoPa 13', True, True, True, False, '', 'especificar 1', False, NULL, True, NULL, 35, True, 46, True, False, True, NULL, False, True, '', False, True, 'observaciones 18', False, True, False, False, True, '', False, False, False, True, '', True, '', 'enterradoPa 13', True, True, 9, False, 'erosionPa 20', True, '');

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 46);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (46, '', '');

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (46, NULL);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('', 'descripcionCementerio 19', True, 'descripcionMito 11', False, True, True, 'descripcionCeramica 4', '', 46, '', 'descripcionOseo 16', False, True, 'otros 17', 'descripcionLitica 1', True, False);

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (46, '');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (False, '', True, 46, '', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, 'otros 9', 46, False, True);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (True, '', 46, True, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (46, NULL);

---------- Fin Insert Yacimiento 46

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (47, 47, 'Venezuela', 'Yacimiento 47', 'Municipio 7', 'Trujillo'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', 'desnivel 9', 'texto 2', 47, 'superficie 7', 'altura 13');

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, True, NULL, True, True, 37, 47, NULL, True, 14);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 18', 47, 'diametro 1', 'ancho 15');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (True, False, False, True, True, True, True, True, True, '', 'anchoA 9', 'profundidadA 14', 47, False, False, 'anchoDe 16', False, False, False);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 12', True, 47, 'diametro 16', 'profundidad 2');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 47, '');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (47, 7, 16, NULL, '', NULL);

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', '', False, 'institucion 16', True, 'fecha 5', False, False, False, 47, 'facebook 2', True, '', 'direccion 13', '', False, '', '', '');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, True, NULL, True, 11, '', '', True, False, False, False, 'otros 6', 'especificar 8', False, NULL, True, NULL, 28, False, 47, True, False, False, 14, False, True, 'mas 12', False, True, '', False, False, True, False, False, 'destruidoPa 11', False, True, True, False, 'patinaPa 17', False, 'trasladadoPa 13', 'enterradoPa 19', True, True, 1, True, 'erosionPa 13', True, 'crecimientoVegPa 10');

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (False, '2013-09-25', 47, True, False, 'urlImagen 7');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', True, False, 47, 'nombrePoblado 11', False, True, True);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('', '', False, '', True, True, True, '', 'descripcionMonticulo 5', 47, '', '', True, True, '', 'descripcionLitica 3', True, True);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, '', True, False, True, True, 47, False, True, 'otros 8', True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (47, '');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, True, 'orientacion 12', 47, False, False, False, 'otros 19');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (47, 'numeroPlano 10');

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, '', 47, True, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, False, True, False, True, 47, False, False, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (47, NULL);

---------- Fin Insert Yacimiento 47

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (48, 48, 'Venezuela', 'Yacimiento 48', 'Municipio 3', 'Mérida'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 13', 'desnivel 10', 'texto 2', 48, 'superficie 4', 'altura 19');

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 48, NULL, 23, False);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, False, NULL, False, False, 22, 48, NULL, False, NULL);

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 20', 48, 'diametro 12', 'ancho 20', '');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 12', 'profundidad 14', 'diametro 1', 48, '', 'largo 20');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 20', False, 48, 'diametro 1', 'profundidad 7');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 48, '');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (48, 26, NULL, 40, 'otros 18', NULL);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 2', '', 48, 'longitud 18');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', 'autor 14', True, 'institucion 6', False, 'fecha 1', False, False, False, 48, 'facebook 10', True, 'mail 14', '', '', True, 'telefono 12', '', 'bibliografia 16');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (48, '');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, False, 4, True, NULL, '', '', True, True, True, True, 'otros 3', '', False, NULL, False, 17, 31, False, 48, False, True, True, NULL, True, True, '', False, True, '', False, True, True, False, False, '', False, True, False, True, '', False, 'trasladadoPa 15', '', True, False, 16, True, 'erosionPa 14', True, 'crecimientoVegPa 4');

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 48);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 4', '', True, 48, True, False, 'nombre 6', True, False, 'otros 7', True);

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', False, False, 48, '', False, False, False);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 18', 'descripcionCementerio 9', False, 'descripcionMito 3', False, True, False, 'descripcionCeramica 18', '', 48, 'descripcionCarbon 14', '', False, True, 'otros 2', '', True, True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (48, 'notas 8');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (48, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, False, False, 48, True, False, '', True);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (False, 'tecnicas 14', True, 48, 'otros 10', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, 'otros 8', 48, False, False);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, True, '', 48, True, False, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, True, True, False, True, 48, True, False, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (48, 2);

---------- Fin Insert Yacimiento 48

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (49, 49, 'Venezuela', 'Yacimiento 49', 'Municipio 5', 'Apure'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 16', '', 'texto 11', 49, 'superficie 12', 'altura 8');

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (True, 49, 37, NULL, False);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 49, 5, 38);

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 5', 49, 'diametro 8', 'ancho 10', '');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 3', 49, 'ancho 9');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('', False, 49, 'diametro 5', 'profundidad 4');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 10', 'utmAdicional 4', 49, 'longitud 11');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 4', '', True, 'institucion 20', True, 'fecha 5', True, False, False, 49, 'facebook 16', True, 'mail 8', 'direccion 15', '', False, '', 'twitter 5', '');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (24, False, NULL, True, NULL, 'perdidoPa 12', '', True, True, False, False, 'otros 1', '', True, 35, True, NULL, NULL, False, 49, False, True, True, 26, False, False, '', True, False, 'observaciones 19', True, False, True, True, True, '', True, True, False, True, '', True, '', 'enterradoPa 20', True, False, 6, False, 'erosionPa 1', False, 'crecimientoVegPa 14');

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 14', 49);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 1', '', True, 49, True, True, 'nombre 9', True, False, '', False);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (49, NULL);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (49, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (49, 'numeroPlano 16');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (49, '');

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, True, True, 49, True, True, 'otros 17', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, '', 49, False, False);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, True, False, '', 49, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, '', 49, False, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, False, True, False, True, 49, False, True, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (49, NULL);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 49, True, False, False, True, True);

---------- Fin Insert Yacimiento 49

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (50, 50, 'Venezuela', 'Yacimiento 50', 'Municipio 2', 'Yaracuy'); 

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 50, 19, 12, False);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (28, False, NULL, True, False, 34, 50, 20, False, NULL);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 50, 36, 14);

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 4', 50, 'ancho 11');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 1', True, 50, 'diametro 4', 'profundidad 11');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 50, '');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (50, NULL, NULL, 35, 'otros 3', 34);

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (50, 'urlImagen 13');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, True, NULL, False, 6, '', '', True, True, False, False, 'otros 18', 'especificar 12', True, 34, True, 35, 35, False, 50, False, True, True, 14, True, True, '', False, False, '', True, False, True, True, True, 'destruidoPa 13', False, False, True, True, '', True, 'trasladadoPa 17', 'enterradoPa 10', True, False, NULL, True, 'erosionPa 1', True, '');

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (False, '2013-04-26', 50, False, False, 'urlImagen 7');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 11', 'observaciones 11', False, 50, True, False, 'nombre 12', True, True, '', True);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('', '', True, '', False, False, False, 'descripcionCeramica 5', '', 50, '', '', False, False, 'otros 1', 'descripcionLitica 8', True, False);

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (50, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, True, False, 50, False, True, '', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, '', 50, False, True);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (False, False, '', 50, True, True, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, False, True, '', 50, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (True, '', 50, False, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, True, True, False, False, 50, False, True, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (50, NULL);

---------- Fin Insert Yacimiento 50

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (51, 51, 'Venezuela', 'Yacimiento 51', 'Municipio 20', 'Monagas'); 

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, False, True, True, False, 'anchoDe 13', 'anchoDeComp 2', 'anchoA 13', 51, False, 'anchoAComp 2', True, True, '', False);

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 51, NULL, 34, True);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (25, True, 18, False, False, NULL, 51, NULL, True, 19);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 51, 25, 33);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 14', 51, 'diametro 15', 'ancho 20');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 16', 51, 'diametro 19', 'ancho 11', 'profundidad 5');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 6', True, 51, 'diametro 19', '');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 51, '');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (51, 6, NULL, 15, 'otros 8', 33);

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 13', 'autor 15', False, '', False, 'fecha 5', False, False, False, 51, 'facebook 11', True, 'mail 20', '', '', False, 'telefono 7', '', 'bibliografia 2');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (51, 'urlImagen 15');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (9, 51);

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, False, NULL, True, NULL, '', 'sumergidoPa 17', True, True, False, True, 'otros 12', 'especificar 5', False, NULL, False, 26, 1, False, 51, False, False, True, 7, False, False, 'mas 14', False, True, 'observaciones 6', False, True, True, True, True, 'destruidoPa 17', False, False, False, True, 'patinaPa 5', False, 'trasladadoPa 8', 'enterradoPa 17', True, True, NULL, False, 'erosionPa 7', False, '');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('', 51);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 51);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (False, '2013-05-27', 51, False, False, '');

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (51, 13);

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (51, 'numeroPlano 19');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (51, '');

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, True, False, False, 51, False, True, '', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, 'otros 3', 51, False, False);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (False, True, '', 51, True, False, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (51, 32);

---------- Fin Insert Yacimiento 51

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (52, 52, 'Venezuela', 'Yacimiento 52', 'Municipio 14', 'Lara'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 8', '', 'texto 2', 52, 'superficie 17', 'altura 20');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, False, False, False, True, 'anchoDe 6', 'anchoDeComp 3', 'anchoA 7', 52, False, 'anchoAComp 4', True, False, 'otros 13', False);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 52, NULL, 5);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 20', 52, 'diametro 14', 'ancho 8');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 13', 52, 'diametro 2', 'ancho 8', '');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 5', 52, 'ancho 13');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (True, True, True, True, False, True, True, True, False, '', 'anchoA 11', 'profundidadA 13', 52, True, True, 'anchoDe 2', False, False, False);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('', False, 52, 'diametro 8', '');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 6', 'utmAdicional 18', 52, 'longitud 6');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 10', '', False, '', False, 'fecha 3', False, False, True, 52, 'facebook 10', True, 'mail 8', 'direccion 17', 'pais 16', False, '', '', 'bibliografia 1');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (52, '');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (7, False, 14, True, NULL, '', 'sumergidoPa 1', True, True, True, True, 'otros 14', 'especificar 2', False, NULL, True, 23, 18, False, 52, True, False, False, 15, True, True, 'mas 17', False, True, 'observaciones 20', True, True, True, False, False, 'destruidoPa 17', False, True, False, True, '', False, 'trasladadoPa 14', 'enterradoPa 16', True, False, NULL, True, '', False, 'crecimientoVegPa 20');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('', 52);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 6', '', False, 52, False, False, 'nombre 4', True, False, 'otros 12', True);

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', False, False, 52, '', True, True, True);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (52, NULL);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 9', 'descripcionCementerio 13', False, '', True, False, True, 'descripcionCeramica 9', '', 52, 'descripcionCarbon 4', '', False, True, 'otros 20', 'descripcionLitica 14', True, False);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (52, '');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, True, 'orientacion 14', 52, True, False, False, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (52, 'numeroPlano 9');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (52, 'tecnicas 15');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, True, True, False, 52, False, True, 'otros 4', True);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, '', True, 52, '', False);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (False, False, '', 52, True, True, False);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, True, False, '', 52, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, 'observaciones 10', 52, True, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, True, True, False, True, 52, False, False, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (52, 34);

---------- Fin Insert Yacimiento 52

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (53, 53, 'Venezuela', 'Yacimiento 53', 'Municipio 20', 'Aragua'); 

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (True, True, False, False, True, 'anchoDe 20', 'anchoDeComp 12', 'anchoA 11', 53, True, 'anchoAComp 20', True, True, '', False);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 53, 29, 36);

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 17', '', 'diametro 13', 53, '', 'largo 19');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('', True, 53, 'diametro 20', '');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (53, 27, NULL, NULL, 'otros 18', 2);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 17', 'utmAdicional 18', 53, 'longitud 3');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (53, '');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (2, True, 22, True, NULL, '', '', True, False, False, True, '', 'especificar 18', False, 34, False, 17, 16, False, 53, False, False, False, NULL, True, True, '', False, True, '', False, False, True, True, False, 'destruidoPa 15', False, False, True, True, '', True, '', 'enterradoPa 17', True, True, NULL, False, 'erosionPa 13', True, 'crecimientoVegPa 13');

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-10-02', 53, False, False, '');

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (53, '', '');

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 16', '', True, '', True, False, False, '', '', 53, 'descripcionCarbon 16', 'descripcionOseo 17', False, True, '', 'descripcionLitica 18', True, True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (53, 'notas 12');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, False, 'orientacion 18', 53, False, False, False, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (53, 'tecnicas 1');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, False, False, 53, True, True, '', False);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (False, 'tecnicas 8', True, 53, 'otros 14', False);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (False, True, 'esTenenciaOtros 15', 53, False, False, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, True, False, 'mixto 16', 53, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (True, 'observaciones 18', 53, True, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (53, NULL);

---------- Fin Insert Yacimiento 53

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (54, 54, 'Venezuela', 'Yacimiento 54', 'Municipio 16', 'Guárico'); 

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 54, 10, 13, True);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 54, NULL, 9);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 17', 54, 'diametro 3', 'ancho 8');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (54, 'urlImagen 16');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, False, NULL, False, 28, 'perdidoPa 20', '', False, True, True, True, 'otros 10', '', False, NULL, False, NULL, 19, True, 54, False, False, True, NULL, True, False, '', False, False, 'observaciones 18', True, False, True, True, True, 'destruidoPa 5', False, False, False, True, 'patinaPa 7', True, 'trasladadoPa 6', '', False, True, 38, False, 'erosionPa 4', False, '');

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (54, NULL);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 20', 'descripcionCementerio 16', False, '', True, False, True, '', 'descripcionMonticulo 20', 54, 'descripcionCarbon 4', 'descripcionOseo 4', True, False, 'otros 2', 'descripcionLitica 7', False, False);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, 'tipo 11', True, False, True, False, 54, False, True, '', True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (54, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (54, 'numeroPlano 5');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, True, False, 54, True, True, 'otros 15', False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, False, True, False, True, 54, False, True, True);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 54, False, True, False, True, False);

---------- Fin Insert Yacimiento 54

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (55, 55, 'Venezuela', 'Yacimiento 55', 'Municipio 7', 'Yaracuy'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 8', '', 'texto 10', 55, 'superficie 3', 'altura 13');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, False, False, True, True, 'anchoDe 19', 'anchoDeComp 16', 'anchoA 16', 55, False, 'anchoAComp 2', True, False, '', True);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (17, False, 3, False, False, NULL, 55, 37, False, NULL);

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 7', 'profundidad 17', 'diametro 16', 55, 'otros 20', 'largo 20');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 9', False, 55, 'diametro 7', 'profundidad 2');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 55, '');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', '', False, 'institucion 19', True, 'fecha 18', False, False, False, 55, '', True, 'mail 9', 'direccion 10', '', False, '', 'twitter 20', 'bibliografia 4');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (1, 55);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (55, 'direcciones 20', 'puntoDatum 12');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', False, False, 55, '', False, False, True);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('', 'descripcionCementerio 10', True, '', True, False, True, 'descripcionCeramica 9', '', 55, 'descripcionCarbon 15', 'descripcionOseo 3', True, False, '', 'descripcionLitica 1', True, True);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (True, 'tipo 16', False, True, True, False, 55, False, True, '', False);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (55, '');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, False, 'orientacion 8', 55, True, False, False, 'otros 2');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (55, 'numeroPlano 19');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (55, '');

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, True, 'esTenenciaOtros 13', 55, False, True, True);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 55, True, False, False, True, True);

---------- Fin Insert Yacimiento 55

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (56, 56, 'Venezuela', 'Yacimiento 56', 'Municipio 6', 'Tachira'); 

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 56, 20, 24);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 18', 56, 'diametro 8', 'ancho 18');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 11', 56, 'diametro 3', 'ancho 6', 'profundidad 12');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 13', 'profundidad 8', 'diametro 20', 56, '', 'largo 14');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, True, True, True, False, False, True, False, True, '', 'anchoA 1', 'profundidadA 11', 56, True, False, 'anchoDe 17', False, False, True);

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 56, 'otros 2');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (56, NULL, 14, 1, '', NULL);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 18', '', 56, 'longitud 2');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (56, 'urlImagen 8');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (4, 56);

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, True, 15, False, NULL, '', '', True, False, True, True, '', 'especificar 3', False, 31, True, NULL, 11, True, 56, False, True, False, 17, True, False, 'mas 20', False, True, 'observaciones 10', True, False, False, False, True, 'destruidoPa 6', True, True, False, False, 'patinaPa 6', False, 'trasladadoPa 2', 'enterradoPa 18', True, False, 17, False, 'erosionPa 17', False, '');

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-04-29', 56, False, False, 'urlImagen 11');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 11', '', True, 56, False, True, 'nombre 6', False, False, 'otros 6', True);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (56, 'direcciones 1', 'puntoDatum 1');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', False, False, 56, 'nombrePoblado 19', False, True, False);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (56, 29);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 15', 'descripcionCementerio 4', True, 'descripcionMito 15', True, True, False, 'descripcionCeramica 7', 'descripcionMonticulo 18', 56, '', 'descripcionOseo 18', True, False, '', 'descripcionLitica 16', True, True);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, False, 'orientacion 2', 56, True, True, False, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (56, '');

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, '', 56, False, True);

---------- Fin Insert Yacimiento 56

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (57, 57, 'Venezuela', 'Yacimiento 57', 'Municipio 13', 'Monagas'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 4', '', 'texto 11', 57, 'superficie 6', 'altura 1');

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (23, True, NULL, False, False, NULL, 57, 1, True, NULL);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 57, NULL, 15);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 6', 57, 'diametro 13', 'ancho 1');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 9', 57, 'diametro 11', 'ancho 11', '');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 15', 'profundidad 9', 'diametro 17', 57, 'otros 15', 'largo 3');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 10', 57, 'ancho 2');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (True, True, False, False, False, False, True, False, False, 'produndidadDe 17', 'anchoA 3', 'profundidadA 10', 57, True, False, 'anchoDe 14', True, True, False);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('', False, 57, 'diametro 3', '');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (57, NULL, 21, NULL, 'otros 15', 35);

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (19, 57);

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('', 57);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 11', 57);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-10-21', 57, True, False, '');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 17', 'observaciones 17', False, 57, False, True, 'nombre 4', False, False, 'otros 3', True);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (57, '', 'puntoDatum 12');

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (57, NULL);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 4', 'descripcionCementerio 8', True, 'descripcionMito 3', False, False, True, 'descripcionCeramica 3', '', 57, 'descripcionCarbon 9', 'descripcionOseo 11', False, True, '', '', False, False);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, True, 'orientacion 5', 57, False, False, False, 'otros 13');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (57, 'numeroPlano 8');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (57, 'tecnicas 17');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, False, True, 57, True, False, '', False);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (False, True, 'esTenenciaOtros 16', 57, True, False, False);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, False, True, 'mixto 15', 57, True);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (True, 'observaciones 17', 57, False, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, True, False, True, False, 57, True, True, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (57, NULL);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 57, True, True, True, False, False);

---------- Fin Insert Yacimiento 57

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (58, 58, 'Venezuela', 'Yacimiento 58', 'Municipio 3', 'Delta Amacuro'); 

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 58, NULL, NULL, False);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (9, False, NULL, False, True, 11, 58, 6, True, 40);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 58, NULL, 33);

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 18', 'profundidad 8', 'diametro 17', 58, '', 'largo 15');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, False, True, False, True, True, False, True, False, 'produndidadDe 9', 'anchoA 7', 'profundidadA 20', 58, False, False, 'anchoDe 16', False, True, False);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 6', False, 58, 'diametro 16', '');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 6', 'autor 15', False, 'institucion 8', True, 'fecha 7', True, True, True, 58, 'facebook 19', True, '', '', '', False, 'telefono 16', '', 'bibliografia 14');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (58, '');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('', 58);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-06-26', 58, True, True, '');

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (58, '', '');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, False, 'orientacion 14', 58, False, True, False, '');

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, False, False, 58, False, True, '', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, '', 58, True, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, True, True, True, False, 58, True, True, False);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 58, True, False, True, True, False);

---------- Fin Insert Yacimiento 58

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (59, 59, 'Venezuela', 'Yacimiento 59', 'Municipio 12', 'Miranda'); 

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 59, NULL, 13, False);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, True, NULL, False, True, 36, 59, NULL, True, NULL);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 1', 59, 'diametro 5', 'ancho 6');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 15', 59, 'diametro 1', 'ancho 10', '');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 12', '', 'diametro 7', 59, 'otros 3', 'largo 1');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (59, 27, NULL, NULL, '', NULL);

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', '', False, '', True, 'fecha 14', False, True, True, 59, '', False, '', '', 'pais 5', False, '', '', 'bibliografia 5');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (59, 'urlImagen 12');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (NULL, 59);

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (5, False, NULL, True, NULL, 'perdidoPa 1', '', False, False, True, False, 'otros 15', 'especificar 5', False, NULL, True, NULL, 18, False, 59, True, False, True, 34, False, True, '', False, False, 'observaciones 6', False, True, True, True, False, 'destruidoPa 19', False, True, True, True, '', True, '', '', False, True, 10, True, 'erosionPa 11', True, 'crecimientoVegPa 15');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('fauna 15', 59);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 59);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 12', '', True, 59, False, False, 'nombre 15', True, True, '', True);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (59, '', 'puntoDatum 19');

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (59, NULL);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('', 'descripcionCementerio 9', False, '', False, False, False, 'descripcionCeramica 18', 'descripcionMonticulo 14', 59, '', '', False, True, 'otros 1', '', True, True);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (True, 'tipo 10', False, True, True, True, 59, True, True, 'otros 2', True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (59, '');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, False, 'orientacion 6', 59, False, False, False, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (59, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (59, 'tecnicas 20');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, True, False, 59, True, True, '', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, 'otros 14', 59, True, True);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, '', 59, True, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, True, True, False, True, 59, False, False, False);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 59, True, True, False, False, False);

---------- Fin Insert Yacimiento 59

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (60, 60, 'Venezuela', 'Yacimiento 60', 'Municipio 13', 'Cojedes'); 

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, False, True, False, True, 'anchoDe 17', 'anchoDeComp 4', 'anchoA 17', 60, True, 'anchoAComp 9', False, True, 'otros 5', False);

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (True, 60, 19, NULL, False);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 60, 16, 12);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 6', 60, 'diametro 15', 'ancho 18');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 18', 60, 'diametro 8', 'ancho 6', '');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 15', '', 'diametro 3', 60, '', 'largo 13');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (NULL, 60);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 5', 60);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 4', 'observaciones 19', False, 60, False, False, 'nombre 1', True, True, 'otros 16', True);

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', False, True, 60, 'nombrePoblado 6', True, True, True);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (60, NULL);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, 'tipo 4', False, False, False, True, 60, True, False, '', True);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, False, 'orientacion 6', 60, False, False, True, '');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, '', False, 60, 'otros 17', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, '', 60, True, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (True, 'observaciones 12', 60, False, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (60, 30);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 60, True, False, True, False, False);

---------- Fin Insert Yacimiento 60

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (61, 61, 'Venezuela', 'Yacimiento 61', 'Municipio 1', 'Anzoategui'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 14', 'desnivel 20', 'texto 19', 61, 'superficie 1', 'altura 14');

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 61, NULL, 38);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 8', 61, 'diametro 3', 'ancho 6');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 13', 'profundidad 13', 'diametro 6', 61, 'otros 10', 'largo 6');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 7', 61, 'ancho 13');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (True, False, False, True, False, True, True, False, False, 'produndidadDe 18', 'anchoA 16', 'profundidadA 20', 61, False, True, 'anchoDe 9', False, False, False);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('', True, 61, 'diametro 19', 'profundidad 11');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (61, NULL, 31, 7, '', 26);

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, False, NULL, True, 3, 'perdidoPa 8', '', True, False, False, True, '', '', False, NULL, False, NULL, NULL, True, 61, False, True, True, 7, True, False, '', True, True, 'observaciones 1', False, False, False, True, True, 'destruidoPa 9', True, True, True, True, '', True, '', 'enterradoPa 8', False, False, NULL, True, 'erosionPa 1', True, 'crecimientoVegPa 17');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('fauna 20', 61);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-02-12', 61, True, True, '');

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (True, 'tipo 20', True, False, False, True, 61, True, True, 'otros 15', False);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (61, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (61, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (61, 'tecnicas 14');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, '', True, 61, '', True);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, True, False, 61, True, True, '', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, '', 61, False, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, '', 61, False, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, False, False, False, False, 61, False, True, False);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 61, False, True, True, True, True);

---------- Fin Insert Yacimiento 61

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (62, 62, 'Venezuela', 'Yacimiento 62', 'Municipio 8', 'Sucre'); 

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (True, 62, 34, 18, False);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 62, NULL, 14);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 20', 62, 'diametro 6', 'ancho 15');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (True, True, True, False, False, True, False, False, True, '', 'anchoA 14', 'profundidadA 11', 62, False, False, 'anchoDe 20', True, False, False);

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 62, '');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 9', 'utmAdicional 1', 62, 'longitud 9');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (62, 'urlImagen 1');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (19, 62);

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, True, NULL, False, NULL, 'perdidoPa 14', '', True, False, True, True, '', '', False, NULL, True, NULL, NULL, True, 62, False, True, True, 13, True, False, '', True, True, 'observaciones 2', False, True, False, False, False, 'destruidoPa 8', True, False, False, False, '', True, 'trasladadoPa 19', '', False, True, 29, True, '', True, '');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('', 62);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 62);

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', True, True, 62, 'nombrePoblado 19', True, True, False);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 5', 'descripcionCementerio 3', True, 'descripcionMito 4', True, False, True, 'descripcionCeramica 16', '', 62, '', '', False, False, 'otros 13', 'descripcionLitica 6', False, True);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, True, 'orientacion 13', 62, True, True, True, 'otros 16');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (62, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (62, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, False, False, 62, True, False, '', True);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, False, False, 62, False, True, 'otros 2', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, '', 62, False, False);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, False, '', 62, True, False, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, True, False, 'mixto 15', 62, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, True, False, False, False, 62, True, True, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (62, 38);

---------- Fin Insert Yacimiento 62

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (63, 63, 'Venezuela', 'Yacimiento 63', 'Municipio 20', 'Amazonas'); 

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 63, 16, 27);

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 10', 63, 'ancho 19');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 2', False, 63, 'diametro 11', '');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (63, NULL, 40, NULL, 'otros 15', NULL);

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (20, False, NULL, False, 31, 'perdidoPa 1', 'sumergidoPa 10', False, True, True, False, '', '', True, NULL, True, NULL, 32, True, 63, False, False, False, NULL, False, True, 'mas 2', True, True, '', True, True, False, False, True, 'destruidoPa 4', True, True, False, True, '', True, 'trasladadoPa 15', 'enterradoPa 8', True, False, NULL, False, '', True, '');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('', 63);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 4', 63);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (False, '2013-10-19', 63, False, True, 'urlImagen 10');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 16', 'observaciones 3', True, 63, False, False, 'nombre 3', True, False, 'otros 4', False);

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('nombreNoPoblado 5', False, False, 63, '', False, False, False);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 11', 'descripcionCementerio 12', True, 'descripcionMito 8', False, False, False, 'descripcionCeramica 19', 'descripcionMonticulo 11', 63, 'descripcionCarbon 14', 'descripcionOseo 3', True, True, '', '', True, True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (63, 'notas 7');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (63, 'numeroPlano 8');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, False, True, 63, True, True, '', False);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, True, True, True, 63, False, True, '', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, '', 63, False, False);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, False, '', 63, True, False, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, False, True, True, True, 63, True, False, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (63, 4);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 63, False, True, False, True, True);

---------- Fin Insert Yacimiento 63

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (64, 64, 'Venezuela', 'Yacimiento 64', 'Municipio 1', 'Amazonas'); 

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, True, True, True, True, 'anchoDe 16', 'anchoDeComp 5', 'anchoA 10', 64, True, 'anchoAComp 3', False, False, '', True);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 64, 35, 14);

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 14', 64, 'diametro 15', 'ancho 11', '');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 15', 64, 'ancho 5');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('', False, 64, 'diametro 19', '');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 64, 'otros 10');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (64, 24, NULL, NULL, 'otros 2', 4);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 6', 'utmAdicional 13', 64, 'longitud 10');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (9, False, 28, True, NULL, 'perdidoPa 18', 'sumergidoPa 19', True, True, False, True, '', '', True, 23, False, 3, 22, False, 64, False, False, False, 7, True, False, '', False, False, '', True, False, True, False, False, 'destruidoPa 4', True, True, False, True, '', False, '', 'enterradoPa 4', True, True, 35, False, 'erosionPa 20', False, '');

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 64);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (False, '2013-05-22', 64, False, False, 'urlImagen 8');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 6', 'observaciones 16', False, 64, True, True, 'nombre 19', False, True, '', False);

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', True, True, 64, '', True, True, True);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (64, NULL);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (True, '', False, True, True, True, 64, False, False, 'otros 5', True);

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (64, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (64, 'tecnicas 16');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (False, '', False, 64, '', True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, True, True, True, True, 64, True, True, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (64, 2);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 64, False, True, True, True, False);

---------- Fin Insert Yacimiento 64

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (65, 65, 'Venezuela', 'Yacimiento 65', 'Municipio 12', 'Zulia'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', 'desnivel 17', 'texto 13', 65, 'superficie 5', 'altura 5');

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (True, 65, NULL, 33, True);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 65, NULL, 12);

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 13', 65, 'diametro 16', 'ancho 3', '');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 9', 'profundidad 10', 'diametro 7', 65, '', 'largo 9');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 1', 65, 'ancho 5');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (65, '');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (NULL, 65);

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('fauna 15', 65);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 9', 65);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (65, 'direcciones 9', '');

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('', '', True, '', True, True, False, 'descripcionCeramica 19', 'descripcionMonticulo 5', 65, 'descripcionCarbon 2', 'descripcionOseo 1', False, False, 'otros 10', '', True, False);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (65, 'notas 13');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, True, 'orientacion 7', 65, True, True, True, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (65, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, True, False, 65, False, False, '', False);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, False, False, 65, False, True, 'otros 13', True);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, True, '', 65, False, True, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, False, False, '', 65, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, '', 65, False, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (65, 18);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 65, True, True, True, False, False);

---------- Fin Insert Yacimiento 65

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (66, 66, 'Venezuela', 'Yacimiento 66', 'Municipio 13', 'Anzoategui'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 15', 'desnivel 17', 'texto 5', 66, 'superficie 17', 'altura 14');

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 8', 66, 'diametro 16', 'ancho 18');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 14', 66, 'diametro 14', 'ancho 8', 'profundidad 12');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 16', '', 'diametro 15', 66, '', 'largo 13');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 16', 66, 'ancho 6');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 66, 'otros 15');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (66, NULL, NULL, NULL, 'otros 9', 3);

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', 'autor 12', False, '', True, 'fecha 7', True, False, True, 66, '', True, '', 'direccion 4', '', False, 'telefono 6', '', 'bibliografia 19');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (66, 'urlImagen 6');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (NULL, 66);

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (3, False, NULL, False, NULL, '', 'sumergidoPa 16', True, True, True, True, '', '', False, NULL, True, 25, 19, True, 66, True, False, False, NULL, False, True, 'mas 5', True, False, '', True, False, False, False, True, '', True, True, True, False, 'patinaPa 8', True, '', '', False, True, NULL, True, 'erosionPa 19', True, 'crecimientoVegPa 11');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('fauna 3', 66);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 13', 66);

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', False, False, 66, 'nombrePoblado 17', False, False, True);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (66, NULL);

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, True, True, True, 66, False, True, '', False);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, '', True, 66, '', False);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, True, False, 66, True, False, '', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, 'otros 8', 66, True, True);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (True, '', 66, True, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, False, True, False, True, 66, False, False, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (66, NULL);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 66, False, False, False, True, True);

---------- Fin Insert Yacimiento 66

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (67, 67, 'Venezuela', 'Yacimiento 67', 'Municipio 13', 'Anzoategui'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', '', 'texto 6', 67, 'superficie 7', 'altura 9');

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 67, NULL, 27);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 12', 67, 'diametro 11', 'ancho 16');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 8', 67, 'diametro 5', 'ancho 20', '');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 16', 'profundidad 3', 'diametro 5', 67, '', 'largo 18');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 1', 67, 'ancho 4');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, False, False, True, False, True, False, True, True, 'produndidadDe 4', 'anchoA 13', 'profundidadA 6', 67, False, True, 'anchoDe 20', True, False, False);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('', True, 67, 'diametro 15', 'profundidad 19');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 67, 'otros 16');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (67, NULL, NULL, NULL, '', NULL);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 1', '', 67, 'longitud 18');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 12', '', False, '', True, 'fecha 9', False, True, True, 67, 'facebook 15', True, '', '', '', False, '', '', '');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (67, '');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (5, False, NULL, True, NULL, '', '', True, True, False, False, 'otros 8', '', False, NULL, True, NULL, 30, False, 67, False, False, True, 33, False, True, '', False, False, 'observaciones 14', True, False, True, True, False, 'destruidoPa 9', True, False, True, False, 'patinaPa 9', False, '', '', True, False, NULL, True, '', False, '');

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-06-15', 67, False, False, 'urlImagen 4');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 10', 'observaciones 20', True, 67, True, False, 'nombre 16', False, False, 'otros 16', True);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (67, NULL);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (True, 'tipo 6', False, False, True, True, 67, False, False, '', True);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, True, 'orientacion 18', 67, True, True, False, 'otros 5');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (67, '');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, '', True, 67, '', True);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, False, True, 67, True, True, '', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, 'otros 19', 67, True, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, True, True, '', 67, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, True, False, True, False, 67, True, True, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (67, NULL);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 67, True, True, True, False, True);

---------- Fin Insert Yacimiento 67

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (68, 68, 'Venezuela', 'Yacimiento 68', 'Municipio 3', 'Barinas'); 

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (True, 68, NULL, NULL, True);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, True, NULL, True, True, NULL, 68, 8, True, NULL);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 68, NULL, 36);

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 2', 'profundidad 11', 'diametro 16', 68, 'otros 1', 'largo 15');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 11', 68, 'ancho 17');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, False, False, False, False, True, True, True, True, 'produndidadDe 14', 'anchoA 13', 'profundidadA 17', 68, True, True, 'anchoDe 5', False, True, True);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('', True, 68, 'diametro 8', '');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 68, 'otros 4');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 9', '', 68, 'longitud 16');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 12', '', True, 'institucion 12', False, 'fecha 7', True, False, True, 68, 'facebook 20', False, '', 'direccion 7', '', False, 'telefono 17', '', '');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (68, 'urlImagen 13');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (4, 68);

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, True, NULL, False, NULL, 'perdidoPa 11', '', True, True, False, True, 'otros 15', '', True, NULL, True, NULL, 37, True, 68, False, True, False, NULL, True, False, '', True, False, '', True, True, True, False, True, 'destruidoPa 1', False, True, False, True, 'patinaPa 7', True, 'trasladadoPa 9', 'enterradoPa 5', False, True, NULL, True, 'erosionPa 8', False, '');

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 68);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-10-02', 68, True, True, '');

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (68, '', '');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('nombreNoPoblado 4', False, False, 68, '', True, True, False);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, 'tipo 2', False, True, True, True, 68, False, False, '', True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (68, '');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, False, 'orientacion 11', 68, False, True, False, 'otros 12');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (68, '');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, '', False, 68, 'otros 8', True);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (False, True, 'esTenenciaOtros 1', 68, False, False, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (True, False, False, 'mixto 14', 68, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, False, True, True, False, 68, False, True, False);

---------- Fin Insert Yacimiento 68

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (69, 69, 'Venezuela', 'Yacimiento 69', 'Municipio 11', 'Zulia'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', 'desnivel 15', 'texto 8', 69, 'superficie 11', 'altura 10');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, False, True, False, True, 'anchoDe 10', 'anchoDeComp 18', 'anchoA 17', 69, True, 'anchoAComp 12', False, True, '', True);

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (True, 69, NULL, NULL, True);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, False, NULL, False, False, NULL, 69, NULL, True, NULL);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 69, NULL, 40);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 9', 69, 'diametro 1', 'ancho 4');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 69, '');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 19', '', 69, 'longitud 5');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', 'autor 18', False, '', True, 'fecha 13', False, True, False, 69, '', False, '', '', '', False, '', 'twitter 19', 'bibliografia 18');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('', 69);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 5', '', True, 69, False, False, 'nombre 10', True, False, '', True);

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('nombreNoPoblado 13', True, True, 69, '', True, False, False);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, '', True, False, False, False, 69, True, False, '', True);

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (69, 'numeroPlano 1');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (69, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, True, True, 69, False, True, 'otros 15', False);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, True, '', 69, True, False, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, True, False, '', 69, False);

---------- Fin Insert Yacimiento 69

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (70, 70, 'Venezuela', 'Yacimiento 70', 'Municipio 8', 'Monagas'); 

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 70, 25, 35);

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 2', 70, 'diametro 7', 'ancho 12', '');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (True, False, True, False, True, False, True, False, True, 'produndidadDe 12', 'anchoA 11', 'profundidadA 2', 70, False, False, 'anchoDe 6', True, True, False);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 7', False, 70, 'diametro 9', '');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (70, NULL, NULL, NULL, '', NULL);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 11', 'utmAdicional 8', 70, 'longitud 13');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (70, 'urlImagen 7');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, False, 23, True, 33, '', '', True, True, True, False, '', 'especificar 14', False, 31, True, NULL, NULL, False, 70, False, True, False, NULL, True, True, '', False, True, '', True, False, False, True, False, '', True, True, True, False, 'patinaPa 3', True, 'trasladadoPa 20', '', False, False, NULL, True, 'erosionPa 9', False, '');

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (False, '2013-01-26', 70, False, False, 'urlImagen 5');

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (70, 'direcciones 20', 'puntoDatum 11');

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (70, 36);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('', 'descripcionCementerio 10', True, '', False, True, True, 'descripcionCeramica 18', 'descripcionMonticulo 12', 70, '', '', True, False, 'otros 20', '', False, True);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (True, 'tipo 18', False, True, False, False, 70, False, True, '', True);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, 'tecnicas 9', False, 70, 'otros 8', True);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, True, True, 70, True, False, 'otros 9', True);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 70, True, False, False, False, False);

---------- Fin Insert Yacimiento 70

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (71, 71, 'Venezuela', 'Yacimiento 71', 'Municipio 18', 'Falcón'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', 'desnivel 8', 'texto 2', 71, 'superficie 19', 'altura 13');

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (35, True, NULL, False, False, 12, 71, 10, True, NULL);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 71, NULL, 28);

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 8', 71, 'diametro 9', 'ancho 4', 'profundidad 9');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 18', 71, 'ancho 19');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 5', 'utmAdicional 20', 71, 'longitud 3');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 15', 'autor 20', True, 'institucion 11', False, 'fecha 2', True, False, False, 71, 'facebook 19', False, '', 'direccion 19', '', False, 'telefono 5', 'twitter 4', 'bibliografia 11');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (71, 'urlImagen 8');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (19, 71);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (False, '2013-07-21', 71, False, False, '');

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (71, '', 'puntoDatum 14');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, False, 'orientacion 6', 71, True, False, False, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (71, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (71, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, True, False, 71, True, True, 'otros 17', True);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, 'tecnicas 15', True, 71, 'otros 9', True);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, True, False, False, 71, True, True, 'otros 12', True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, True, False, 'mixto 2', 71, True);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 71, True, False, True, False, False);

---------- Fin Insert Yacimiento 71

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (72, 72, 'Venezuela', 'Yacimiento 72', 'Municipio 9', 'Carabobo'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', '', 'texto 10', 72, 'superficie 14', 'altura 10');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 6', 72, 'diametro 18', 'ancho 16', '');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 4', '', 'diametro 10', 72, '', 'largo 12');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (True, False, False, False, False, False, True, False, True, '', 'anchoA 20', 'profundidadA 12', 72, False, True, 'anchoDe 1', False, True, False);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 5', False, 72, 'diametro 8', '');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 72, '');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 12', '', 72, 'longitud 11');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('fauna 12', 72);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 72);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-02-10', 72, True, False, '');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('nombreNoPoblado 6', False, False, 72, 'nombrePoblado 1', False, True, True);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (72, 12);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (72, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (72, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (72, 'tecnicas 12');

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, 'otros 4', 72, False, False);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, True, 'esTenenciaOtros 13', 72, False, False, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (72, NULL);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 72, True, False, True, True, False);

---------- Fin Insert Yacimiento 72

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (73, 73, 'Venezuela', 'Yacimiento 73', 'Municipio 14', 'Trujillo'); 

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, False, NULL, False, False, 21, 73, 35, False, 39);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 73, NULL, 12);

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 4', 73, 'ancho 11');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, False, False, True, False, True, True, True, True, 'produndidadDe 13', 'anchoA 20', 'profundidadA 2', 73, False, True, 'anchoDe 5', False, True, True);

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 73, '');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (3, 73);

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (29, True, 9, True, NULL, '', 'sumergidoPa 15', False, False, True, False, '', '', False, 24, True, NULL, 15, False, 73, True, True, True, NULL, True, True, '', False, False, '', True, False, False, True, False, 'destruidoPa 14', False, False, False, True, 'patinaPa 3', False, '', 'enterradoPa 3', False, False, NULL, False, 'erosionPa 11', True, '');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('', 73);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 73);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 17', '', False, 73, False, True, 'nombre 17', True, True, '', False);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 13', '', True, '', True, True, False, '', '', 73, '', 'descripcionOseo 2', False, False, 'otros 8', '', False, True);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (True, '', True, True, False, False, 73, True, True, '', True);

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (73, 'numeroPlano 12');

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, False, False, 73, True, True, 'otros 14', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, '', 73, True, False);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, True, 'esTenenciaOtros 13', 73, False, False, False);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (True, True, False, '', 73, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, True, True, False, True, 73, True, False, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (73, NULL);

---------- Fin Insert Yacimiento 73

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (74, 74, 'Venezuela', 'Yacimiento 74', 'Municipio 13', 'Miranda'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', '', 'texto 8', 74, 'superficie 16', 'altura 16');

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, True, 18, False, True, 23, 74, NULL, False, NULL);

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 12', 74, 'diametro 20', 'ancho 3', 'profundidad 4');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 12', 74, 'ancho 9');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, True, True, False, True, True, False, True, False, '', 'anchoA 3', 'profundidadA 6', 74, False, False, 'anchoDe 18', False, True, False);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 8', False, 74, 'diametro 13', '');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', 'autor 12', True, '', False, 'fecha 19', False, False, True, 74, '', False, '', 'direccion 5', 'pais 2', False, '', 'twitter 13', 'bibliografia 11');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, False, NULL, True, 34, '', '', True, True, False, False, '', '', True, NULL, False, NULL, NULL, True, 74, False, True, False, NULL, True, False, '', False, False, '', True, True, False, True, True, 'destruidoPa 15', True, False, True, False, 'patinaPa 14', True, '', 'enterradoPa 4', True, False, NULL, False, '', False, 'crecimientoVegPa 16');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('', 74);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-04-21', 74, True, False, '');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 17', '', True, 74, False, False, 'nombre 5', True, False, '', False);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (74, '', 'puntoDatum 15');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('nombreNoPoblado 3', True, True, 74, 'nombrePoblado 14', False, False, True);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (True, '', False, False, False, False, 74, True, False, '', True);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, False, 'orientacion 1', 74, False, False, False, 'otros 3');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (74, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (74, '');

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, False, False, 74, False, True, 'otros 3', True);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, True, 'esTenenciaOtros 4', 74, True, False, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, False, False, True, False, 74, False, True, False);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 74, False, True, True, False, False);

---------- Fin Insert Yacimiento 74

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (75, 75, 'Venezuela', 'Yacimiento 75', 'Municipio 7', 'Yaracuy'); 

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 75, NULL, 27);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 1', 75, 'diametro 19', 'ancho 14');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 3', '', 'diametro 3', 75, '', 'largo 5');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 8', 75, 'ancho 15');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, False, False, True, False, False, True, True, True, 'produndidadDe 8', 'anchoA 20', 'profundidadA 7', 75, True, False, 'anchoDe 12', False, True, True);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('', True, 75, 'diametro 18', '');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 75, 'otros 20');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (75, NULL, 24, NULL, '', NULL);

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', '', True, 'institucion 9', True, 'fecha 12', False, True, True, 75, 'facebook 16', False, '', 'direccion 5', '', True, '', 'twitter 12', '');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, False, NULL, True, NULL, '', 'sumergidoPa 4', True, False, True, False, 'otros 7', 'especificar 5', True, 30, True, 16, 24, False, 75, False, False, False, 35, False, True, 'mas 11', False, False, '', False, False, True, True, True, '', False, True, True, True, 'patinaPa 17', True, 'trasladadoPa 9', '', True, False, 12, False, '', True, '');

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 18', 75);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (False, '2013-04-12', 75, True, False, '');

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (75, 'direcciones 18', '');

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 10', '', True, 'descripcionMito 19', True, False, False, 'descripcionCeramica 7', 'descripcionMonticulo 20', 75, 'descripcionCarbon 12', '', False, False, '', 'descripcionLitica 6', False, True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (75, 'notas 16');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, False, 'orientacion 9', 75, True, False, False, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (75, 'numeroPlano 12');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, False, False, 75, True, True, 'otros 1', False);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, True, True, 75, True, False, '', False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, 'observaciones 14', 75, False, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (75, NULL);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 75, False, True, True, False, True);

---------- Fin Insert Yacimiento 75

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (76, 76, 'Venezuela', 'Yacimiento 76', 'Municipio 13', 'Amazonas'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 13', 'desnivel 3', 'texto 20', 76, 'superficie 6', 'altura 2');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (True, False, False, True, False, 'anchoDe 16', 'anchoDeComp 15', 'anchoA 10', 76, True, 'anchoAComp 12', False, True, 'otros 15', True);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, True, 21, False, False, 4, 76, 31, False, 13);

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 7', 76, 'diametro 19', 'ancho 20', 'profundidad 3');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 19', 'profundidad 18', 'diametro 7', 76, 'otros 10', 'largo 10');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 8', 76, 'ancho 17');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 4', True, 76, 'diametro 1', '');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 76, 'otros 17');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (76, NULL, NULL, NULL, '', 32);

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', 'autor 13', True, 'institucion 2', False, 'fecha 2', True, True, False, 76, 'facebook 16', True, '', 'direccion 17', '', True, 'telefono 11', '', 'bibliografia 19');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (NULL, 76);

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', False, False, 76, '', False, True, False);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (76, 29);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (False, 'tecnicas 14', True, 76, 'otros 18', False);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, True, False, True, 76, False, True, '', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, '', 76, True, True);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, True, '', 76, False, False, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, False, True, False, False, 76, False, False, False);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 76, True, False, True, False, True);

---------- Fin Insert Yacimiento 76

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (77, 77, 'Venezuela', 'Yacimiento 77', 'Municipio 18', 'Amazonas'); 

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (True, False, True, True, False, 'anchoDe 11', 'anchoDeComp 7', 'anchoA 18', 77, False, 'anchoAComp 16', True, True, 'otros 16', True);

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 77, NULL, 9, True);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (12, False, 26, False, True, 36, 77, NULL, False, 6);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 77, NULL, 2);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 3', 77, 'diametro 3', 'ancho 3');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 17', True, 77, 'diametro 13', 'profundidad 12');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 17', 'utmAdicional 7', 77, 'longitud 16');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 9', '', False, 'institucion 10', True, 'fecha 10', True, True, False, 77, '', True, '', 'direccion 1', 'pais 10', True, '', 'twitter 19', 'bibliografia 1');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (23, 77);

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('fauna 17', 77);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-04-02', 77, True, False, '');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 20', '', False, 77, False, False, 'nombre 9', False, False, 'otros 20', True);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (77, '', '');

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 9', '', True, 'descripcionMito 9', True, True, True, 'descripcionCeramica 8', '', 77, 'descripcionCarbon 8', 'descripcionOseo 5', True, True, 'otros 5', '', False, False);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (77, 'notas 3');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, True, 'orientacion 6', 77, False, False, True, 'otros 20');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (77, 'tecnicas 16');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, True, True, 77, False, True, '', False);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, False, True, 77, True, True, '', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, 'otros 8', 77, False, True);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (True, 'observaciones 10', 77, True, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, True, True, True, True, 77, True, True, True);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 77, False, True, True, False, True);

---------- Fin Insert Yacimiento 77

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (78, 78, 'Venezuela', 'Yacimiento 78', 'Municipio 2', 'Barinas'); 

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (31, False, 4, False, False, NULL, 78, 16, True, NULL);

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 14', 78, 'diametro 7', 'ancho 4', '');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 20', 78, 'ancho 15');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 16', False, 78, 'diametro 16', 'profundidad 9');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 78, 'otros 14');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 9', 'utmAdicional 10', 78, 'longitud 4');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 4', '', True, 'institucion 18', False, 'fecha 14', True, True, True, 78, 'facebook 7', False, '', '', '', True, '', 'twitter 12', 'bibliografia 13');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (22, True, NULL, True, 35, '', '', True, False, True, True, '', '', False, NULL, True, NULL, NULL, True, 78, True, True, True, 40, False, False, 'mas 11', True, False, 'observaciones 3', True, False, False, False, True, '', False, False, False, False, '', False, 'trasladadoPa 17', '', False, True, 34, True, 'erosionPa 15', True, '');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('fauna 7', 78);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 78);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-06-04', 78, False, True, '');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 3', '', False, 78, False, True, 'nombre 1', True, True, 'otros 14', False);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (78, 'direcciones 14', '');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', True, True, 78, '', False, False, True);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (78, NULL);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('', '', True, '', True, False, False, '', 'descripcionMonticulo 8', 78, '', '', False, True, 'otros 14', '', True, False);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (True, 'tipo 19', True, False, True, False, 78, False, False, '', True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (78, 'notas 17');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, False, 'orientacion 16', 78, True, True, False, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, False, True, 78, True, False, 'otros 17', True);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, 'tecnicas 1', False, 78, '', False);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, True, False, 78, False, True, '', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, '', 78, True, True);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, False, '', 78, False, False, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (True, False, False, 'mixto 4', 78, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, False, False, True, True, 78, False, True, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (78, 16);

---------- Fin Insert Yacimiento 78

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (79, 79, 'Venezuela', 'Yacimiento 79', 'Municipio 5', 'Yaracuy'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 13', '', 'texto 2', 79, 'superficie 20', 'altura 12');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, True, True, False, True, 'anchoDe 7', 'anchoDeComp 17', 'anchoA 9', 79, False, 'anchoAComp 7', True, False, '', True);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (39, True, 30, False, False, 30, 79, 38, False, NULL);

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 17', '', 'diametro 5', 79, '', 'largo 6');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 2', False, 79, 'diametro 8', 'profundidad 14');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 79, 'otros 16');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 4', '', 79, 'longitud 12');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (79, 'urlImagen 19');

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 2', '', False, '', False, True, False, 'descripcionCeramica 15', '', 79, '', 'descripcionOseo 9', False, True, 'otros 8', '', True, True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (79, 'notas 12');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, False, 'orientacion 5', 79, True, True, False, '');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, '', True, 79, '', False);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, False, False, 79, False, True, 'otros 9', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, '', 79, True, True);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, False, '', 79, True, True, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, True, True, 'mixto 1', 79, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, True, True, True, False, 79, True, False, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (79, 3);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 79, False, False, True, True, False);

---------- Fin Insert Yacimiento 79

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (80, 80, 'Venezuela', 'Yacimiento 80', 'Municipio 8', 'Yaracuy'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 10', '', 'texto 15', 80, 'superficie 17', 'altura 10');

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (True, 80, 30, 23, True);

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 18', '', 'diametro 6', 80, 'otros 14', 'largo 18');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 4', 80, 'ancho 3');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (True, False, True, False, False, False, True, False, True, 'produndidadDe 20', 'anchoA 16', 'profundidadA 13', 80, False, True, 'anchoDe 3', True, False, True);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 3', False, 80, 'diametro 7', 'profundidad 16');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 80, '');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (80, 32, NULL, 4, '', 35);

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (NULL, 80);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 80);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-08-30', 80, False, True, 'urlImagen 18');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 13', 'observaciones 8', True, 80, True, False, 'nombre 10', True, False, 'otros 4', True);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (80, '', '');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', False, True, 80, '', False, False, True);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 5', 'descripcionCementerio 11', False, 'descripcionMito 12', True, True, False, '', '', 80, '', 'descripcionOseo 12', False, True, 'otros 6', '', False, True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (80, 'notas 4');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (80, 'numeroPlano 1');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, 'tecnicas 8', True, 80, 'otros 7', True);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, False, False, 80, True, True, 'otros 7', True);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, '', 80, True, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, False, True, False, True, 80, True, False, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (80, 24);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 80, True, True, False, False, False);

---------- Fin Insert Yacimiento 80

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (81, 81, 'Venezuela', 'Yacimiento 81', 'Municipio 9', 'Nueva Esparta'); 

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, True, NULL, False, True, NULL, 81, NULL, False, 4);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 16', 81, 'diametro 10', 'ancho 19');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 4', 81, 'diametro 9', 'ancho 20', 'profundidad 11');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 4', 81, 'ancho 12');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, False, True, False, True, False, False, True, False, 'produndidadDe 3', 'anchoA 1', 'profundidadA 6', 81, True, True, 'anchoDe 10', False, False, True);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 16', False, 81, 'diametro 8', 'profundidad 4');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 81, 'otros 4');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 12', '', True, 'institucion 12', False, 'fecha 8', True, False, False, 81, '', False, '', '', 'pais 13', True, '', '', 'bibliografia 2');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, True, NULL, True, NULL, 'perdidoPa 16', '', True, False, True, False, '', 'especificar 19', False, 31, False, NULL, 24, False, 81, False, True, False, NULL, True, False, '', False, True, '', False, True, True, True, False, '', True, True, True, False, '', False, 'trasladadoPa 17', '', False, True, NULL, False, 'erosionPa 2', True, 'crecimientoVegPa 6');

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 17', 81);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-09-04', 81, False, False, '');

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (81, 'direcciones 1', 'puntoDatum 9');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', False, False, 81, 'nombrePoblado 2', True, False, True);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('', 'descripcionCementerio 16', True, 'descripcionMito 6', True, True, False, '', '', 81, '', '', False, False, 'otros 7', '', False, True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (81, 'notas 13');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, True, 'orientacion 5', 81, True, True, False, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (81, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (81, 'tecnicas 4');

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, True, False, 81, True, True, 'otros 12', True);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, True, '', 81, False, False, False);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, True, True, 'mixto 14', 81, True);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, '', 81, True, True);

---------- Fin Insert Yacimiento 81

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (82, 82, 'Venezuela', 'Yacimiento 82', 'Municipio 11', 'Amazonas'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', '', 'texto 15', 82, 'superficie 8', 'altura 18');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, True, False, True, True, 'anchoDe 1', 'anchoDeComp 8', 'anchoA 7', 82, True, 'anchoAComp 2', True, True, 'otros 5', False);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, False, 16, True, False, 18, 82, 18, False, NULL);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 14', 82, 'diametro 9', 'ancho 17');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 20', '', 'diametro 3', 82, 'otros 6', 'largo 8');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 6', 82, 'ancho 9');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (NULL, 82);

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('fauna 16', 82);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 16', 82);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (82, 'direcciones 20', 'puntoDatum 5');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('nombreNoPoblado 7', False, False, 82, '', False, True, True);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (82, 27);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 2', 'descripcionCementerio 17', False, '', False, True, True, '', 'descripcionMonticulo 5', 82, 'descripcionCarbon 12', '', True, True, 'otros 6', '', False, False);

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (82, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (82, 'tecnicas 9');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, True, False, True, 82, True, False, 'otros 17', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, 'otros 6', 82, True, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, True, False, True, False, 82, True, True, True);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 82, True, False, True, False, True);

---------- Fin Insert Yacimiento 82

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (83, 83, 'Venezuela', 'Yacimiento 83', 'Municipio 16', 'Bolívar'); 

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 83, NULL, NULL, False);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (33, True, NULL, True, True, 38, 83, NULL, True, 20);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 4', 83, 'diametro 4', 'ancho 2');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 9', 83, 'diametro 20', 'ancho 13', 'profundidad 8');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (True, False, True, True, True, True, True, True, True, 'produndidadDe 11', 'anchoA 15', 'profundidadA 15', 83, False, True, 'anchoDe 5', True, True, True);

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (83, NULL, NULL, 9, '', NULL);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 9', '', 83, 'longitud 15');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (83, '');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (17, True, NULL, True, NULL, 'perdidoPa 11', 'sumergidoPa 20', True, True, True, False, '', 'especificar 3', False, 35, True, NULL, 37, False, 83, False, False, True, NULL, False, False, 'mas 8', True, True, '', True, False, False, False, True, 'destruidoPa 16', True, True, True, False, '', True, '', 'enterradoPa 9', False, True, 27, True, 'erosionPa 9', True, 'crecimientoVegPa 11');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('', 83);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (83, 'direcciones 18', 'puntoDatum 15');

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (83, 7);

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (83, 'numeroPlano 11');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (83, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, False, True, 83, True, False, '', True);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (False, '', False, 83, 'otros 16', False);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, False, False, 83, True, True, '', False);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (True, True, False, 'mixto 10', 83, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (83, 6);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 83, False, False, True, True, True);

---------- Fin Insert Yacimiento 83

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (84, 84, 'Venezuela', 'Yacimiento 84', 'Municipio 19', 'Sucre'); 

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (True, 84, NULL, 27, False);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, False, NULL, True, False, 13, 84, 3, False, 2);

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 20', '', 'diametro 15', 84, 'otros 14', 'largo 8');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 9', 84, 'ancho 11');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('', True, 84, 'diametro 17', '');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 84, '');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (84, 21, NULL, 26, '', NULL);

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', 'autor 1', False, '', True, 'fecha 5', False, True, False, 84, '', False, '', 'direccion 20', 'pais 11', False, '', '', 'bibliografia 16');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (84, 'urlImagen 5');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (NULL, 84);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 84);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (84, '', 'puntoDatum 2');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('nombreNoPoblado 3', False, False, 84, '', False, False, True);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, True, 'orientacion 3', 84, False, False, True, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (84, 'tecnicas 8');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, 'tecnicas 13', False, 84, 'otros 5', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, '', 84, True, True);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (False, True, 'esTenenciaOtros 10', 84, True, False, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (True, True, False, '', 84, True);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, '', 84, False, False);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 84, False, True, False, False, False);

---------- Fin Insert Yacimiento 84

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (85, 85, 'Venezuela', 'Yacimiento 85', 'Municipio 1', 'Yaracuy'); 

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (26, False, NULL, False, True, NULL, 85, 2, True, NULL);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 85, 12, 9);

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 14', 'profundidad 11', 'diametro 2', 85, '', 'largo 4');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, True, True, True, False, True, False, False, False, '', 'anchoA 17', 'profundidadA 1', 85, True, False, 'anchoDe 20', False, True, True);

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 85, '');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (85, 30, 24, 37, '', 25);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 19', 'utmAdicional 15', 85, 'longitud 16');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (8, 85);

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, True, NULL, True, 5, 'perdidoPa 3', '', False, True, True, True, 'otros 19', 'especificar 8', True, 19, False, 6, 22, True, 85, False, False, True, NULL, True, True, '', False, False, '', True, False, True, True, False, 'destruidoPa 6', True, True, True, False, 'patinaPa 2', False, 'trasladadoPa 16', 'enterradoPa 12', False, False, 31, False, '', False, '');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('fauna 9', 85);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-03-08', 85, False, True, '');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 11', '', True, 85, True, True, 'nombre 16', True, False, 'otros 7', False);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 4', 'descripcionCementerio 17', False, 'descripcionMito 11', True, True, False, '', 'descripcionMonticulo 14', 85, 'descripcionCarbon 4', 'descripcionOseo 20', False, False, '', '', True, False);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (True, 'tipo 15', False, False, True, False, 85, False, False, '', True);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, True, 'orientacion 5', 85, False, True, True, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (85, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, True, False, True, 85, False, False, 'otros 20', True);

---------- Fin Insert Yacimiento 85

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (86, 86, 'Venezuela', 'Yacimiento 86', 'Municipio 13', 'Tachira'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 7', '', 'texto 5', 86, 'superficie 12', 'altura 14');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, True, True, True, False, 'anchoDe 4', 'anchoDeComp 7', 'anchoA 12', 86, True, 'anchoAComp 1', True, False, '', False);

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (True, 86, NULL, NULL, True);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 86, 1, 29);

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (True, False, True, False, True, False, False, True, True, '', 'anchoA 3', 'profundidadA 6', 86, True, False, 'anchoDe 4', True, True, True);

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 86, '');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 15', 'utmAdicional 3', 86, 'longitud 6');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (86, 'urlImagen 14');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (NULL, 86);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 86);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-05-20', 86, False, True, '');

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (86, 'direcciones 15', 'puntoDatum 13');

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (86, NULL);

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (86, 'numeroPlano 18');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, True, False, 86, False, True, '', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, 'otros 4', 86, True, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, False, True, 'mixto 16', 86, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (True, 'observaciones 6', 86, True, True);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 86, True, True, False, False, False);

---------- Fin Insert Yacimiento 86

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (87, 87, 'Venezuela', 'Yacimiento 87', 'Municipio 4', 'Trujillo'); 

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (True, False, True, False, True, 'anchoDe 11', 'anchoDeComp 7', 'anchoA 19', 87, True, 'anchoAComp 14', True, True, 'otros 8', True);

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 87, 1, NULL, True);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, False, 22, True, True, NULL, 87, 5, True, 18);

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 10', 87, 'diametro 13', 'ancho 10', 'profundidad 13');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 12', 87, 'ancho 18');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 4', True, 87, 'diametro 7', 'profundidad 19');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (87, NULL, 22, 35, '', 28);

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', '', True, 'institucion 10', True, 'fecha 11', True, True, True, 87, 'facebook 16', True, 'mail 13', 'direccion 18', 'pais 19', True, '', 'twitter 16', 'bibliografia 18');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (87, '');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (NULL, 87);

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('fauna 5', 87);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (87, 'direcciones 15', 'puntoDatum 5');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('nombreNoPoblado 1', True, False, 87, 'nombrePoblado 20', True, True, True);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (87, 12);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, '', False, False, False, False, 87, False, True, 'otros 9', True);

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (87, 'numeroPlano 7');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (87, 'tecnicas 20');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, False, False, 87, True, True, '', True);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, 'tecnicas 8', True, 87, 'otros 16', False);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, False, False, 87, False, True, '', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, 'otros 3', 87, False, False);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, True, False, '', 87, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, True, False, True, False, 87, True, True, True);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 87, True, False, True, True, False);

---------- Fin Insert Yacimiento 87

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (88, 88, 'Venezuela', 'Yacimiento 88', 'Municipio 18', 'Apure'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 9', 'desnivel 7', 'texto 3', 88, 'superficie 9', 'altura 11');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, True, False, True, False, 'anchoDe 1', 'anchoDeComp 1', 'anchoA 10', 88, True, 'anchoAComp 17', True, False, 'otros 8', True);

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (True, 88, NULL, 11, False);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 17', 88, 'diametro 11', 'ancho 12');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 6', 88, 'diametro 11', 'ancho 5', '');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 13', '', 'diametro 1', 88, 'otros 18', 'largo 16');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 17', 88, 'ancho 16');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, True, True, True, True, False, False, True, False, 'produndidadDe 10', 'anchoA 10', 'profundidadA 7', 88, True, False, 'anchoDe 1', False, False, False);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('', False, 88, 'diametro 8', 'profundidad 1');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 88, '');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 8', '', 88, 'longitud 8');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('fauna 19', 88);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 88);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (88, 18);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (True, '', True, True, True, True, 88, True, True, '', False);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (88, '');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, False, 'orientacion 3', 88, False, True, False, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (88, '');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (88, 'tecnicas 20');

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, 'otros 3', 88, True, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, True, True, '', 88, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (True, 'observaciones 16', 88, True, False);

---------- Fin Insert Yacimiento 88

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (89, 89, 'Venezuela', 'Yacimiento 89', 'Municipio 11', 'Falcón'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', 'desnivel 6', 'texto 3', 89, 'superficie 7', 'altura 14');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (True, True, True, False, True, 'anchoDe 5', 'anchoDeComp 10', 'anchoA 8', 89, False, 'anchoAComp 17', True, False, 'otros 9', True);

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 89, 15, 14, False);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, True, 20, True, True, 13, 89, NULL, True, NULL);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 89, 18, 8);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 3', 89, 'diametro 16', 'ancho 4');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, True, True, False, True, False, False, False, True, '', 'anchoA 2', 'profundidadA 3', 89, False, False, 'anchoDe 10', False, False, False);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 10', '', 89, 'longitud 3');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 9', '', True, 'institucion 8', False, 'fecha 16', False, True, False, 89, '', False, 'mail 18', 'direccion 19', '', True, 'telefono 10', '', '');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (21, 89);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 18', 89);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (False, '2013-03-23', 89, True, False, 'urlImagen 9');

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (89, 'direcciones 18', '');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('nombreNoPoblado 4', False, True, 89, 'nombrePoblado 10', False, False, True);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (True, '', False, False, True, False, 89, True, True, 'otros 12', False);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, False, 'orientacion 3', 89, True, False, False, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, True, True, 89, True, True, 'otros 7', True);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (False, '', False, 89, '', True);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, True, True, False, 89, False, True, '', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, 'otros 19', 89, False, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (False, False, False, 'mixto 12', 89, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, '', 89, False, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (89, 9);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 89, True, True, True, False, True);

---------- Fin Insert Yacimiento 89

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (90, 90, 'Venezuela', 'Yacimiento 90', 'Municipio 8', 'Sucre'); 

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, False, True, False, True, 'anchoDe 18', 'anchoDeComp 4', 'anchoA 9', 90, False, 'anchoAComp 12', False, False, 'otros 18', True);

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (True, 90, NULL, 34, True);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (34, True, 29, True, True, 9, 90, NULL, False, NULL);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 90, NULL, 26);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 17', 90, 'diametro 18', 'ancho 16');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (True, False, False, True, True, False, True, True, True, 'produndidadDe 7', 'anchoA 5', 'profundidadA 17', 90, False, True, 'anchoDe 5', True, False, False);

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 90, 'otros 19');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (NULL, 90);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 90);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 9', '', True, 90, False, False, 'nombre 17', False, True, '', True);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (90, '', '');

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (90, NULL);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, '', True, False, True, True, 90, True, True, 'otros 1', True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (90, 'notas 2');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, True, 'orientacion 16', 90, True, True, True, 'otros 13');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (90, 'tecnicas 16');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, True, True, False, 90, False, True, 'otros 1', False);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, 'tecnicas 17', True, 90, '', False);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (True, True, True, 'mixto 17', 90, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (90, NULL);

---------- Fin Insert Yacimiento 90

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (91, 91, 'Venezuela', 'Yacimiento 91', 'Municipio 8', 'Aragua'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 16', 'desnivel 3', 'texto 16', 91, 'superficie 9', 'altura 19');

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, True, NULL, False, True, 6, 91, NULL, True, NULL);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 91, 35, 14);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 8', 91, 'diametro 11', 'ancho 1');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 20', 91, 'diametro 9', 'ancho 9', '');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 9', 'profundidad 13', 'diametro 2', 91, 'otros 7', 'largo 17');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 4', 91, 'ancho 8');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (False, 91, '');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 20', '', True, '', False, 'fecha 17', True, True, False, 91, '', False, '', 'direccion 13', '', False, '', '', '');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (91, 'urlImagen 9');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (5, 91);

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (38, False, 17, False, NULL, 'perdidoPa 3', '', True, False, True, True, '', 'especificar 18', True, NULL, False, NULL, NULL, False, 91, True, True, True, 30, False, True, 'mas 9', True, True, 'observaciones 5', False, True, True, False, False, '', True, True, False, False, 'patinaPa 12', False, '', '', False, True, NULL, True, 'erosionPa 16', True, 'crecimientoVegPa 11');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('fauna 10', 91);

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-03-18', 91, True, True, '');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 17', 'observaciones 4', False, 91, False, True, 'nombre 19', True, True, '', True);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (91, 'direcciones 13', 'puntoDatum 1');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', False, False, 91, 'nombrePoblado 13', True, False, False);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 11', '', True, 'descripcionMito 10', True, False, True, '', 'descripcionMonticulo 20', 91, 'descripcionCarbon 7', 'descripcionOseo 1', False, False, '', 'descripcionLitica 6', True, False);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, 'tipo 3', True, True, True, True, 91, True, False, '', True);

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (91, '');

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, True, True, True, True, 91, True, False, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (91, NULL);

---------- Fin Insert Yacimiento 91

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (92, 92, 'Venezuela', 'Yacimiento 92', 'Municipio 9', 'Amazonas'); 

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (True, 92, NULL, 3);

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 1', '', 'diametro 15', 92, 'otros 19', 'largo 19');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 12', 92, 'ancho 8');

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 8', False, 92, 'diametro 13', 'profundidad 8');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 92, 'otros 10');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 8', '', 92, 'longitud 8');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('fauna 13', 92);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 92);

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (92, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, False, True, 92, False, True, 'otros 5', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (False, '', 92, False, False);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, False, 'esTenenciaOtros 16', 92, True, True, False);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (True, False, False, 'mixto 4', 92, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, False, False, True, True, 92, True, True, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (92, 27);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 92, False, True, False, False, False);

---------- Fin Insert Yacimiento 92

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (93, 93, 'Venezuela', 'Yacimiento 93', 'Municipio 3', 'Trujillo'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('desarrollo 18', 'desnivel 14', 'texto 4', 93, 'superficie 20', 'altura 17');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, False, False, False, True, 'anchoDe 15', 'anchoDeComp 6', 'anchoA 7', 93, False, 'anchoAComp 4', False, True, '', True);

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 3', '', 'diametro 2', 93, '', 'largo 15');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 14', 93, 'ancho 19');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, False, False, False, True, False, False, False, True, 'produndidadDe 16', 'anchoA 6', 'profundidadA 16', 93, False, True, 'anchoDe 4', True, False, False);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 11', True, 93, 'diametro 14', '');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (93, 7, 21, 10, '', NULL);

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 2', 'autor 8', True, '', True, 'fecha 5', True, False, False, 93, 'facebook 14', False, 'mail 3', '', 'pais 16', False, 'telefono 12', '', 'bibliografia 7');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (93, 'urlImagen 17');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (28, 93);

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('fauna 12', 93);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 8', 93);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (93, 'direcciones 19', 'puntoDatum 2');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('nombreNoPoblado 2', False, False, 93, 'nombrePoblado 9', True, True, True);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 1', '', False, '', True, True, False, '', '', 93, 'descripcionCarbon 14', 'descripcionOseo 17', True, False, '', 'descripcionLitica 15', False, True);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, True, 'orientacion 13', 93, True, False, True, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (93, 'numeroPlano 17');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (93, '');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, False, True, 93, True, False, 'otros 14', True);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, True, True, 93, False, False, 'otros 19', False);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (True, True, True, 'mixto 17', 93, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, '', 93, True, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (93, NULL);

---------- Fin Insert Yacimiento 93

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (94, 94, 'Venezuela', 'Yacimiento 94', 'Municipio 4', 'Trujillo'); 

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 94, 26, NULL, True);

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 18', 94, 'diametro 4', 'ancho 15', 'profundidad 16');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 10', '', 94, 'longitud 19');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 11', 'autor 19', False, 'institucion 20', True, 'fecha 12', False, True, False, 94, 'facebook 8', True, '', '', 'pais 10', False, 'telefono 13', '', '');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, True, 37, False, NULL, 'perdidoPa 8', 'sumergidoPa 3', False, True, False, False, '', '', True, 12, True, 21, 17, True, 94, True, True, True, 25, True, False, '', True, False, '', False, False, True, True, False, '', False, True, False, False, 'patinaPa 8', False, 'trasladadoPa 10', '', False, False, 1, False, '', False, 'crecimientoVegPa 12');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('', 94);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 94);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 1', '', True, 94, True, True, 'nombre 19', False, True, 'otros 6', False);

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', True, False, 94, 'nombrePoblado 11', True, True, False);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (94, NULL);

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, False, True, 94, True, False, 'otros 12', True);

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (True, '', True, 94, 'otros 14', True);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, False, 'esTenenciaOtros 13', 94, False, True, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (True, '', 94, False, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (94, 15);

---------- Fin Insert Yacimiento 94

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (95, 95, 'Venezuela', 'Yacimiento 95', 'Municipio 6', 'Miranda'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', '', 'texto 9', 95, 'superficie 1', 'altura 10');

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (True, 95, 23, NULL, True);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (20, True, NULL, False, False, NULL, 95, 38, False, 18);

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 20', '', 'diametro 18', 95, '', 'largo 20');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (True, True, True, True, False, True, True, False, False, 'produndidadDe 18', 'anchoA 9', 'profundidadA 4', 95, True, True, 'anchoDe 17', False, True, True);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 14', False, 95, 'diametro 11', 'profundidad 5');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', '', False, 'institucion 12', False, 'fecha 20', True, True, True, 95, '', False, '', 'direccion 5', '', False, '', 'twitter 15', 'bibliografia 7');

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (20, True, 1, True, NULL, 'perdidoPa 16', 'sumergidoPa 6', True, False, True, True, 'otros 11', 'especificar 8', False, 40, False, 17, 8, False, 95, False, True, True, 5, True, False, '', True, False, 'observaciones 2', True, False, True, True, True, 'destruidoPa 2', True, False, False, False, 'patinaPa 7', True, '', 'enterradoPa 14', False, False, 3, False, '', True, '');

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 95);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 2', '', True, 95, True, True, 'nombre 12', False, True, '', True);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (95, '', 'puntoDatum 11');

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (95, 'notas 4');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, False, 'orientacion 16', 95, True, False, True, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (95, 'numeroPlano 15');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (95, 'tecnicas 17');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, False, False, True, 95, True, False, '', False);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, True, True, False, 95, True, True, 'otros 8', True);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (True, True, 'esTenenciaOtros 14', 95, False, False, True);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (True, '', 95, False, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (95, NULL);

---------- Fin Insert Yacimiento 95

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (96, 96, 'Venezuela', 'Yacimiento 96', 'Municipio 20', 'Vargas'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', '', 'texto 6', 96, 'superficie 2', 'altura 1');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (True, True, False, False, False, 'anchoDe 18', 'anchoDeComp 7', 'anchoA 20', 96, True, 'anchoAComp 13', False, False, '', False);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 18', 96, 'diametro 13', 'ancho 20');

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 13', '', 'diametro 10', 96, '', 'largo 9');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 14', 96, 'ancho 3');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (False, False, True, False, True, True, True, False, False, '', 'anchoA 5', 'profundidadA 5', 96, False, False, 'anchoDe 19', False, True, False);

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 96, 'otros 1');

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 12', 'utmAdicional 8', 96, 'longitud 18');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', 'autor 2', False, 'institucion 12', True, 'fecha 4', True, False, True, 96, 'facebook 3', True, '', 'direccion 12', 'pais 16', True, '', '', 'bibliografia 1');

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (True, '2013-05-24', 96, True, False, 'urlImagen 16');

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 3', 'observaciones 5', False, 96, False, False, 'nombre 3', True, False, '', True);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (96, 'direcciones 13', 'puntoDatum 16');

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', True, False, 96, '', False, True, True);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (False, '', True, True, False, False, 96, False, False, 'otros 20', True);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (96, 'notas 8');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (False, True, 'orientacion 17', 96, True, False, True, 'otros 15');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (96, '');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (False, 'tecnicas 10', True, 96, 'otros 13', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, 'otros 6', 96, False, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (True, True, False, '', 96, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, False, False, False, True, 96, True, True, True);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (96, NULL);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 96, True, True, True, False, True);

---------- Fin Insert Yacimiento 96

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (97, 97, 'Venezuela', 'Yacimiento 97', 'Municipio 3', 'Falcón'); 

	INSERT INTO anarapp_altitud (desarrollo, desnivel, texto, yacimiento_id, superficie, altura) 
	VALUES ('', 'desnivel 18', 'texto 15', 97, 'superficie 3', 'altura 14');

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (True, False, False, False, False, 'anchoDe 15', 'anchoDeComp 14', 'anchoA 11', 97, False, 'anchoAComp 10', False, True, 'otros 14', False);

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 97, 20, NULL, False);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, True, 36, True, True, 35, 97, NULL, True, 8);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 17', 97, 'diametro 1', 'ancho 7');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (True, False, True, False, True, False, True, False, True, '', 'anchoA 5', 'profundidadA 11', 97, False, False, 'anchoDe 11', False, False, True);

	INSERT INTO anarapp_caracsurcopuntosacopl (otros, "esPunteado", yacimiento_id, diametro, profundidad) 
	VALUES ('otros 5', False, 97, 'diametro 18', 'profundidad 3');

	INSERT INTO anarapp_considertemp ("cincoAno", yacimiento_id, otros) 
	VALUES (True, 97, 'otros 2');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (97, NULL, NULL, NULL, '', 9);

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 13', 'autor 8', False, 'institucion 17', False, 'fecha 9', True, False, False, 97, '', True, '', 'direccion 7', 'pais 5', False, 'telefono 6', '', '');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (97, '');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (9, 97);

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, False, NULL, True, 14, '', 'sumergidoPa 17', True, True, True, True, 'otros 8', 'especificar 16', True, 17, True, NULL, 7, True, 97, False, False, False, NULL, False, False, 'mas 15', False, True, '', False, True, True, True, True, '', False, False, False, False, 'patinaPa 14', False, '', 'enterradoPa 19', False, False, NULL, True, '', True, 'crecimientoVegPa 7');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('fauna 10', 97);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('', 97);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 2', 'observaciones 17', False, 97, False, False, 'nombre 5', True, True, 'otros 16', True);

	INSERT INTO anarapp_localidadyacimiento ("nombreNoPoblado", "esCentroPoblado", "esUrbano", yacimiento_id, "nombrePoblado", "esIndigena", "esCentroNoPoblado", "esRural") 
	VALUES ('', True, True, 97, 'nombrePoblado 17', False, True, True);

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (97, 3);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 8', '', True, 'descripcionMito 13', False, True, True, 'descripcionCeramica 14', 'descripcionMonticulo 15', 97, 'descripcionCarbon 15', 'descripcionOseo 17', True, True, 'otros 18', '', False, False);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (97, '');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, False, 'orientacion 8', 97, True, False, False, '');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (97, 'numeroPlano 14');

	INSERT INTO anarapp_tecnicaparageoglifo (yacimiento_id, tecnicas) 
	VALUES (97, 'tecnicas 2');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (False, 'tecnicas 17', False, 97, '', False);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, True, False, True, 97, False, False, 'otros 11', False);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, 'otros 11', 97, True, True);

	INSERT INTO anarapp_texturasuelo ("esArenoso", "esPedregoso", "esRocaMadre", mixto, yacimiento_id, "esArcilloso") 
	VALUES (True, False, False, '', 97, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (False, 'observaciones 16', 97, False, True);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, True, True, True, True, 97, True, False, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (97, NULL);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (False, 97, False, False, False, True, False);

---------- Fin Insert Yacimiento 97

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (98, 98, 'Venezuela', 'Yacimiento 98', 'Municipio 3', 'Miranda'); 

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (NULL, True, NULL, True, True, NULL, 98, 16, False, NULL);

	INSERT INTO anarapp_caracsurcocupulas (ancho, profundidad, diametro, yacimiento_id, otros, largo) 
	VALUES ('ancho 10', 'profundidad 10', 'diametro 10', 98, '', 'largo 13');

	INSERT INTO anarapp_caracsurcomortero (largo, yacimiento_id, ancho) 
	VALUES ('largo 16', 98, 'ancho 17');

	INSERT INTO anarapp_caracsurcopetroglifo ("esAreaInterlinealPulida", "esAreaInterlinealRebajada", "esGrabadoSuperpuesto", "esBaseAguda", "esBajoRelievePlanar", "esBajoRelieve", "esAltoRelieve", "esBajoRelieveLineal", "esAreaInterlineal", "produndidadDe", "anchoA", "profundidadA", yacimiento_id, "esAltoRelievePlanar", "esAltoRelieveLineal", "anchoDe", "esBase", "esBaseRedonda", "esGrabadoRebajado") 
	VALUES (True, True, False, True, False, False, True, False, True, 'produndidadDe 10', 'anchoA 12', 'profundidadA 16', 98, True, False, 'anchoDe 2', True, False, False);

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (98, NULL, NULL, 8, 'otros 4', NULL);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 19', 'utmAdicional 11', 98, 'longitud 18');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('', 'autor 7', False, '', False, 'fecha 20', True, True, True, 98, 'facebook 11', True, 'mail 12', 'direccion 20', '', True, 'telefono 14', 'twitter 20', '');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (98, '');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (NULL, 98);

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (26, False, NULL, False, 10, '', '', True, False, False, False, 'otros 1', '', False, 1, True, NULL, NULL, False, 98, True, False, True, 4, True, True, 'mas 19', False, False, 'observaciones 15', True, False, True, True, False, '', False, False, True, True, 'patinaPa 16', True, 'trasladadoPa 18', '', True, False, 33, False, 'erosionPa 16', False, 'crecimientoVegPa 14');

	INSERT INTO anarapp_faunayacimiento (fauna, yacimiento_id) 
	VALUES ('fauna 9', 98);

	INSERT INTO anarapp_florayacimiento (flora, yacimiento_id) 
	VALUES ('flora 20', 98);

	INSERT INTO anarapp_hidrologiayacimiento (distancia, observaciones, rio, yacimiento_id, arroyo, "manantialIntermitente", nombre, manantial, laguna, otros, "arroyoPerenne") 
	VALUES ('distancia 4', 'observaciones 9', True, 98, True, True, 'nombre 14', False, False, '', True);

	INSERT INTO anarapp_indicaciones (yacimiento_id, direcciones, "puntoDatum") 
	VALUES (98, '', 'puntoDatum 16');

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (98, NULL);

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, True, 'orientacion 1', 98, False, True, False, 'otros 18');

	INSERT INTO anarapp_plano (yacimiento_id, "numeroPlano") 
	VALUES (98, 'numeroPlano 7');

	INSERT INTO anarapp_tecnicaparamonumentos ("esMonolito", tecnicas, "esMenhir", yacimiento_id, otros, "esDolmen") 
	VALUES (False, '', True, 98, 'otros 10', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, '', 98, True, False);

	INSERT INTO anarapp_tipoexposicionyac (expuesto, observaciones, yacimiento_id, "noExpuesto", "expuestoPeriodicamente") 
	VALUES (True, '', 98, True, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (True, True, True, True, True, 98, False, False, False);

	INSERT INTO anarapp_usoactsuelo ("esSueloUrbano", yacimiento_id, "esForestal", "esGanadero", "esSueloTuristico", "esAgriRiesgo", "esAgriTemp") 
	VALUES (True, 98, False, True, False, True, False);

---------- Fin Insert Yacimiento 98

	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (99, 99, 'Venezuela', 'Yacimiento 99', 'Municipio 8', 'Bolívar'); 

	INSERT INTO anarapp_caracdelapintura ("esImpresionDeManosPositivo", "esPinturaRupestre", "esImpresionDeManos", "esLineaSencilla", "tienesFigurasSuperpuestas", "anchoDe", "anchoDeComp", "anchoA", yacimiento_id, "esLineaCompuesta", "anchoAComp", "esTecnicaFibra", "esImpresionDeManosNegativo", otros, "esTecnicaDactilar") 
	VALUES (False, False, True, True, True, 'anchoDe 14', 'anchoDeComp 10', 'anchoA 15', 99, True, 'anchoAComp 9', False, False, 'otros 2', True);

	INSERT INTO anarapp_caracdolmenart ("ConPetroglifo", yacimiento_id, "cantidadConPinturas", "cantidadConPetroglifo", "conPinturas") 
	VALUES (False, 99, NULL, 16, True);

	INSERT INTO anarapp_caracmenhires ("cantidadPiedrasVerticales", "ConPetroglifo", distanciamiento, "conPinturas", "sonPiedrasVerticales", "cantidadConPetroglifo", yacimiento_id, "cantidadConPuntosAcoplados", "conPuntosAcoplados", "cantidadConPinturas") 
	VALUES (6, False, 33, False, False, 30, 99, NULL, True, NULL);

	INSERT INTO anarapp_caracmonolitos ("esPinturaRupestre", yacimiento_id, "cantidadConGrabados", cantidad) 
	VALUES (False, 99, NULL, 18);

	INSERT INTO anarapp_caracsurcoamoladores (largo, yacimiento_id, diametro, ancho) 
	VALUES ('largo 19', 99, 'diametro 3', 'ancho 13');

	INSERT INTO anarapp_caracsurcobateas (largo, yacimiento_id, diametro, ancho, profundidad) 
	VALUES ('largo 11', 99, 'diametro 13', 'ancho 6', '');

	INSERT INTO anarapp_constitucionyacimiento (yacimiento_id, "nroPiedrasGrabadas", "nroPiedrasPintadas", "nroPiedrasColocadas", otros, "nroPiedras") 
	VALUES (99, NULL, 5, NULL, '', 22);

	INSERT INTO anarapp_coordenadas (latitud, "utmAdicional", yacimiento_id, longitud) 
	VALUES ('latitud 9', 'utmAdicional 12', 99, 'longitud 19');

	INSERT INTO anarapp_cronologiatentativa (tecnica, autor, "esCrono1", institucion, "esCrono4", fecha, "esCrono3", "esCrono2", "esCrono7", yacimiento_id, facebook, "esCrono5", mail, direccion, pais, "esCrono6", telefono, twitter, bibliografia) 
	VALUES ('tecnica 18', 'autor 2', True, '', False, 'fecha 16', False, False, True, 99, '', True, 'mail 10', 'direccion 10', '', True, 'telefono 19', 'twitter 16', '');

	INSERT INTO anarapp_croquis (yacimiento_id, "urlImagen") 
	VALUES (99, 'urlImagen 15');

	INSERT INTO anarapp_datum ("tipoDatum", yacimiento_id) 
	VALUES (NULL, 99);

	INSERT INTO anarapp_estadoconseryac (perdido, "enPorCausaHumana", patina, "cincoAno", sumergido, "perdidoPa", "sumergidoPa", "esInmediato", "porErosion", "porErosionExtModerada", "porAsentamientoHumand", otros, especificar, "porObraLargoPlazo", destruido, "tresAno", "crecimientoVeg", enterrado, "porObraCortoPlazo", yacimiento_id, "enPorCausaNaturalLigera", "enBuenEstado", "porNivelacion", erosion, "cuatroAno", "porExtraccionMayor", mas, "estadoModificado", "porErosionExtSevera", observaciones, "porErosionParModerada", "unAno", "esPorCausaNatural", "porErosionParSevera", "dosAno", "destruidoPa", "destruccionPotencial", "porVandalismo", "porExtraccionFamiliar", "estaDestruido", "patinaPa", "porObraMedianoPlazo", "trasladadoPa", "enterradoPa", "enPorCausaHumanaLigera", "esDeTiempo", trasladado, "enPorCausaNaturalAguda", "erosionPa", "enPorCausaHumanaAguda", "crecimientoVegPa") 
	VALUES (NULL, True, 15, True, NULL, '', 'sumergidoPa 19', True, True, True, True, '', '', True, NULL, True, NULL, NULL, True, 99, True, False, True, 33, False, True, '', True, True, '', True, True, True, False, False, '', True, True, False, True, '', False, '', 'enterradoPa 8', False, True, 16, False, 'erosionPa 8', False, 'crecimientoVegPa 9');

	INSERT INTO anarapp_fotografiayac ("noEsAerea", fecha, yacimiento_id, "esSatelital", "esAerea", "urlImagen") 
	VALUES (False, '2013-07-01', 99, True, True, '');

	INSERT INTO anarapp_manifestacionyacimiento (yacimiento_id, "tipoManifestacion") 
	VALUES (99, 1);

	INSERT INTO anarapp_manifestacionesasociadas ("descripcionConcha", "descripcionCementerio", "esLitica", "descripcionMito", "esCeramica", "esConcha", "esCementerio", "descripcionCeramica", "descripcionMonticulo", yacimiento_id, "descripcionCarbon", "descripcionOseo", "esCarbon", "esOseo", otros, "descripcionLitica", "esMonticulo", "esMito") 
	VALUES ('descripcionConcha 9', '', True, 'descripcionMito 5', True, True, False, 'descripcionCeramica 12', '', 99, '', '', True, True, '', '', False, False);

	INSERT INTO anarapp_materialyacimiento ("esPiel", tipo, "esCorteza", "esSedimentaria", "esMetamor", "esRoca", yacimiento_id, "esHueso", "esIgnea", otros, "esTierra") 
	VALUES (True, '', False, True, False, False, 99, True, False, 'otros 9', False);

	INSERT INTO anarapp_notasyacimiento (yacimiento_id, notas) 
	VALUES (99, '');

	INSERT INTO anarapp_orientacionyacimiento ("haciaRio", "haciaValle", orientacion, yacimiento_id, "haciaCosta", "haciaCerro", "haciaCielo", otros) 
	VALUES (True, True, 'orientacion 10', 99, True, True, True, 'otros 6');

	INSERT INTO anarapp_tecnicaparamicropetro ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (True, False, True, False, 99, False, True, 'otros 1', True);

	INSERT INTO anarapp_tecnicaparapetroglifo ("esGrabadoPercusionDirecta", "esGrabadoPercusionIndirecta", "esGrabado", "esGrabadoPercusion", yacimiento_id, "esAbrasion", "esAbrasionArena", otros, "esAbrasionPiedra") 
	VALUES (False, True, True, False, 99, True, True, 'otros 15', True);

	INSERT INTO anarapp_tecnicaparapintura (soplado, otros, yacimiento_id, fibra, "conDedo") 
	VALUES (True, '', 99, False, False);

	INSERT INTO anarapp_tenenciadetierra ("esMunicipal", "esPrivada", "esTenenciaOtros", yacimiento_id, "esComunal", "esABRAE", "esEjido") 
	VALUES (False, True, '', 99, True, False, False);

	INSERT INTO anarapp_tipoyacimiento ("esParedRocosa", "esCuevadeRec", "esTerrenoPro", "esCueva", "esAbrigo", yacimiento_id, "esRoca", "esTerrenoSup", "esDolmen") 
	VALUES (False, True, True, False, True, 99, True, True, False);

	INSERT INTO anarapp_ubicacionyacimiento (yacimiento_id, "ubicacionManifestacion") 
	VALUES (99, NULL);

---------- Fin Insert Yacimiento 99

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (0, 22, 'Miranda', 33, 'Nombre de las Figuras 11', 'Piedra 0', '0', '3', 'Manifestaciones Asociadas 7'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (17, 0, 'numero 9');

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (0, 17);

	INSERT INTO anarapp_ubicacioncaras (piedra_id, "lagoInterior", "salaPrincipal", "requiereAndamiaje", luminosidad, claraboya, "todaLaCaverna", "otraSala", "areasEspecificas") 
	VALUES (0, False, True, True, 36, False, False, True, False);

---------- Fin Insert Piedra 0

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (1, 11, 'Nueva Esparta', 22, 'Nombre de las Figuras 15', 'Piedra 1', '1', '47', 'Manifestaciones Asociadas 20'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (32, 1, 'numero 4');

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('posicion 17', 1, '', 'numero 4');

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (1, 'persona 14', '', 36);

---------- Fin Insert Piedra 1

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (2, 14, 'Anzoategui', 16, 'Nombre de las Figuras 3', 'Piedra 2', '2', '63', 'Manifestaciones Asociadas 3'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (23, 2, 'numero 3');

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (2, 10);

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (2);

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (2, True, False, False, True, True);

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (2, '', '', 33);

	INSERT INTO anarapp_ubicacioncaras (piedra_id, "lagoInterior", "salaPrincipal", "requiereAndamiaje", luminosidad, claraboya, "todaLaCaverna", "otraSala", "areasEspecificas") 
	VALUES (2, False, False, False, 19, False, True, True, False);

---------- Fin Insert Piedra 2

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (3, 38, 'Monagas', 25, 'Nombre de las Figuras 1', 'Piedra 3', '3', '89', 'Manifestaciones Asociadas 12'); 

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (3, 37);

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (3);

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (3, 'cantidad 18', 'numero 5', 'descripcion 2', 33, True);

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (3, False, True, True, True, False);

---------- Fin Insert Piedra 3

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (4, 9, 'Apure', 8, 'Nombre de las Figuras 14', 'Piedra 4', '4', '93', 'Manifestaciones Asociadas 8'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (20, 4, 'numero 8');

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (4, 7);

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (4);

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('', 4, 'textoCara 15', 'numero 7');

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (4, '', '', 11);

---------- Fin Insert Piedra 4

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (5, 13, 'Bolívar', 33, 'Nombre de las Figuras 18', 'Piedra 5', '5', '60', 'Manifestaciones Asociadas 17'); 

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (5, 17);

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (5);

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('posicion 1', 5, 'textoCara 16', 'numero 4');

	INSERT INTO anarapp_ubicacioncaras (piedra_id, "lagoInterior", "salaPrincipal", "requiereAndamiaje", luminosidad, claraboya, "todaLaCaverna", "otraSala", "areasEspecificas") 
	VALUES (5, False, False, False, NULL, False, False, True, False);

---------- Fin Insert Piedra 5

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (6, 39, 'Yaracuy', 39, 'Nombre de las Figuras 14', 'Piedra 6', '6', '93', 'Manifestaciones Asociadas 14'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (23, 6, 'numero 7');

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (6, 'cantidad 14', 'numero 1', '', 15, True);

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (6, '', '', 39);

	INSERT INTO anarapp_ubicacioncaras (piedra_id, "lagoInterior", "salaPrincipal", "requiereAndamiaje", luminosidad, claraboya, "todaLaCaverna", "otraSala", "areasEspecificas") 
	VALUES (6, True, True, True, NULL, True, False, True, False);

---------- Fin Insert Piedra 6

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (7, 13, 'Amazonas', 22, 'Nombre de las Figuras 5', 'Piedra 7', '7', '47', 'Manifestaciones Asociadas 13'); 

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('posicion 9', 7, '', 'numero 19');

---------- Fin Insert Piedra 7

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (8, 16, 'Tachira', 9, 'Nombre de las Figuras 8', 'Piedra 8', '8', '46', 'Manifestaciones Asociadas 14'); 

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (8, 1);

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (8);

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (8, 'persona 16', 'instituto 18', 9);

---------- Fin Insert Piedra 8

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (9, 20, 'Apure', 22, 'Nombre de las Figuras 9', 'Piedra 9', '9', '77', 'Manifestaciones Asociadas 5'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (27, 9, 'numero 4');

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (9, 39);

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (9);

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('', 9, '', 'numero 17');

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (9, 'cantidad 3', 'numero 18', '', 10, True);

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (9, False, False, True, False, True);

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (9, '', 'instituto 4', 37);

---------- Fin Insert Piedra 9

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (10, 3, 'Cojedes', 40, 'Nombre de las Figuras 16', 'Piedra 10', '10', '94', 'Manifestaciones Asociadas 12'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (31, 10, 'numero 8');

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (10, 1);

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (10);

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (10, 'cantidad 8', 'numero 17', '', 39, True);

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (10, True, False, True, False, False);

---------- Fin Insert Piedra 10

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (11, 10, 'Tachira', 13, 'Nombre de las Figuras 8', 'Piedra 11', '11', '38', 'Manifestaciones Asociadas 7'); 

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (11, 37);

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (11);

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('', 11, '', 'numero 10');

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (11, True, False, True, True, True);

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (11, 'persona 16', '', 22);

---------- Fin Insert Piedra 11

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (12, 32, 'Bolívar', 9, 'Nombre de las Figuras 1', 'Piedra 12', '12', '86', 'Manifestaciones Asociadas 17'); 

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (12, 15);

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (12);

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('posicion 15', 12, '', 'numero 14');

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (12, 'persona 1', 'instituto 19', 34);

---------- Fin Insert Piedra 12

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (13, 15, 'Amazonas', 10, 'Nombre de las Figuras 18', 'Piedra 13', '13', '45', 'Manifestaciones Asociadas 17'); 

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (13);

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('', 13, '', 'numero 15');

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (13, 'cantidad 15', 'numero 16', '', 10, True);

	INSERT INTO anarapp_ubicacioncaras (piedra_id, "lagoInterior", "salaPrincipal", "requiereAndamiaje", luminosidad, claraboya, "todaLaCaverna", "otraSala", "areasEspecificas") 
	VALUES (13, True, False, False, 10, True, True, False, False);

---------- Fin Insert Piedra 13

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (14, 40, 'Cojedes', 4, 'Nombre de las Figuras 8', 'Piedra 14', '14', '72', 'Manifestaciones Asociadas 6'); 

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (14, 10);

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (14);

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('posicion 15', 14, '', 'numero 3');

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (14, True, False, False, False, False);

---------- Fin Insert Piedra 14

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (15, 14, 'Cojedes', 40, 'Nombre de las Figuras 13', 'Piedra 15', '15', '5', 'Manifestaciones Asociadas 4'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (18, 15, 'numero 19');

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (15, True, False, True, True, True);

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (15, 'persona 19', 'instituto 8', 29);

	INSERT INTO anarapp_ubicacioncaras (piedra_id, "lagoInterior", "salaPrincipal", "requiereAndamiaje", luminosidad, claraboya, "todaLaCaverna", "otraSala", "areasEspecificas") 
	VALUES (15, True, False, True, NULL, False, False, False, False);

---------- Fin Insert Piedra 15

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (16, 32, 'Tachira', 37, 'Nombre de las Figuras 3', 'Piedra 16', '16', '54', 'Manifestaciones Asociadas 5'); 

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (16);

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('', 16, '', 'numero 17');

---------- Fin Insert Piedra 16

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (17, 18, 'Sucre', 33, 'Nombre de las Figuras 6', 'Piedra 17', '17', '25', 'Manifestaciones Asociadas 19'); 

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (17, 31);

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (17);

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (17, True, True, False, True, True);

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (17, 'persona 14', 'instituto 2', 30);

---------- Fin Insert Piedra 17

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (18, 31, 'Delta Amacuro', 17, 'Nombre de las Figuras 13', 'Piedra 18', '18', '91', 'Manifestaciones Asociadas 9'); 

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (18, 32);

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (18);

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (18, False, False, False, True, False);

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (18, '', '', 33);

	INSERT INTO anarapp_ubicacioncaras (piedra_id, "lagoInterior", "salaPrincipal", "requiereAndamiaje", luminosidad, claraboya, "todaLaCaverna", "otraSala", "areasEspecificas") 
	VALUES (18, True, False, False, NULL, False, True, False, True);

---------- Fin Insert Piedra 18

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (19, 13, 'Yaracuy', 33, 'Nombre de las Figuras 15', 'Piedra 19', '19', '52', 'Manifestaciones Asociadas 8'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (11, 19, 'numero 5');

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('posicion 2', 19, '', 'numero 1');

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (19, 'cantidad 11', 'numero 14', '', 20, True);

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (19, True, False, False, False, False);

	INSERT INTO anarapp_ubicacioncaras (piedra_id, "lagoInterior", "salaPrincipal", "requiereAndamiaje", luminosidad, claraboya, "todaLaCaverna", "otraSala", "areasEspecificas") 
	VALUES (19, True, True, True, 24, True, False, False, True);

---------- Fin Insert Piedra 19

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (20, 21, 'Cojedes', 38, 'Nombre de las Figuras 17', 'Piedra 20', '20', '91', 'Manifestaciones Asociadas 20'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (6, 20, 'numero 15');

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (20, 11);

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (20);

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('', 20, 'textoCara 20', 'numero 6');

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (20, False, True, False, False, False);

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (20, '', 'instituto 12', 29);

---------- Fin Insert Piedra 20

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (21, 18, 'Cojedes', 27, 'Nombre de las Figuras 17', 'Piedra 21', '21', '22', 'Manifestaciones Asociadas 12'); 

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (21, 25);

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('', 21, 'textoCara 3', 'numero 2');

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (21, 'persona 19', '', 23);

---------- Fin Insert Piedra 21

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (22, 1, 'Vargas', 18, 'Nombre de las Figuras 14', 'Piedra 22', '22', '99', 'Manifestaciones Asociadas 3'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (17, 22, 'numero 3');

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (22);

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('', 22, '', 'numero 6');

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (22, 'cantidad 5', 'numero 3', 'descripcion 20', 24, True);

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (22, True, True, True, True, True);

	INSERT INTO anarapp_ubicacioncaras (piedra_id, "lagoInterior", "salaPrincipal", "requiereAndamiaje", luminosidad, claraboya, "todaLaCaverna", "otraSala", "areasEspecificas") 
	VALUES (22, True, True, False, NULL, True, False, False, False);

---------- Fin Insert Piedra 22

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (23, 10, 'Monagas', 27, 'Nombre de las Figuras 17', 'Piedra 23', '23', '19', 'Manifestaciones Asociadas 4'); 

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('posicion 17', 23, '', 'numero 12');

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (23, False, True, False, False, True);

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (23, '', '', 32);

	INSERT INTO anarapp_ubicacioncaras (piedra_id, "lagoInterior", "salaPrincipal", "requiereAndamiaje", luminosidad, claraboya, "todaLaCaverna", "otraSala", "areasEspecificas") 
	VALUES (23, False, False, True, 26, False, True, True, True);

---------- Fin Insert Piedra 23

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (24, 26, 'Cojedes', 22, 'Nombre de las Figuras 1', 'Piedra 24', '24', '11', 'Manifestaciones Asociadas 1'); 

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (24, 'cantidad 13', 'numero 17', '', 30, True);

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (24, False, True, False, False, False);

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (24, '', '', 26);

	INSERT INTO anarapp_ubicacioncaras (piedra_id, "lagoInterior", "salaPrincipal", "requiereAndamiaje", luminosidad, claraboya, "todaLaCaverna", "otraSala", "areasEspecificas") 
	VALUES (24, False, True, True, NULL, True, False, True, True);

---------- Fin Insert Piedra 24

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (25, 16, 'Trujillo', 34, 'Nombre de las Figuras 8', 'Piedra 25', '25', '48', 'Manifestaciones Asociadas 12'); 

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (25, 2);

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (25);

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('posicion 20', 25, '', 'numero 19');

	INSERT INTO anarapp_ubicacioncaras (piedra_id, "lagoInterior", "salaPrincipal", "requiereAndamiaje", luminosidad, claraboya, "todaLaCaverna", "otraSala", "areasEspecificas") 
	VALUES (25, True, False, True, NULL, True, True, False, True);

---------- Fin Insert Piedra 25

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (26, 40, 'Mérida', 21, 'Nombre de las Figuras 2', 'Piedra 26', '26', '14', 'Manifestaciones Asociadas 6'); 

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (26, 6);

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (26, 'cantidad 5', 'numero 14', 'descripcion 5', 37, True);

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (26, 'persona 8', 'instituto 11', 40);

---------- Fin Insert Piedra 26

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (27, 33, 'Carabobo', 8, 'Nombre de las Figuras 7', 'Piedra 27', '27', '35', 'Manifestaciones Asociadas 8'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (1, 27, 'numero 8');

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (27, 40);

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (27);

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('posicion 14', 27, '', 'numero 17');

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (27, 'persona 5', '', 28);

---------- Fin Insert Piedra 27

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (28, 5, 'Carabobo', 35, 'Nombre de las Figuras 5', 'Piedra 28', '28', '87', 'Manifestaciones Asociadas 18'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (40, 28, 'numero 1');

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (28, 15);

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('', 28, 'textoCara 18', 'numero 9');

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (28, 'cantidad 17', 'numero 8', '', 14, True);

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (28, False, False, False, True, False);

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (28, 'persona 7', '', 25);

---------- Fin Insert Piedra 28

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (29, 36, 'Anzoategui', 15, 'Nombre de las Figuras 18', 'Piedra 29', '29', '3', 'Manifestaciones Asociadas 15'); 

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (29);

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (29, 'cantidad 9', 'numero 13', '', 27, False);

	INSERT INTO anarapp_ubicacioncaras (piedra_id, "lagoInterior", "salaPrincipal", "requiereAndamiaje", luminosidad, claraboya, "todaLaCaverna", "otraSala", "areasEspecificas") 
	VALUES (29, False, True, False, 19, True, True, False, False);

---------- Fin Insert Piedra 29

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (30, 10, 'Apure', 37, 'Nombre de las Figuras 14', 'Piedra 30', '30', '91', 'Manifestaciones Asociadas 3'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (29, 30, 'numero 17');

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (30, 22);

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('posicion 7', 30, 'textoCara 15', 'numero 3');

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (30, '', '', 17);

---------- Fin Insert Piedra 30

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (31, 6, 'Zulia', 14, 'Nombre de las Figuras 5', 'Piedra 31', '31', '57', 'Manifestaciones Asociadas 13'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (12, 31, 'numero 18');

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (31, 1);

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (31, False, True, False, True, True);

---------- Fin Insert Piedra 31

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (32, 29, 'Guárico', 18, 'Nombre de las Figuras 5', 'Piedra 32', '32', '70', 'Manifestaciones Asociadas 3'); 

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (32);

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (32, 'cantidad 4', 'numero 5', 'descripcion 6', 8, False);

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (32, False, True, True, False, False);

---------- Fin Insert Piedra 32

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (33, 13, 'Tachira', 9, 'Nombre de las Figuras 17', 'Piedra 33', '33', '45', 'Manifestaciones Asociadas 15'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (14, 33, 'numero 4');

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (33);

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('', 33, 'textoCara 6', 'numero 4');

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (33, True, True, False, True, False);

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (33, 'persona 10', '', 32);

---------- Fin Insert Piedra 33

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (34, 20, 'Carabobo', 39, 'Nombre de las Figuras 5', 'Piedra 34', '34', '31', 'Manifestaciones Asociadas 7'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (20, 34, 'numero 16');

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (34);

---------- Fin Insert Piedra 34

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (35, 27, 'Tachira', 11, 'Nombre de las Figuras 14', 'Piedra 35', '35', '63', 'Manifestaciones Asociadas 3'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (10, 35, 'numero 16');

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (35, 27);

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (35);

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (35, 'cantidad 20', 'numero 11', 'descripcion 18', 4, False);

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (35, False, False, True, False, True);

---------- Fin Insert Piedra 35

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (36, 19, 'Lara', 8, 'Nombre de las Figuras 8', 'Piedra 36', '36', '95', 'Manifestaciones Asociadas 15'); 

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (36);

---------- Fin Insert Piedra 36

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (37, 30, 'Zulia', 18, 'Nombre de las Figuras 12', 'Piedra 37', '37', '57', 'Manifestaciones Asociadas 14'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (39, 37, 'numero 7');

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (37);

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('posicion 11', 37, '', 'numero 8');

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (37, 'cantidad 11', 'numero 19', '', 27, False);

	INSERT INTO anarapp_ubicacioncaras (piedra_id, "lagoInterior", "salaPrincipal", "requiereAndamiaje", luminosidad, claraboya, "todaLaCaverna", "otraSala", "areasEspecificas") 
	VALUES (37, True, True, False, 7, True, False, False, True);

---------- Fin Insert Piedra 37

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (38, 11, 'Anzoategui', 19, 'Nombre de las Figuras 20', 'Piedra 38', '38', '40', 'Manifestaciones Asociadas 5'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (32, 38, 'numero 10');

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('posicion 17', 38, '', 'numero 5');

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (38, 'cantidad 20', 'numero 16', '', 11, True);

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (38, False, True, True, True, True);

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (38, '', 'instituto 19', 21);

	INSERT INTO anarapp_ubicacioncaras (piedra_id, "lagoInterior", "salaPrincipal", "requiereAndamiaje", luminosidad, claraboya, "todaLaCaverna", "otraSala", "areasEspecificas") 
	VALUES (38, False, True, True, NULL, True, False, False, True);

---------- Fin Insert Piedra 38

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (39, 36, 'Sucre', 19, 'Nombre de las Figuras 11', 'Piedra 39', '39', '86', 'Manifestaciones Asociadas 5'); 

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (39, 19);

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (39);

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('posicion 8', 39, '', 'numero 20');

	INSERT INTO anarapp_ubicacioncaras (piedra_id, "lagoInterior", "salaPrincipal", "requiereAndamiaje", luminosidad, claraboya, "todaLaCaverna", "otraSala", "areasEspecificas") 
	VALUES (39, True, True, False, NULL, False, False, False, True);

---------- Fin Insert Piedra 39

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (40, 1, 'Yaracuy', 12, 'Nombre de las Figuras 17', 'Piedra 40', '40', '52', 'Manifestaciones Asociadas 1'); 

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (40, 13);

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (40, 'cantidad 16', 'numero 8', 'descripcion 18', 10, True);

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (40, 'persona 6', '', 30);

	INSERT INTO anarapp_ubicacioncaras (piedra_id, "lagoInterior", "salaPrincipal", "requiereAndamiaje", luminosidad, claraboya, "todaLaCaverna", "otraSala", "areasEspecificas") 
	VALUES (40, True, False, False, NULL, True, True, True, False);

---------- Fin Insert Piedra 40

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (41, 11, 'Monagas', 29, 'Nombre de las Figuras 10', 'Piedra 41', '41', '33', 'Manifestaciones Asociadas 7'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (32, 41, 'numero 20');

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (41, 31);

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (41);

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (41, 'cantidad 19', 'numero 11', 'descripcion 15', 28, False);

	INSERT INTO anarapp_ubicacioncaras (piedra_id, "lagoInterior", "salaPrincipal", "requiereAndamiaje", luminosidad, claraboya, "todaLaCaverna", "otraSala", "areasEspecificas") 
	VALUES (41, True, True, True, NULL, True, False, False, True);

---------- Fin Insert Piedra 41

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (42, 24, 'Guárico', 13, 'Nombre de las Figuras 17', 'Piedra 42', '42', '32', 'Manifestaciones Asociadas 7'); 

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (42, 26);

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('posicion 6', 42, 'textoCara 19', 'numero 12');

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (42, 'cantidad 15', 'numero 15', '', 7, True);

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (42, False, False, False, False, True);

---------- Fin Insert Piedra 42

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (43, 9, 'Portuguesa', 23, 'Nombre de las Figuras 1', 'Piedra 43', '43', '82', 'Manifestaciones Asociadas 9'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (35, 43, 'numero 8');

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (43);

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (43, 'cantidad 17', 'numero 6', 'descripcion 13', 36, True);

---------- Fin Insert Piedra 43

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (44, 28, 'Tachira', 34, 'Nombre de las Figuras 16', 'Piedra 44', '44', '29', 'Manifestaciones Asociadas 15'); 

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (44, 19);

	INSERT INTO anarapp_dimensionpiedra (piedra_id) 
	VALUES (44);

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('posicion 20', 44, 'textoCara 18', 'numero 10');

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (44, 'cantidad 10', 'numero 6', '', 25, True);

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (44, 'persona 11', 'instituto 5', 12);

---------- Fin Insert Piedra 44

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (45, 30, 'Monagas', 24, 'Nombre de las Figuras 13', 'Piedra 45', '45', '9', 'Manifestaciones Asociadas 4'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (15, 45, 'numero 1');

	INSERT INTO anarapp_conexionfiguras (piedra_id, "conexionFiguras") 
	VALUES (45, 28);

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('', 45, 'textoCara 14', 'numero 7');

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (45, 'cantidad 18', 'numero 8', 'descripcion 8', 20, True);

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (45, True, False, False, False, False);

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (45, 'persona 11', 'instituto 16', 26);

	INSERT INTO anarapp_ubicacioncaras (piedra_id, "lagoInterior", "salaPrincipal", "requiereAndamiaje", luminosidad, claraboya, "todaLaCaverna", "otraSala", "areasEspecificas") 
	VALUES (45, True, False, True, NULL, True, True, False, True);

---------- Fin Insert Piedra 45

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (46, 17, 'Aragua', 37, 'Nombre de las Figuras 2', 'Piedra 46', '46', '90', 'Manifestaciones Asociadas 2'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (33, 46, 'numero 15');

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('posicion 13', 46, 'textoCara 14', 'numero 17');

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (46, 'cantidad 9', 'numero 3', '', 28, True);

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (46, True, False, False, True, False);

	INSERT INTO anarapp_ubicacioncaras (piedra_id, "lagoInterior", "salaPrincipal", "requiereAndamiaje", luminosidad, claraboya, "todaLaCaverna", "otraSala", "areasEspecificas") 
	VALUES (46, False, False, False, 13, False, False, True, False);

---------- Fin Insert Piedra 46

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (47, 3, 'Delta Amacuro', 36, 'Nombre de las Figuras 8', 'Piedra 47', '47', '25', 'Manifestaciones Asociadas 10'); 

	INSERT INTO anarapp_caratrabajada (orientacion, piedra_id, numero) 
	VALUES (29, 47, 'numero 14');

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('posicion 6', 47, 'textoCara 20', 'numero 3');

	INSERT INTO anarapp_ubicacioncaras (piedra_id, "lagoInterior", "salaPrincipal", "requiereAndamiaje", luminosidad, claraboya, "todaLaCaverna", "otraSala", "areasEspecificas") 
	VALUES (47, False, False, True, 5, True, False, True, True);

---------- Fin Insert Piedra 47

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (48, 38, 'Monagas', 28, 'Nombre de las Figuras 1', 'Piedra 48', '48', '4', 'Manifestaciones Asociadas 2'); 

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('', 48, '', 'numero 3');

	INSERT INTO anarapp_figurasportipo (piedra_id, cantidad, numero, descripcion, "tipoFigura", "esCantidadInexacta") 
	VALUES (48, 'cantidad 13', 'numero 14', 'descripcion 8', 14, True);

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (48, '', 'instituto 20', 13);

---------- Fin Insert Piedra 48

	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (49, 14, 'Portuguesa', 25, 'Nombre de las Figuras 10', 'Piedra 49', '49', '22', 'Manifestaciones Asociadas 20'); 

	INSERT INTO anarapp_esquemaporcara (posicion, piedra_id, "textoCara", numero) 
	VALUES ('', 49, '', 'numero 19');

	INSERT INTO anarapp_manifestaciones (piedra_id, "tienePinturaRupestre", "tienePetroglifo", "tieneAmoladores", "tienePuntosAcoplados", "tieneCupulas") 
	VALUES (49, False, False, False, True, True);

	INSERT INTO anarapp_repgrafpiedra (piedra_id, persona, instituto, "numPiezas") 
	VALUES (49, '', 'instituto 5', 16);

	INSERT INTO anarapp_ubicacioncaras (piedra_id, "lagoInterior", "salaPrincipal", "requiereAndamiaje", luminosidad, claraboya, "todaLaCaverna", "otraSala", "areasEspecificas") 
	VALUES (49, True, False, True, NULL, True, True, True, False);

---------- Fin Insert Piedra 49


---------- La sequencia de yacimiento y piedra no se actualiza, y por tanto no permite insertar registros.

	SELECT setval('anarapp_yacimiento_id_seq', (SELECT MAX(id) FROM anarapp_yacimiento)+1);

	SELECT setval('anarapp_piedra_id_seq', (SELECT MAX(id) FROM anarapp_piedra)+1);
