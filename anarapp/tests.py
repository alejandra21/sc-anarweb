# -*- coding: utf-8 -*-
from django.test import TestCase
from datetime import date
import random
import anarapp.models
import inspect


ESTADOS = [
	'Amazonas', 'Anzoategui', 'Apure',
	'Aragua', 'Barinas', 'Bolívar',
	'Carabobo', 'Cojedes', 'Delta Amacuro',
	'Falcón', 'Guárico', 'Lara', 'Mérida',
	'Miranda', 'Monagas', 'Nueva Esparta', 
	'Portuguesa', 'Sucre', 'Tachira', 
	'Trujillo', 'Vargas', 'Yaracuy', 'Zulia'
]

obligatorios = ['altura', 'superficie', 'anchoDe', 'anchoA', 'anchoDeComp', 'anchoAComp', 'largo', 'ancho', 'diametro', 'profundidadDe', 'profundidadA', 'longitud', 'latitud', 'fecha', 'distancia', 'nombre', 'texto', 'altoMaximo', 'bocaPrincipal', 'numero', 'alto', 'cantidad', 'conexionFiguras', 'numPiezas', 'orientacion', 'tipoFigura', 'largoMaximo']

def random_int(maximo, obligatorio = False):
	if bool(random.getrandbits(1)) or obligatorio:
		return str(random.randint(1, maximo))
	return 'NULL'


def random_text(text, obligatorio = False):
	if bool(random.getrandbits(1)) or obligatorio:
		return  '\'%s %d\'' % (text, random.randint(1,20))
	return '\'\''


def random_date(obligatorio = False):
	if bool(random.getrandbits(1)) or obligatorio:
		start_date = date.today().replace(day=1, month=1).toordinal()
		end_date = date.today().toordinal()
		return  '\'%s\'' % date.fromordinal(random.randint(start_date, end_date))
	return 'NULL'	

def yacimiento(i, inserts):
	
	yacimiento 	= 'Yacimiento ' + str(i)
	municipio 	= 'Municipio ' + str(random.randint(1,20))
	estado 		= ESTADOS[random.randint(0,22)]
	
	print >> inserts, """
	INSERT INTO anarapp_yacimiento (id, codigo, pais, nombre, municipio, estado) 
	VALUES (%d, %s, 'Venezuela', '%s', '%s', '%s'); """ % (i, i, yacimiento, municipio, estado)

	for name, obj in inspect.getmembers(anarapp.models):
		if inspect.isclass(obj) and obj.__module__ == 'anarapp.models':
			if bool(random.getrandbits(1)) and name != 'Yacimiento':
				
				#FALTA: Objetos con herencia	
				if any(x.endswith('_ptr') for x in obj.__dict__):
					continue;
				
				attrs = {}
				
				if 'yacimiento' in obj.__dict__ and name != 'Piedra':
				
					for field in obj._meta.fields:
						if field.name == 'id':
							continue

						atype = field.get_internal_type()
						fieldname = field.name
						if any(x.isupper() for x in field.name):
							fieldname = '"' + fieldname + '"'

						if atype == 'CharField':
							attrs[fieldname] = random_text(field.name, field.name in obligatorios)
						elif atype == 'IntegerField':
							attrs[fieldname] = random_int(40, field.name in obligatorios)
						elif atype == 'BooleanField':
							attrs[fieldname] = bool(random.getrandbits(1))				
						elif atype == 'DateField':
							attrs[fieldname] = random_date(field.name in obligatorios)
						elif atype == 'OneToOneField' or atype == 'ForeignKey':
							attrs[fieldname + '_id'] = i

					print  >> inserts, """
	INSERT INTO anarapp_%s (%s) 
	VALUES (%s);""" % (name.lower(), ', '.join(map(str, list(attrs.keys()))), ', '.join(map(str, attrs.values())))


def piedra(i, inserts):
	
	yacimiento = random_int(99, True)
	piedra 	= 'Piedra ' + str(i)
	manifes = random_text('Manifestaciones Asociadas', True)
	figuras = random_text('Nombre de las Figuras', True)
	estado 	= ESTADOS[random.randint(0,22)]
	numcara = random_int(40, True)
	caratrb	= random_int(40, True)
	
	print  >> inserts, """
	INSERT INTO anarapp_piedra (id, "numeroCarasTrajabadas", estado, "numeroCaras", "nombreFiguras", nombre, codigo, yacimiento_id, "manifiestacionAsociada") 
	VALUES (%s, %s, '%s', %s, %s, '%s', '%s', '%s', %s); """ % (i, caratrb, estado, numcara, figuras, piedra, i, yacimiento, manifes)

	for name, obj in inspect.getmembers(anarapp.models):
		if inspect.isclass(obj) and obj.__module__ == 'anarapp.models':
			if bool(random.getrandbits(1)) and name != 'Piedra':
				
				#FALTA: Objetos con herencia	
				if any(x.endswith('_ptr') for x in obj.__dict__):
					continue;
				
				attrs = {}
				
				if 'piedra' in obj.__dict__:
				
					for field in obj._meta.fields:
						if field.name == 'id':
							continue

						atype = field.get_internal_type()
						fieldname = field.name
						if any(x.isupper() for x in field.name):
							fieldname = '"' + fieldname + '"'

						if atype == 'CharField':
							attrs[fieldname] = random_text(field.name, field.name in obligatorios)
						elif atype == 'IntegerField':
							attrs[fieldname] = random_int(40, field.name in obligatorios)
						elif atype == 'BooleanField':
							attrs[fieldname] = bool(random.getrandbits(1))				
						elif atype == 'DateField':
							attrs[fieldname] = random_date(field.name in obligatorios)
						elif atype == 'OneToOneField' or atype == 'ForeignKey':
							attrs[fieldname + '_id'] = i

					print >> inserts, """
	INSERT INTO anarapp_%s (%s) 
	VALUES (%s);""" % (name.lower(), ', '.join(map(str, list(attrs.keys()))), ', '.join(map(str, attrs.values())))


#############################################################3

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

class SimpleTest(TestCase):
    def test_basic_addition(self):
		inserts = open('inserts.sql', 'w')
		
		for i in range(0, 100):
			yacimiento(i, inserts)
				
			print >> inserts, '\n---------- Fin Insert Yacimiento ' + str(i)
	
		for i in range(0, 50):
			piedra(i, inserts)
				
			print >> inserts, '\n---------- Fin Insert Piedra ' + str(i)

		return self.assertEqual(True, True)
