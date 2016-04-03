# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Estado'
        db.create_table('anarapp_estado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('activo', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['Estado'])

        # Adding model 'Municipio'
        db.create_table('anarapp_municipio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Municipio', to=orm['anarapp.Estado'])),
            ('activo', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['Municipio'])

        # Adding model 'Yacimiento'
        db.create_table('anarapp_yacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('pais', self.gf('anarapp.models.CharField')(default='Venezuela', max_length=65000)),
            ('nombre', self.gf('anarapp.models.CharField')(max_length=65000, null=True, blank=True)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='EstadoYac', null=True, to=orm['anarapp.Estado'])),
            ('municipio', self.gf('smart_selects.db_fields.ChainedForeignKey')(blank=True, related_name='MunicipioYac', null=True, to=orm['anarapp.Municipio'])),
        ))
        db.send_create_signal('anarapp', ['Yacimiento'])

        # Adding model 'LocalidadYacimiento'
        db.create_table('anarapp_localidadyacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='LocalidadYacimiento', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esCentroPoblado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esUrbano', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esRural', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esIndigena', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nombrePoblado', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('esCentroNoPoblado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nombreNoPoblado', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['LocalidadYacimiento'])

        # Adding model 'UsoActSuelo'
        db.create_table('anarapp_usoactsuelo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='UsoActSuelo', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esForestal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esGanadero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAgriRiesgo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAgriTemp', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esSueloUrbano', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esSueloTuristico', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('anarapp', ['UsoActSuelo'])

        # Adding model 'TenenciaDeTierra'
        db.create_table('anarapp_tenenciadetierra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='TenenciaDeTierra', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esPrivada', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esComunal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esEjido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMunicipal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esABRAE', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esTenenciaOtros', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['TenenciaDeTierra'])

        # Adding model 'Indicaciones'
        db.create_table('anarapp_indicaciones', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='Indicaciones', unique=True, to=orm['anarapp.Yacimiento'])),
            ('direcciones', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('puntoDatum', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['Indicaciones'])

        # Adding model 'Croquis'
        db.create_table('anarapp_croquis', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Croquis', to=orm['anarapp.Yacimiento'])),
            ('archivo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['Croquis'])

        # Adding model 'Plano'
        db.create_table('anarapp_plano', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='Plano', unique=True, to=orm['anarapp.Yacimiento'])),
            ('numeroPlano', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['Plano'])

        # Adding model 'Coordenadas'
        db.create_table('anarapp_coordenadas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='Coordenadas', unique=True, to=orm['anarapp.Yacimiento'])),
            ('longitud', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('latitud', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('utmAdicional', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['Coordenadas'])

        # Adding model 'Datum'
        db.create_table('anarapp_datum', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='Datum', unique=True, to=orm['anarapp.Yacimiento'])),
            ('tipoDatum', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['Datum'])

        # Adding model 'Altitud'
        db.create_table('anarapp_altitud', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='Altitud', unique=True, to=orm['anarapp.Yacimiento'])),
            ('texto', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('altura', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('superficie', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('desarrollo', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('desnivel', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['Altitud'])

        # Adding model 'FotografiaYac'
        db.create_table('anarapp_fotografiayac', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='FotografiaYac', to=orm['anarapp.Yacimiento'])),
            ('esAerea', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('noEsAerea', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esSatelital', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fecha', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('archivo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['FotografiaYac'])

        # Adding model 'TipoYacimiento'
        db.create_table('anarapp_tipoyacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='TipoYacimiento', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esParedRocosa', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esRoca', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esDolmen', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAbrigo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCueva', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCuevadeRec', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esTerrenoSup', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esTerrenoPro', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('anarapp', ['TipoYacimiento'])

        # Adding model 'ManifestacionYacimiento'
        db.create_table('anarapp_manifestacionyacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='ManifestacionYacimiento', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esGeoglifo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esPintura', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esPetroglifo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esPetroglifoPintado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMicroPetroglifo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esPiedraMiticaNatural', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCerroMiticoNatural', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCerroConPetroglifo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCerroConPintura', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCerroConDolmen', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMonumentosMegaliticos', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMonolitos', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMonolitoConGrabados', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMenhires', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMenhiresConPuntos', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMenhiresConPetroglifo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMenhiresConPintura', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAmolador', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esBatea', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esPuntosAcoplados', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCupulas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMortero', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('anarapp', ['ManifestacionYacimiento'])

        # Adding model 'UbicacionYacimiento'
        db.create_table('anarapp_ubicacionyacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='UbicacionYacimiento', unique=True, to=orm['anarapp.Yacimiento'])),
            ('enCerro', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enCerroCima', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enCerroLadera', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enCerroFalda', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enCerroFila', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enCerroPieDeMonte', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enCerroBarranco', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enCerroAcantilado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enValle', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enRio', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enRioLecho', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enRioMargenDerecha', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enRioMargenIzquierda', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enRioIsla', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enRioRaudal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enRioCosta', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('anarapp', ['UbicacionYacimiento'])

        # Adding model 'OrientacionYacimiento'
        db.create_table('anarapp_orientacionyacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='OrientacionYacimiento', unique=True, to=orm['anarapp.Yacimiento'])),
            ('haciaCerro', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('haciaValle', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('haciaRio', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('haciaCosta', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('haciaCielo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otros', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('orientacion', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['OrientacionYacimiento'])

        # Adding model 'TexturaSuelo'
        db.create_table('anarapp_texturasuelo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='TexturaSuelo', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esRocaMadre', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esPedregoso', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esArenoso', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esArcilloso', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mixto', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['TexturaSuelo'])

        # Adding model 'FloraYacimiento'
        db.create_table('anarapp_florayacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='FloraYacimiento', unique=True, to=orm['anarapp.Yacimiento'])),
            ('flora', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['FloraYacimiento'])

        # Adding model 'FaunaYacimiento'
        db.create_table('anarapp_faunayacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='FaunaYacimiento', unique=True, to=orm['anarapp.Yacimiento'])),
            ('fauna', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['FaunaYacimiento'])

        # Adding model 'HidrologiaYacimiento'
        db.create_table('anarapp_hidrologiayacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='HidrologiaYacimiento', unique=True, to=orm['anarapp.Yacimiento'])),
            ('rio', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('laguna', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('arroyo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('arroyoPerenne', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('manantial', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('manantialIntermitente', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otros', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('nombre', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('distancia', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('observaciones', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['HidrologiaYacimiento'])

        # Adding model 'TipoExposicionYac'
        db.create_table('anarapp_tipoexposicionyac', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='TipoExposicionYac', unique=True, to=orm['anarapp.Yacimiento'])),
            ('expuesto', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('noExpuesto', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('expuestoPeriodicamente', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('observaciones', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['TipoExposicionYac'])

        # Adding model 'ConstitucionYacimiento'
        db.create_table('anarapp_constitucionyacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='ConstitucionYacimiento', unique=True, to=orm['anarapp.Yacimiento'])),
            ('nroPiedras', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('nroPiedrasGrabadas', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('nroPiedrasPintadas', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('nroPiedrasColocadas', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('otros', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['ConstitucionYacimiento'])

        # Adding model 'MaterialYacimiento'
        db.create_table('anarapp_materialyacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='MaterialYacimiento', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esRoca', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esIgnea', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMetamor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esSedimentaria', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tipo', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('esTierra', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esHueso', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCorteza', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esPiel', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otros', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['MaterialYacimiento'])

        # Adding model 'TecnicaParaGeoglifo'
        db.create_table('anarapp_tecnicaparageoglifo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='TecnicaParaGeoglifo', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esGeoflifo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tecnicas', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['TecnicaParaGeoglifo'])

        # Adding model 'TecnicaParaPintura'
        db.create_table('anarapp_tecnicaparapintura', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='TecnicaParaPintura', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esPintura', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('conDedo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fibra', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('soplado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otros', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['TecnicaParaPintura'])

        # Adding model 'TecnicaParaPetroglifo'
        db.create_table('anarapp_tecnicaparapetroglifo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='TecnicaParaPetroglifo', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esPetroglifo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esGrabado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esGrabadoPercusion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esGrabadoPercusionDirecta', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esGrabadoPercusionIndirecta', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAbrasion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAbrasionPiedra', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAbrasionArena', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esConcha', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otros', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['TecnicaParaPetroglifo'])

        # Adding model 'TecnicaParaMicroPetro'
        db.create_table('anarapp_tecnicaparamicropetro', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='TecnicaParaMicroPetro', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esMicro', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esGrabado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esGrabadoPercusion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esGrabadoPercusionDirecta', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esGrabadoPercusionIndirecta', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAbrasion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAbrasionPiedra', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAbrasionArena', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esConcha', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otros', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['TecnicaParaMicroPetro'])

        # Adding model 'TecnicaParaMonumentos'
        db.create_table('anarapp_tecnicaparamonumentos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='TecnicaParaMonumentos', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esMonumento', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMonolito', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esMenhir', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esDolmen', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tecnicas', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('otros', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['TecnicaParaMonumentos'])

        # Adding model 'CaracSurcoPetroglifo'
        db.create_table('anarapp_caracsurcopetroglifo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='CaracSurcoPetroglifo', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esCaracSucorPetro', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('anchoDe', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('anchoA', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('produndidadDe', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('profundidadA', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('esBase', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esBaseRedonda', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esBaseAguda', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esBajoRelieve', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esBajoRelieveLineal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esBajoRelievePlanar', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAltoRelieve', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAltoRelieveLineal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAltoRelievePlanar', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAreaInterlineal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAreaInterlinealPulida', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esAreaInterlinealRebajada', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esGrabadoSuperpuesto', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esGrabadoRebajado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('anarapp', ['CaracSurcoPetroglifo'])

        # Adding model 'CaracSurcoAmoladores'
        db.create_table('anarapp_caracsurcoamoladores', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='CaracSurcoAmoladores', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esCaracSurcoAmoladores', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('largo', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('ancho', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('diametro', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['CaracSurcoAmoladores'])

        # Adding model 'CaracSurcoBateas'
        db.create_table('anarapp_caracsurcobateas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='CaracSurcoBateas', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esCaracSurcoBateas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('largo', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('ancho', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('diametro', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('profundidad', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['CaracSurcoBateas'])

        # Adding model 'CaracSurcoPuntosAcopl'
        db.create_table('anarapp_caracsurcopuntosacopl', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('esCaracSurcPuntosAcopl', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='CaracSurcoPuntosAcopl', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esPunteado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('diametro', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('profundidad', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('otros', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['CaracSurcoPuntosAcopl'])

        # Adding model 'CaracSurcoCupulas'
        db.create_table('anarapp_caracsurcocupulas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('esCaracSurcoCupulas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='CaracSurcoCupulas', unique=True, to=orm['anarapp.Yacimiento'])),
            ('largo', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('ancho', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('diametro', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('profundidad', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('otros', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['CaracSurcoCupulas'])

        # Adding model 'CaracSurcoMortero'
        db.create_table('anarapp_caracsurcomortero', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='CaracSurcoMortero', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esCaracSurcoMortero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('largo', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('ancho', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['CaracSurcoMortero'])

        # Adding model 'CaracDeLaPintura'
        db.create_table('anarapp_caracdelapintura', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='CaracDeLaPintura', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esPinturaRupestre', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esTecnicaDactilar', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esTecnicaFibra', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otros', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('esLineaSencilla', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('anchoDe', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('anchoA', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('esLineaCompuesta', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('anchoDeComp', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('anchoAComp', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('esFiguraRellena', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esImpresionDeManos', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esImpresionDeManosPositivo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esImpresionDeManosNegativo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tienesFigurasSuperpuestas', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('anarapp', ['CaracDeLaPintura'])

        # Adding model 'Colores'
        db.create_table('anarapp_colores', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Colores', to=orm['anarapp.Yacimiento'])),
            ('c', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('m', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('y', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('k', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['Colores'])

        # Adding model 'DescColores'
        db.create_table('anarapp_desccolores', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='ColoresPositiva', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esPositiva', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('posNegro', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('posBlanco', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('posAmarillo', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('posUnRojo', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('posDosRojos', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('posTresRojos', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('esNegativa', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('negNegro', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('negBlanco', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('negAmarillo', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('negUnRojo', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('negDosRojos', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('negTresRojos', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('colorBase', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['DescColores'])

        # Adding model 'CaracMonolitos'
        db.create_table('anarapp_caracmonolitos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='CaracMonolitos', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esCarcaMonolitos', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('esPinturaRupestre', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cantidadConGrabados', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['CaracMonolitos'])

        # Adding model 'CaracMenhires'
        db.create_table('anarapp_caracmenhires', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='CaracMehnires', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esCaracMenhier', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sonPiedrasVerticales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cantidadPiedrasVerticales', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('conPuntosAcoplados', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cantidadConPuntosAcoplados', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ConPetroglifo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cantidadConPetroglifo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('conPinturas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cantidadConPinturas', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('distanciamiento', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['CaracMenhires'])

        # Adding model 'CaracDolmenArt'
        db.create_table('anarapp_caracdolmenart', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='CaracDolmenArt', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esCaracDolmen', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ConPetroglifo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cantidadConPetroglifo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('conPinturas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cantidadConPinturas', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['CaracDolmenArt'])

        # Adding model 'NotasYacimiento'
        db.create_table('anarapp_notasyacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='NotasYacimiento', unique=True, to=orm['anarapp.Yacimiento'])),
            ('notas', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['NotasYacimiento'])

        # Adding model 'EstadoConserYac'
        db.create_table('anarapp_estadoconseryac', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='EstadoConserYac', unique=True, to=orm['anarapp.Yacimiento'])),
            ('enBuenEstado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('estadoModificado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('trasladado', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('trasladadoPa', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('sumergido', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sumergidoPa', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('enterrado', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('enterradoPa', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('perdido', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('perdidoPa', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('destruido', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('destruidoPa', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('crecimientoVeg', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('crecimientoVegPa', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('patina', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('patinaPa', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('erosion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('erosionPa', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('estaDestruido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esPorCausaNatural', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enPorCausaNaturalLigera', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enPorCausaNaturalAguda', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enPorCausaHumana', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enPorCausaHumanaLigera', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enPorCausaHumanaAguda', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('especificar', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('destruccionPotencial', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('anarapp', ['EstadoConserYac'])

        # Adding model 'CausasDestruccionYac'
        db.create_table('anarapp_causasdestruccionyac', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='CausasDestruccionYac', unique=True, to=orm['anarapp.Yacimiento'])),
            ('porAsentamientoHumand', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porObraCortoPlazo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porObraMedianoPlazo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porObraLargoPlazo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porNivelacion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porExtraccionFamiliar', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porExtraccionMayor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porVandalismo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porErosion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porErosionParModerada', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porErosionParSevera', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porErosionExtModerada', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porErosionExtSevera', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otros', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['CausasDestruccionYac'])

        # Adding model 'IntensidadDestruccionYac'
        db.create_table('anarapp_intensidaddestruccionyac', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='IntensidadDestruccionYac', unique=True, to=orm['anarapp.Yacimiento'])),
            ('observaciones', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('esDeTiempo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esInmediato', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unAno', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dosAno', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tresAno', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cuatroAno', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cincoAno', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mas', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['IntensidadDestruccionYac'])

        # Adding model 'ConsiderTemp'
        db.create_table('anarapp_considertemp', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='ConsiderTemp', unique=True, to=orm['anarapp.Yacimiento'])),
            ('cincoAno', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otros', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['ConsiderTemp'])

        # Adding model 'CronologiaTentativa'
        db.create_table('anarapp_cronologiatentativa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='CronologiaTentativa', to=orm['anarapp.Yacimiento'])),
            ('esCrono1', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCrono2', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCrono3', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCrono4', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCrono5', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCrono6', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esCrono7', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('autor', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('fecha', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('institucion', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('pais', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('direccion', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('telefono', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('mail', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('tecnica', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('bibliografia', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('twitter', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('facebook', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['CronologiaTentativa'])

        # Adding model 'ManifestacionesAsociadas'
        db.create_table('anarapp_manifestacionesasociadas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='ManifestacionesAsociadas', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esLitica', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionLitica', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('esCeramica', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionCeramica', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('esOseo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionOseo', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('esConcha', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionConcha', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('esCarbon', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionCarbon', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('esMito', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionMito', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('esCementerio', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionCementerio', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('esMonticulo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionMonticulo', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('otros', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['ManifestacionesAsociadas'])

        # Adding model 'ManifestacionesLitica'
        db.create_table('anarapp_manifestacioneslitica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='ManifestacionesLitica', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esLitica', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionLitica', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['ManifestacionesLitica'])

        # Adding model 'ManifestacionesCeramica'
        db.create_table('anarapp_manifestacionesceramica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='ManifestacionesCeramica', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esCeramica', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionCeramica', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['ManifestacionesCeramica'])

        # Adding model 'ManifestacionesOseo'
        db.create_table('anarapp_manifestacionesoseo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='ManifestacionesOseo', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esOseo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionOseo', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['ManifestacionesOseo'])

        # Adding model 'ManifestacionesConcha'
        db.create_table('anarapp_manifestacionesconcha', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='ManifestacionesConcha', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esConcha', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionConcha', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['ManifestacionesConcha'])

        # Adding model 'ManifestacionesCarbon'
        db.create_table('anarapp_manifestacionescarbon', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='ManifestacionesCarbon', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esCarbon', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionCarbon', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['ManifestacionesCarbon'])

        # Adding model 'ManifestacionesMito'
        db.create_table('anarapp_manifestacionesmito', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='ManifestacionesMito', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esMito', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionMito', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['ManifestacionesMito'])

        # Adding model 'ManifestacionesCementerio'
        db.create_table('anarapp_manifestacionescementerio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='ManifestacionesCementerio', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esCementerio', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionCementerio', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['ManifestacionesCementerio'])

        # Adding model 'ManifestacionesMonticulo'
        db.create_table('anarapp_manifestacionesmonticulo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='ManifestacionesMonticulo', unique=True, to=orm['anarapp.Yacimiento'])),
            ('esMonticulo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcionMonticulo', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['ManifestacionesMonticulo'])

        # Adding model 'ManifestacionesOtros'
        db.create_table('anarapp_manifestacionesotros', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='ManifestacionesOtros', unique=True, to=orm['anarapp.Yacimiento'])),
            ('otros', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['ManifestacionesOtros'])

        # Adding model 'Piedra'
        db.create_table('anarapp_piedra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Yacimiento', to=orm['anarapp.Yacimiento'])),
            ('codigo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('nombre', self.gf('anarapp.models.CharField')(max_length=65000)),
        ))
        db.send_create_signal('anarapp', ['Piedra'])

        # Adding model 'FotografiaPiedra'
        db.create_table('anarapp_fotografiapiedra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(related_name='FotografiaPiedra', to=orm['anarapp.Piedra'])),
            ('aerea', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('noEsAerea', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('satelital', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fecha', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('archivo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['FotografiaPiedra'])

        # Adding model 'Piedra2'
        db.create_table('anarapp_piedra2', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Piedra2', to=orm['anarapp.Piedra'])),
            ('nombreFiguras', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='EstadoPied', null=True, to=orm['anarapp.Estado'])),
            ('numeroCaras', self.gf('django.db.models.fields.IntegerField')()),
            ('numeroCarasTrajabadas', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['Piedra2'])

        # Adding model 'DimensionPiedra'
        db.create_table('anarapp_dimensionpiedra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(related_name='DimensionPiedra', to=orm['anarapp.Piedra'])),
            ('dimensiones', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('alto', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('largo', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('ancho', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['DimensionPiedra'])

        # Adding model 'CaraTrabajada'
        db.create_table('anarapp_caratrabajada', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(related_name='CaraTrabajada', to=orm['anarapp.Piedra'])),
            ('numero', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('orientacion', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['CaraTrabajada'])

        # Adding model 'UbicacionCaras'
        db.create_table('anarapp_ubicacioncaras', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.OneToOneField')(related_name='UbicacionCaras', unique=True, to=orm['anarapp.Piedra'])),
            ('todaLaCaverna', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('areasEspecificas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('salaPrincipal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otraSala', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('lagoInterior', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('claraboya', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('principalMouth', self.gf('anarapp.models.CharField')(max_length=65000, null=True, blank=True)),
            ('luminosity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('heights', self.gf('anarapp.models.CharField')(max_length=65000, null=True, blank=True)),
            ('requiereAndamiaje', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('anarapp', ['UbicacionCaras'])

        # Adding model 'FigurasPorTipo'
        db.create_table('anarapp_figurasportipo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(related_name='FigurasPorTipo', to=orm['anarapp.Piedra'])),
            ('numero', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('tipoFigura', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('esCantidadInexacta', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('descripcion', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['FigurasPorTipo'])

        # Adding model 'EsquemaPorCara'
        db.create_table('anarapp_esquemaporcara', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(related_name='EsquemaPorCara', to=orm['anarapp.Piedra'])),
            ('numero', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('textoCara', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('posicion', self.gf('anarapp.models.CharField')(max_length=65000)),
        ))
        db.send_create_signal('anarapp', ['EsquemaPorCara'])

        # Adding model 'ConexionFiguras'
        db.create_table('anarapp_conexionfiguras', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.OneToOneField')(related_name='ConexionFiguras', unique=True, to=orm['anarapp.Piedra'])),
            ('conexionFiguras', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['ConexionFiguras'])

        # Adding model 'Manifestaciones'
        db.create_table('anarapp_manifestaciones', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Manifestaciones', to=orm['anarapp.Piedra'])),
            ('tienePetroglifos', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tieneRupestres', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tieneAmoladore', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tienePuntosAc', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tieneCupula', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hasMitos', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('hasOtros', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['Manifestaciones'])

        # Adding model 'TratFoto'
        db.create_table('anarapp_tratfoto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('limpiezaCon', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('rellenoSurcos', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('tratamientoDigital', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('programaVersion', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('otrosTratamientos', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['TratFoto'])

        # Adding model 'TratFotoPiedra'
        db.create_table('anarapp_tratfotopiedra', (
            ('tratfoto_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.TratFoto'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.OneToOneField')(related_name='TratFotoPiedra', unique=True, to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['TratFotoPiedra'])

        # Adding model 'Foto'
        db.create_table('anarapp_foto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('esfoto', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('negativo', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('tipoFotoA', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tipoFotoNA', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tipoFotoS', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fecha', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('fotografo', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('institucion', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('numReferencia', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('numRollo', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('numFoto', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('numMarcaNegativo', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('esDeAnar', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('numCopiaAnarFoto', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['Foto'])

        # Adding model 'FotoPiedra'
        db.create_table('anarapp_fotopiedra', (
            ('foto_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Foto'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(related_name='FotoPiedra', to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['FotoPiedra'])

        # Adding model 'RepGrafPiedra'
        db.create_table('anarapp_repgrafpiedra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(related_name='RepGrafPiedra', to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['RepGrafPiedra'])

        # Adding model 'EscNatPiedra'
        db.create_table('anarapp_escnatpiedra', (
            ('repgrafpiedra_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.RepGrafPiedra'], unique=True, primary_key=True)),
            ('esEscNatPiedra', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tipoReproduccione', self.gf('django.db.models.fields.IntegerField')()),
            ('numPiezasP', self.gf('django.db.models.fields.IntegerField')()),
            ('institutoP', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('personaP', self.gf('anarapp.models.CharField')(max_length=65000)),
        ))
        db.send_create_signal('anarapp', ['EscNatPiedra'])

        # Adding model 'EscRedPiedra'
        db.create_table('anarapp_escredpiedra', (
            ('repgrafpiedra_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.RepGrafPiedra'], unique=True, primary_key=True)),
            ('esEscNatPiedra', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tipoReproduccion', self.gf('django.db.models.fields.IntegerField')()),
            ('numPiezasP', self.gf('django.db.models.fields.IntegerField')()),
            ('institutoP', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('personaP', self.gf('anarapp.models.CharField')(max_length=65000)),
        ))
        db.send_create_signal('anarapp', ['EscRedPiedra'])

        # Adding model 'Bibliografia'
        db.create_table('anarapp_bibliografia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['Bibliografia'])

        # Adding model 'BibYacimiento'
        db.create_table('anarapp_bibyacimiento', (
            ('bibliografia_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Bibliografia'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='BibYacimiento', to=orm['anarapp.Yacimiento'])),
            ('esBibliografia', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('conPdf', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tienePDF', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tienePDF1', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tienePDF2', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('conWord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tieneWord', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tieneWord1', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('codigo', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('titulo', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('autor', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('ano', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('institucion', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('conDibujo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('archivo', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('archivo1', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('archivo2', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('archivo3', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('archivo4', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('esFotografia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tieneFotografia', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tieneFotografia1', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tieneFotografia2', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tieneFotografia3', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tieneFotografia4', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('escolor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esBlancoYNegro', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esDiapositiva', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esPapel', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esDigital', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esNegativo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tieneMapa', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tieneMapa1', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tieneMapa2', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tieneMapa3', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tieneMapa4', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tipoMapa', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['BibYacimiento'])

        # Adding model 'BibPiedra'
        db.create_table('anarapp_bibpiedra', (
            ('bibliografia_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Bibliografia'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(related_name='BibPiedra', to=orm['anarapp.Piedra'])),
            ('esbilbio', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tienePDF', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pdfarchivo', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('pdfarchivo1', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('pdfarchivo2', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tieneWord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('wordarchivo', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('wordarchivo1', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('codigo', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('titulo', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('autor', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('ano', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('institucion', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('conDibujo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('archivo', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('archivo1', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('archivo2', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('archivo3', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('archivo4', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('esFotografia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tieneFotografia', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tieneFotografia1', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tieneFotografia2', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tieneFotografia3', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tieneFotografia4', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('escolor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esBlancoYNegro', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esDiapositiva', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esPapel', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esDigital', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esNegativo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tieneMapa', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tieneMapa1', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tieneMapa2', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tieneMapa3', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tieneMapa4', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('tipoMapa', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['BibPiedra'])

        # Adding model 'MatAudioVisual'
        db.create_table('anarapp_mataudiovisual', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['MatAudioVisual'])

        # Adding model 'MatAVYacimiento'
        db.create_table('anarapp_matavyacimiento', (
            ('mataudiovisual_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MatAudioVisual'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='MatAVYacimiento', to=orm['anarapp.Yacimiento'])),
            ('ismatavy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('format', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('archive', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['MatAVYacimiento'])

        # Adding model 'MatAVPiedra'
        db.create_table('anarapp_matavpiedra', (
            ('mataudiovisual_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MatAudioVisual'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(related_name='MatAVPiedra', to=orm['anarapp.Piedra'])),
            ('ismatavy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('format', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('archive', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['MatAVPiedra'])

        # Adding model 'Video'
        db.create_table('anarapp_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['Video'])

        # Adding model 'VideoYacimiento'
        db.create_table('anarapp_videoyacimiento', (
            ('video_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Video'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='VideoYacimiento', to=orm['anarapp.Yacimiento'])),
            ('isvidyac', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('anioy', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('formatoy', self.gf('anarapp.models.CharField')(max_length=65000, null=True, blank=True)),
            ('tituloy', self.gf('anarapp.models.CharField')(max_length=65000, null=True, blank=True)),
            ('autory', self.gf('anarapp.models.CharField')(max_length=65000, null=True, blank=True)),
            ('instituciony', self.gf('anarapp.models.CharField')(max_length=65000, null=True, blank=True)),
            ('numReferenciay', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('isFromAnary', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('numCopiayac', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('archivoy', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['VideoYacimiento'])

        # Adding model 'VideoPiedra'
        db.create_table('anarapp_videopiedra', (
            ('video_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Video'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(related_name='VideoPiedra', to=orm['anarapp.Piedra'])),
            ('isvidyac', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('anioy', self.gf('django.db.models.fields.IntegerField')()),
            ('formatoy', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('tituloy', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('autory', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('instituciony', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('numReferenciay', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('isFromAnary', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('numCopiaPiedra', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('archivoy', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['VideoPiedra'])

        # Adding model 'Pelicula'
        db.create_table('anarapp_pelicula', (
            ('video_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Video'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['Pelicula'])

        # Adding model 'PeliYacimiento'
        db.create_table('anarapp_peliyacimiento', (
            ('pelicula_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Pelicula'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='PeliYacimiento', to=orm['anarapp.Yacimiento'])),
            ('isvidyac', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('anioy', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('formatoy', self.gf('anarapp.models.CharField')(max_length=65000, null=True, blank=True)),
            ('tituloy', self.gf('anarapp.models.CharField')(max_length=65000, null=True, blank=True)),
            ('autory', self.gf('anarapp.models.CharField')(max_length=65000, null=True, blank=True)),
            ('instituciony', self.gf('anarapp.models.CharField')(max_length=65000, null=True, blank=True)),
            ('numReferenciay', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('isFromAnary', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('numCopiayac', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('archivoy', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['PeliYacimiento'])

        # Adding model 'PeliculaPiedra'
        db.create_table('anarapp_peliculapiedra', (
            ('pelicula_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Pelicula'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(related_name='PeliculaPiedra', to=orm['anarapp.Piedra'])),
            ('isvidyac', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('formatoy', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('tituloy', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('autory', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('instituciony', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('numReferenciay', self.gf('django.db.models.fields.IntegerField')()),
            ('isFromAnary', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('numCopiaPiedra', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('archivoy', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['PeliculaPiedra'])

        # Adding model 'PaginaWeb'
        db.create_table('anarapp_paginaweb', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['PaginaWeb'])

        # Adding model 'PaginaWebYac'
        db.create_table('anarapp_paginawebyac', (
            ('paginaweb_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.PaginaWeb'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='PaginaWebYac', to=orm['anarapp.Yacimiento'])),
            ('tieneWb', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('direccionURLy', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('anarapp', ['PaginaWebYac'])

        # Adding model 'PaginaWebPiedra'
        db.create_table('anarapp_paginawebpiedra', (
            ('paginaweb_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.PaginaWeb'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(related_name='PaginaWebPiedra', to=orm['anarapp.Piedra'])),
            ('tieneWb', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('direccionURLP', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('anarapp', ['PaginaWebPiedra'])

        # Adding model 'Multimedia'
        db.create_table('anarapp_multimedia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['Multimedia'])

        # Adding model 'MultimediaYac'
        db.create_table('anarapp_multimediayac', (
            ('multimedia_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Multimedia'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='MultimediaYac', to=orm['anarapp.Yacimiento'])),
            ('ismult', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tecnicaY', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('archivoY', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['MultimediaYac'])

        # Adding model 'MultimediaPiedra'
        db.create_table('anarapp_multimediapiedra', (
            ('multimedia_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Multimedia'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(related_name='MultimediaPiedra', to=orm['anarapp.Piedra'])),
            ('ismult', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tecnicaP', self.gf('anarapp.models.CharField')(max_length=65000, null=True, blank=True)),
            ('archivoP', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['MultimediaPiedra'])

        # Adding model 'ObtencionInfo'
        db.create_table('anarapp_obtencioninfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['ObtencionInfo'])

        # Adding model 'ObtInfoYac'
        db.create_table('anarapp_obtinfoyac', (
            ('obtencioninfo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.ObtencionInfo'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ObtInfoYac', to=orm['anarapp.Yacimiento'])),
            ('isinfo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('prospeccionY', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comunicacionY', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nombreY', self.gf('anarapp.models.CharField')(max_length=65000)),
            ('direccionY', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('telefonoY', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('telefonoCelY', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('mailY', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('paginaWebY', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('twitterY', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('nombreFacebookY', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('blogY', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('fechaY', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('verificadoY', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('anarapp', ['ObtInfoYac'])

        # Adding model 'ObtInfoPiedra'
        db.create_table('anarapp_obtinfopiedra', (
            ('obtencioninfo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.ObtencionInfo'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ObtInfoPiedra', to=orm['anarapp.Piedra'])),
            ('isinfo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('prospeccionP', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comunicacionP', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nombreP', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('direccionP', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('telefonoP', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('telefonoCelP', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('mailP', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('paginaWebP', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('twitterP', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('nombreFacebookP', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('blogP', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('fechaP', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('verificadoP', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('anarapp', ['ObtInfoPiedra'])

        # Adding model 'OtrosValores'
        db.create_table('anarapp_otrosvalores', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['OtrosValores'])

        # Adding model 'OtrosValYac'
        db.create_table('anarapp_otrosvalyac', (
            ('otrosvalores_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.OtrosValores'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='OtrosValYac', to=orm['anarapp.Yacimiento'])),
            ('texto', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['OtrosValYac'])

        # Adding model 'OtrosValPiedra'
        db.create_table('anarapp_otrosvalpiedra', (
            ('otrosvalores_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.OtrosValores'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(related_name='OtrosValPiedra', to=orm['anarapp.Piedra'])),
            ('texto', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['OtrosValPiedra'])

        # Adding model 'Observaciones'
        db.create_table('anarapp_observaciones', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['Observaciones'])

        # Adding model 'ObservacionesYac'
        db.create_table('anarapp_observacionesyac', (
            ('observaciones_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Observaciones'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ObservacionesYac', to=orm['anarapp.Yacimiento'])),
            ('textoY', self.gf('anarapp.models.CharField')(max_length=65000)),
        ))
        db.send_create_signal('anarapp', ['ObservacionesYac'])

        # Adding model 'ObservacPiedra'
        db.create_table('anarapp_observacpiedra', (
            ('observaciones_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Observaciones'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ObservacPiedra', to=orm['anarapp.Piedra'])),
            ('textoP', self.gf('anarapp.models.CharField')(max_length=65000)),
        ))
        db.send_create_signal('anarapp', ['ObservacPiedra'])

        # Adding model 'LlenadoPor'
        db.create_table('anarapp_llenadopor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['LlenadoPor'])

        # Adding model 'LlenadoYac'
        db.create_table('anarapp_llenadoyac', (
            ('llenadopor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.LlenadoPor'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='LlenadoYac', to=orm['anarapp.Yacimiento'])),
            ('nombreY', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('fechaY', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['LlenadoYac'])

        # Adding model 'LlenadoPiedra'
        db.create_table('anarapp_llenadopiedra', (
            ('llenadopor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.LlenadoPor'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(related_name='LlenadoPiedra', to=orm['anarapp.Piedra'])),
            ('nombreP', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('fechaP', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['LlenadoPiedra'])

        # Adding model 'SupervisadoPor'
        db.create_table('anarapp_supervisadopor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['SupervisadoPor'])

        # Adding model 'SupervisadoYac'
        db.create_table('anarapp_supervisadoyac', (
            ('supervisadopor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.SupervisadoPor'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='SupervisadoYac', to=orm['anarapp.Yacimiento'])),
            ('nombreY', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('fechaY', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['SupervisadoYac'])

        # Adding model 'SupervisadoPiedra'
        db.create_table('anarapp_supervisadopiedra', (
            ('supervisadopor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.SupervisadoPor'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(related_name='SupervisadoPiedra', to=orm['anarapp.Piedra'])),
            ('nombreP', self.gf('anarapp.models.CharField')(max_length=65000, blank=True)),
            ('fechaP', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['SupervisadoPiedra'])


    def backwards(self, orm):
        # Deleting model 'Estado'
        db.delete_table('anarapp_estado')

        # Deleting model 'Municipio'
        db.delete_table('anarapp_municipio')

        # Deleting model 'Yacimiento'
        db.delete_table('anarapp_yacimiento')

        # Deleting model 'LocalidadYacimiento'
        db.delete_table('anarapp_localidadyacimiento')

        # Deleting model 'UsoActSuelo'
        db.delete_table('anarapp_usoactsuelo')

        # Deleting model 'TenenciaDeTierra'
        db.delete_table('anarapp_tenenciadetierra')

        # Deleting model 'Indicaciones'
        db.delete_table('anarapp_indicaciones')

        # Deleting model 'Croquis'
        db.delete_table('anarapp_croquis')

        # Deleting model 'Plano'
        db.delete_table('anarapp_plano')

        # Deleting model 'Coordenadas'
        db.delete_table('anarapp_coordenadas')

        # Deleting model 'Datum'
        db.delete_table('anarapp_datum')

        # Deleting model 'Altitud'
        db.delete_table('anarapp_altitud')

        # Deleting model 'FotografiaYac'
        db.delete_table('anarapp_fotografiayac')

        # Deleting model 'TipoYacimiento'
        db.delete_table('anarapp_tipoyacimiento')

        # Deleting model 'ManifestacionYacimiento'
        db.delete_table('anarapp_manifestacionyacimiento')

        # Deleting model 'UbicacionYacimiento'
        db.delete_table('anarapp_ubicacionyacimiento')

        # Deleting model 'OrientacionYacimiento'
        db.delete_table('anarapp_orientacionyacimiento')

        # Deleting model 'TexturaSuelo'
        db.delete_table('anarapp_texturasuelo')

        # Deleting model 'FloraYacimiento'
        db.delete_table('anarapp_florayacimiento')

        # Deleting model 'FaunaYacimiento'
        db.delete_table('anarapp_faunayacimiento')

        # Deleting model 'HidrologiaYacimiento'
        db.delete_table('anarapp_hidrologiayacimiento')

        # Deleting model 'TipoExposicionYac'
        db.delete_table('anarapp_tipoexposicionyac')

        # Deleting model 'ConstitucionYacimiento'
        db.delete_table('anarapp_constitucionyacimiento')

        # Deleting model 'MaterialYacimiento'
        db.delete_table('anarapp_materialyacimiento')

        # Deleting model 'TecnicaParaGeoglifo'
        db.delete_table('anarapp_tecnicaparageoglifo')

        # Deleting model 'TecnicaParaPintura'
        db.delete_table('anarapp_tecnicaparapintura')

        # Deleting model 'TecnicaParaPetroglifo'
        db.delete_table('anarapp_tecnicaparapetroglifo')

        # Deleting model 'TecnicaParaMicroPetro'
        db.delete_table('anarapp_tecnicaparamicropetro')

        # Deleting model 'TecnicaParaMonumentos'
        db.delete_table('anarapp_tecnicaparamonumentos')

        # Deleting model 'CaracSurcoPetroglifo'
        db.delete_table('anarapp_caracsurcopetroglifo')

        # Deleting model 'CaracSurcoAmoladores'
        db.delete_table('anarapp_caracsurcoamoladores')

        # Deleting model 'CaracSurcoBateas'
        db.delete_table('anarapp_caracsurcobateas')

        # Deleting model 'CaracSurcoPuntosAcopl'
        db.delete_table('anarapp_caracsurcopuntosacopl')

        # Deleting model 'CaracSurcoCupulas'
        db.delete_table('anarapp_caracsurcocupulas')

        # Deleting model 'CaracSurcoMortero'
        db.delete_table('anarapp_caracsurcomortero')

        # Deleting model 'CaracDeLaPintura'
        db.delete_table('anarapp_caracdelapintura')

        # Deleting model 'Colores'
        db.delete_table('anarapp_colores')

        # Deleting model 'DescColores'
        db.delete_table('anarapp_desccolores')

        # Deleting model 'CaracMonolitos'
        db.delete_table('anarapp_caracmonolitos')

        # Deleting model 'CaracMenhires'
        db.delete_table('anarapp_caracmenhires')

        # Deleting model 'CaracDolmenArt'
        db.delete_table('anarapp_caracdolmenart')

        # Deleting model 'NotasYacimiento'
        db.delete_table('anarapp_notasyacimiento')

        # Deleting model 'EstadoConserYac'
        db.delete_table('anarapp_estadoconseryac')

        # Deleting model 'CausasDestruccionYac'
        db.delete_table('anarapp_causasdestruccionyac')

        # Deleting model 'IntensidadDestruccionYac'
        db.delete_table('anarapp_intensidaddestruccionyac')

        # Deleting model 'ConsiderTemp'
        db.delete_table('anarapp_considertemp')

        # Deleting model 'CronologiaTentativa'
        db.delete_table('anarapp_cronologiatentativa')

        # Deleting model 'ManifestacionesAsociadas'
        db.delete_table('anarapp_manifestacionesasociadas')

        # Deleting model 'ManifestacionesLitica'
        db.delete_table('anarapp_manifestacioneslitica')

        # Deleting model 'ManifestacionesCeramica'
        db.delete_table('anarapp_manifestacionesceramica')

        # Deleting model 'ManifestacionesOseo'
        db.delete_table('anarapp_manifestacionesoseo')

        # Deleting model 'ManifestacionesConcha'
        db.delete_table('anarapp_manifestacionesconcha')

        # Deleting model 'ManifestacionesCarbon'
        db.delete_table('anarapp_manifestacionescarbon')

        # Deleting model 'ManifestacionesMito'
        db.delete_table('anarapp_manifestacionesmito')

        # Deleting model 'ManifestacionesCementerio'
        db.delete_table('anarapp_manifestacionescementerio')

        # Deleting model 'ManifestacionesMonticulo'
        db.delete_table('anarapp_manifestacionesmonticulo')

        # Deleting model 'ManifestacionesOtros'
        db.delete_table('anarapp_manifestacionesotros')

        # Deleting model 'Piedra'
        db.delete_table('anarapp_piedra')

        # Deleting model 'FotografiaPiedra'
        db.delete_table('anarapp_fotografiapiedra')

        # Deleting model 'Piedra2'
        db.delete_table('anarapp_piedra2')

        # Deleting model 'DimensionPiedra'
        db.delete_table('anarapp_dimensionpiedra')

        # Deleting model 'CaraTrabajada'
        db.delete_table('anarapp_caratrabajada')

        # Deleting model 'UbicacionCaras'
        db.delete_table('anarapp_ubicacioncaras')

        # Deleting model 'FigurasPorTipo'
        db.delete_table('anarapp_figurasportipo')

        # Deleting model 'EsquemaPorCara'
        db.delete_table('anarapp_esquemaporcara')

        # Deleting model 'ConexionFiguras'
        db.delete_table('anarapp_conexionfiguras')

        # Deleting model 'Manifestaciones'
        db.delete_table('anarapp_manifestaciones')

        # Deleting model 'TratFoto'
        db.delete_table('anarapp_tratfoto')

        # Deleting model 'TratFotoPiedra'
        db.delete_table('anarapp_tratfotopiedra')

        # Deleting model 'Foto'
        db.delete_table('anarapp_foto')

        # Deleting model 'FotoPiedra'
        db.delete_table('anarapp_fotopiedra')

        # Deleting model 'RepGrafPiedra'
        db.delete_table('anarapp_repgrafpiedra')

        # Deleting model 'EscNatPiedra'
        db.delete_table('anarapp_escnatpiedra')

        # Deleting model 'EscRedPiedra'
        db.delete_table('anarapp_escredpiedra')

        # Deleting model 'Bibliografia'
        db.delete_table('anarapp_bibliografia')

        # Deleting model 'BibYacimiento'
        db.delete_table('anarapp_bibyacimiento')

        # Deleting model 'BibPiedra'
        db.delete_table('anarapp_bibpiedra')

        # Deleting model 'MatAudioVisual'
        db.delete_table('anarapp_mataudiovisual')

        # Deleting model 'MatAVYacimiento'
        db.delete_table('anarapp_matavyacimiento')

        # Deleting model 'MatAVPiedra'
        db.delete_table('anarapp_matavpiedra')

        # Deleting model 'Video'
        db.delete_table('anarapp_video')

        # Deleting model 'VideoYacimiento'
        db.delete_table('anarapp_videoyacimiento')

        # Deleting model 'VideoPiedra'
        db.delete_table('anarapp_videopiedra')

        # Deleting model 'Pelicula'
        db.delete_table('anarapp_pelicula')

        # Deleting model 'PeliYacimiento'
        db.delete_table('anarapp_peliyacimiento')

        # Deleting model 'PeliculaPiedra'
        db.delete_table('anarapp_peliculapiedra')

        # Deleting model 'PaginaWeb'
        db.delete_table('anarapp_paginaweb')

        # Deleting model 'PaginaWebYac'
        db.delete_table('anarapp_paginawebyac')

        # Deleting model 'PaginaWebPiedra'
        db.delete_table('anarapp_paginawebpiedra')

        # Deleting model 'Multimedia'
        db.delete_table('anarapp_multimedia')

        # Deleting model 'MultimediaYac'
        db.delete_table('anarapp_multimediayac')

        # Deleting model 'MultimediaPiedra'
        db.delete_table('anarapp_multimediapiedra')

        # Deleting model 'ObtencionInfo'
        db.delete_table('anarapp_obtencioninfo')

        # Deleting model 'ObtInfoYac'
        db.delete_table('anarapp_obtinfoyac')

        # Deleting model 'ObtInfoPiedra'
        db.delete_table('anarapp_obtinfopiedra')

        # Deleting model 'OtrosValores'
        db.delete_table('anarapp_otrosvalores')

        # Deleting model 'OtrosValYac'
        db.delete_table('anarapp_otrosvalyac')

        # Deleting model 'OtrosValPiedra'
        db.delete_table('anarapp_otrosvalpiedra')

        # Deleting model 'Observaciones'
        db.delete_table('anarapp_observaciones')

        # Deleting model 'ObservacionesYac'
        db.delete_table('anarapp_observacionesyac')

        # Deleting model 'ObservacPiedra'
        db.delete_table('anarapp_observacpiedra')

        # Deleting model 'LlenadoPor'
        db.delete_table('anarapp_llenadopor')

        # Deleting model 'LlenadoYac'
        db.delete_table('anarapp_llenadoyac')

        # Deleting model 'LlenadoPiedra'
        db.delete_table('anarapp_llenadopiedra')

        # Deleting model 'SupervisadoPor'
        db.delete_table('anarapp_supervisadopor')

        # Deleting model 'SupervisadoYac'
        db.delete_table('anarapp_supervisadoyac')

        # Deleting model 'SupervisadoPiedra'
        db.delete_table('anarapp_supervisadopiedra')


    models = {
        'anarapp.altitud': {
            'Meta': {'object_name': 'Altitud'},
            'altura': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'desarrollo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'desnivel': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'superficie': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'texto': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Altitud'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.bibliografia': {
            'Meta': {'object_name': 'Bibliografia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'anarapp.bibpiedra': {
            'Meta': {'object_name': 'BibPiedra', '_ormbases': ['anarapp.Bibliografia']},
            'ano': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'archivo1': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'archivo2': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'archivo3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'archivo4': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'autor': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'bibliografia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Bibliografia']", 'unique': 'True', 'primary_key': 'True'}),
            'codigo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'conDibujo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esBlancoYNegro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esDiapositiva': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esDigital': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esFotografia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esNegativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPapel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esbilbio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'escolor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'institucion': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'pdfarchivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pdfarchivo1': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pdfarchivo2': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'BibPiedra'", 'to': "orm['anarapp.Piedra']"}),
            'tieneFotografia': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tieneFotografia1': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tieneFotografia2': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tieneFotografia3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tieneFotografia4': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tieneMapa': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tieneMapa1': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tieneMapa2': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tieneMapa3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tieneMapa4': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tienePDF': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tieneWord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tipoMapa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'titulo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'wordarchivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'wordarchivo1': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'anarapp.bibyacimiento': {
            'Meta': {'object_name': 'BibYacimiento', '_ormbases': ['anarapp.Bibliografia']},
            'ano': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'archivo1': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'archivo2': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'archivo3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'archivo4': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'autor': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'bibliografia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Bibliografia']", 'unique': 'True', 'primary_key': 'True'}),
            'codigo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'conDibujo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'conPdf': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'conWord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esBibliografia': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'esBlancoYNegro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esDiapositiva': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esDigital': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esFotografia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esNegativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPapel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'escolor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'institucion': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'tieneFotografia': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tieneFotografia1': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tieneFotografia2': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tieneFotografia3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tieneFotografia4': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tieneMapa': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tieneMapa1': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tieneMapa2': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tieneMapa3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tieneMapa4': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tienePDF': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tienePDF1': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tienePDF2': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tieneWord': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tieneWord1': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tipoMapa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'titulo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'BibYacimiento'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracdelapintura': {
            'Meta': {'object_name': 'CaracDeLaPintura'},
            'anchoA': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'anchoAComp': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'anchoDe': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'anchoDeComp': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esFiguraRellena': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esImpresionDeManos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esImpresionDeManosNegativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esImpresionDeManosPositivo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esLineaCompuesta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esLineaSencilla': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPinturaRupestre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esTecnicaDactilar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esTecnicaFibra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'tienesFigurasSuperpuestas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracDeLaPintura'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracdolmenart': {
            'ConPetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Meta': {'object_name': 'CaracDolmenArt'},
            'cantidadConPetroglifo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cantidadConPinturas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'conPinturas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCaracDolmen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracDolmenArt'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracmenhires': {
            'ConPetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Meta': {'object_name': 'CaracMenhires'},
            'cantidadConPetroglifo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cantidadConPinturas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cantidadConPuntosAcoplados': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cantidadPiedrasVerticales': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'conPinturas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'conPuntosAcoplados': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'distanciamiento': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'esCaracMenhier': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sonPiedrasVerticales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracMehnires'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracmonolitos': {
            'Meta': {'object_name': 'CaracMonolitos'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cantidadConGrabados': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'esCarcaMonolitos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPinturaRupestre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracMonolitos'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcoamoladores': {
            'Meta': {'object_name': 'CaracSurcoAmoladores'},
            'ancho': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'diametro': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esCaracSurcoAmoladores': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracSurcoAmoladores'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcobateas': {
            'Meta': {'object_name': 'CaracSurcoBateas'},
            'ancho': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'diametro': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esCaracSurcoBateas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'profundidad': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracSurcoBateas'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcocupulas': {
            'Meta': {'object_name': 'CaracSurcoCupulas'},
            'ancho': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'diametro': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esCaracSurcoCupulas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'profundidad': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracSurcoCupulas'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcomortero': {
            'Meta': {'object_name': 'CaracSurcoMortero'},
            'ancho': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esCaracSurcoMortero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracSurcoMortero'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcopetroglifo': {
            'Meta': {'object_name': 'CaracSurcoPetroglifo'},
            'anchoA': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'anchoDe': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esAltoRelieve': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAltoRelieveLineal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAltoRelievePlanar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAreaInterlineal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAreaInterlinealPulida': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAreaInterlinealRebajada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esBajoRelieve': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esBajoRelieveLineal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esBajoRelievePlanar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esBase': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esBaseAguda': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esBaseRedonda': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCaracSucorPetro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoRebajado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoSuperpuesto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'produndidadDe': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'profundidadA': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracSurcoPetroglifo'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcopuntosacopl': {
            'Meta': {'object_name': 'CaracSurcoPuntosAcopl'},
            'diametro': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esCaracSurcPuntosAcopl': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPunteado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'profundidad': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracSurcoPuntosAcopl'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caratrabajada': {
            'Meta': {'object_name': 'CaraTrabajada'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'orientacion': ('django.db.models.fields.IntegerField', [], {}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'CaraTrabajada'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.causasdestruccionyac': {
            'Meta': {'object_name': 'CausasDestruccionYac'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'porAsentamientoHumand': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porErosion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porErosionExtModerada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porErosionExtSevera': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porErosionParModerada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porErosionParSevera': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porExtraccionFamiliar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porExtraccionMayor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porNivelacion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porObraCortoPlazo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porObraLargoPlazo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porObraMedianoPlazo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porVandalismo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CausasDestruccionYac'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.colores': {
            'Meta': {'object_name': 'Colores'},
            'c': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'k': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'm': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'y': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Colores'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.conexionfiguras': {
            'Meta': {'object_name': 'ConexionFiguras'},
            'conexionFiguras': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'ConexionFiguras'", 'unique': 'True', 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.considertemp': {
            'Meta': {'object_name': 'ConsiderTemp'},
            'cincoAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'ConsiderTemp'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.constitucionyacimiento': {
            'Meta': {'object_name': 'ConstitucionYacimiento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nroPiedras': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nroPiedrasColocadas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nroPiedrasGrabadas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nroPiedrasPintadas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'ConstitucionYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.coordenadas': {
            'Meta': {'object_name': 'Coordenadas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'longitud': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'utmAdicional': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Coordenadas'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.cronologiatentativa': {
            'Meta': {'object_name': 'CronologiaTentativa'},
            'autor': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'bibliografia': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'direccion': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esCrono1': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono3': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono4': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono5': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono6': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono7': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'facebook': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'fecha': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'mail': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'pais': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'tecnica': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'telefono': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'twitter': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'CronologiaTentativa'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.croquis': {
            'Meta': {'object_name': 'Croquis'},
            'archivo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Croquis'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.datum': {
            'Meta': {'object_name': 'Datum'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipoDatum': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Datum'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.desccolores': {
            'Meta': {'object_name': 'DescColores'},
            'colorBase': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esNegativa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPositiva': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'negAmarillo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'negBlanco': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'negDosRojos': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'negNegro': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'negTresRojos': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'negUnRojo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'posAmarillo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'posBlanco': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'posDosRojos': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'posNegro': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'posTresRojos': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'posUnRojo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'ColoresPositiva'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.dimensionpiedra': {
            'Meta': {'object_name': 'DimensionPiedra'},
            'alto': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'ancho': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'dimensiones': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'DimensionPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.escnatpiedra': {
            'Meta': {'object_name': 'EscNatPiedra', '_ormbases': ['anarapp.RepGrafPiedra']},
            'esEscNatPiedra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'institutoP': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'numPiezasP': ('django.db.models.fields.IntegerField', [], {}),
            'personaP': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'repgrafpiedra_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.RepGrafPiedra']", 'unique': 'True', 'primary_key': 'True'}),
            'tipoReproduccione': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.escredpiedra': {
            'Meta': {'object_name': 'EscRedPiedra', '_ormbases': ['anarapp.RepGrafPiedra']},
            'esEscNatPiedra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'institutoP': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'numPiezasP': ('django.db.models.fields.IntegerField', [], {}),
            'personaP': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'repgrafpiedra_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.RepGrafPiedra']", 'unique': 'True', 'primary_key': 'True'}),
            'tipoReproduccion': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.esquemaporcara': {
            'Meta': {'object_name': 'EsquemaPorCara'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'EsquemaPorCara'", 'to': "orm['anarapp.Piedra']"}),
            'posicion': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'textoCara': ('anarapp.models.CharField', [], {'max_length': '65000'})
        },
        'anarapp.estado': {
            'Meta': {'object_name': 'Estado'},
            'activo': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('anarapp.models.CharField', [], {'max_length': '65000'})
        },
        'anarapp.estadoconseryac': {
            'Meta': {'object_name': 'EstadoConserYac'},
            'crecimientoVeg': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'crecimientoVegPa': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'destruccionPotencial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'destruido': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'destruidoPa': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'enBuenEstado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enPorCausaHumana': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enPorCausaHumanaAguda': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enPorCausaHumanaLigera': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enPorCausaNaturalAguda': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enPorCausaNaturalLigera': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enterrado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'enterradoPa': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'erosion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'erosionPa': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esPorCausaNatural': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'especificar': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'estaDestruido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estadoModificado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patina': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'patinaPa': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'perdido': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'perdidoPa': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'sumergido': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sumergidoPa': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'trasladado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trasladadoPa': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'EstadoConserYac'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.faunayacimiento': {
            'Meta': {'object_name': 'FaunaYacimiento'},
            'fauna': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'FaunaYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.figurasportipo': {
            'Meta': {'object_name': 'FigurasPorTipo'},
            'cantidad': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'descripcion': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esCantidadInexacta': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'FigurasPorTipo'", 'to': "orm['anarapp.Piedra']"}),
            'tipoFigura': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.florayacimiento': {
            'Meta': {'object_name': 'FloraYacimiento'},
            'flora': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'FloraYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.foto': {
            'Meta': {'object_name': 'Foto'},
            'esDeAnar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esfoto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fotografo': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'negativo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'numCopiaAnarFoto': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'numFoto': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'numMarcaNegativo': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'numReferencia': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'numRollo': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'tipoFotoA': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tipoFotoNA': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tipoFotoS': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'anarapp.fotografiapiedra': {
            'Meta': {'object_name': 'FotografiaPiedra'},
            'aerea': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'archivo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noEsAerea': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'FotografiaPiedra'", 'to': "orm['anarapp.Piedra']"}),
            'satelital': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'anarapp.fotografiayac': {
            'Meta': {'object_name': 'FotografiaYac'},
            'archivo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'esAerea': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esSatelital': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noEsAerea': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'FotografiaYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.fotopiedra': {
            'Meta': {'object_name': 'FotoPiedra', '_ormbases': ['anarapp.Foto']},
            'foto_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Foto']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'FotoPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.hidrologiayacimiento': {
            'Meta': {'object_name': 'HidrologiaYacimiento'},
            'arroyo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'arroyoPerenne': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'distancia': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'laguna': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manantial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manantialIntermitente': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nombre': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'observaciones': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'rio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'HidrologiaYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.indicaciones': {
            'Meta': {'object_name': 'Indicaciones'},
            'direcciones': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puntoDatum': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Indicaciones'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.intensidaddestruccionyac': {
            'Meta': {'object_name': 'IntensidadDestruccionYac'},
            'cincoAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cuatroAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dosAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esDeTiempo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esInmediato': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mas': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'observaciones': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'tresAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'IntensidadDestruccionYac'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.llenadopiedra': {
            'Meta': {'object_name': 'LlenadoPiedra', '_ormbases': ['anarapp.LlenadoPor']},
            'fechaP': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'llenadopor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.LlenadoPor']", 'unique': 'True', 'primary_key': 'True'}),
            'nombreP': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'LlenadoPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.llenadopor': {
            'Meta': {'object_name': 'LlenadoPor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'anarapp.llenadoyac': {
            'Meta': {'object_name': 'LlenadoYac', '_ormbases': ['anarapp.LlenadoPor']},
            'fechaY': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'llenadopor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.LlenadoPor']", 'unique': 'True', 'primary_key': 'True'}),
            'nombreY': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'LlenadoYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.localidadyacimiento': {
            'Meta': {'object_name': 'LocalidadYacimiento'},
            'esCentroNoPoblado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCentroPoblado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esIndigena': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esRural': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esUrbano': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreNoPoblado': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'nombrePoblado': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'LocalidadYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.manifestaciones': {
            'Meta': {'object_name': 'Manifestaciones'},
            'hasMitos': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'hasOtros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Manifestaciones'", 'to': "orm['anarapp.Piedra']"}),
            'tieneAmoladore': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tieneCupula': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tienePetroglifos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tienePuntosAc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tieneRupestres': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'anarapp.manifestacionesasociadas': {
            'Meta': {'object_name': 'ManifestacionesAsociadas'},
            'descripcionCarbon': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'descripcionCementerio': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'descripcionCeramica': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'descripcionConcha': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'descripcionLitica': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'descripcionMito': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'descripcionMonticulo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'descripcionOseo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esCarbon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCementerio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCeramica': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esConcha': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esLitica': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMito': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMonticulo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esOseo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'ManifestacionesAsociadas'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.manifestacionescarbon': {
            'Meta': {'object_name': 'ManifestacionesCarbon'},
            'descripcionCarbon': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esCarbon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'ManifestacionesCarbon'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.manifestacionescementerio': {
            'Meta': {'object_name': 'ManifestacionesCementerio'},
            'descripcionCementerio': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esCementerio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'ManifestacionesCementerio'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.manifestacionesceramica': {
            'Meta': {'object_name': 'ManifestacionesCeramica'},
            'descripcionCeramica': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esCeramica': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'ManifestacionesCeramica'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.manifestacionesconcha': {
            'Meta': {'object_name': 'ManifestacionesConcha'},
            'descripcionConcha': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esConcha': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'ManifestacionesConcha'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.manifestacioneslitica': {
            'Meta': {'object_name': 'ManifestacionesLitica'},
            'descripcionLitica': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esLitica': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'ManifestacionesLitica'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.manifestacionesmito': {
            'Meta': {'object_name': 'ManifestacionesMito'},
            'descripcionMito': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esMito': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'ManifestacionesMito'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.manifestacionesmonticulo': {
            'Meta': {'object_name': 'ManifestacionesMonticulo'},
            'descripcionMonticulo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esMonticulo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'ManifestacionesMonticulo'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.manifestacionesoseo': {
            'Meta': {'object_name': 'ManifestacionesOseo'},
            'descripcionOseo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esOseo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'ManifestacionesOseo'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.manifestacionesotros': {
            'Meta': {'object_name': 'ManifestacionesOtros'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'ManifestacionesOtros'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.manifestacionyacimiento': {
            'Meta': {'object_name': 'ManifestacionYacimiento'},
            'esAmolador': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esBatea': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCerroConDolmen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCerroConPetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCerroConPintura': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCerroMiticoNatural': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCupulas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGeoglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMenhires': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMenhiresConPetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMenhiresConPintura': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMenhiresConPuntos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMicroPetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMonolitoConGrabados': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMonolitos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMonumentosMegaliticos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMortero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPetroglifoPintado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPiedraMiticaNatural': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPintura': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPuntosAcoplados': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'ManifestacionYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.mataudiovisual': {
            'Meta': {'object_name': 'MatAudioVisual'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'anarapp.matavpiedra': {
            'Meta': {'object_name': 'MatAVPiedra', '_ormbases': ['anarapp.MatAudioVisual']},
            'archive': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'format': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'ismatavy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mataudiovisual_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MatAudioVisual']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'MatAVPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.matavyacimiento': {
            'Meta': {'object_name': 'MatAVYacimiento', '_ormbases': ['anarapp.MatAudioVisual']},
            'archive': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'format': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'ismatavy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mataudiovisual_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MatAudioVisual']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'MatAVYacimiento'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.materialyacimiento': {
            'Meta': {'object_name': 'MaterialYacimiento'},
            'esCorteza': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esHueso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esIgnea': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMetamor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPiel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esRoca': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esSedimentaria': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esTierra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'tipo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'MaterialYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.multimedia': {
            'Meta': {'object_name': 'Multimedia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'anarapp.multimediapiedra': {
            'Meta': {'object_name': 'MultimediaPiedra', '_ormbases': ['anarapp.Multimedia']},
            'archivoP': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ismult': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'multimedia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Multimedia']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'MultimediaPiedra'", 'to': "orm['anarapp.Piedra']"}),
            'tecnicaP': ('anarapp.models.CharField', [], {'max_length': '65000', 'null': 'True', 'blank': 'True'})
        },
        'anarapp.multimediayac': {
            'Meta': {'object_name': 'MultimediaYac', '_ormbases': ['anarapp.Multimedia']},
            'archivoY': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ismult': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'multimedia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Multimedia']", 'unique': 'True', 'primary_key': 'True'}),
            'tecnicaY': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'MultimediaYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'activo': ('django.db.models.fields.IntegerField', [], {}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Municipio'", 'to': "orm['anarapp.Estado']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('anarapp.models.CharField', [], {'max_length': '65000'})
        },
        'anarapp.notasyacimiento': {
            'Meta': {'object_name': 'NotasYacimiento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notas': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'NotasYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.observaciones': {
            'Meta': {'object_name': 'Observaciones'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'anarapp.observacionesyac': {
            'Meta': {'object_name': 'ObservacionesYac', '_ormbases': ['anarapp.Observaciones']},
            'observaciones_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Observaciones']", 'unique': 'True', 'primary_key': 'True'}),
            'textoY': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ObservacionesYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.observacpiedra': {
            'Meta': {'object_name': 'ObservacPiedra', '_ormbases': ['anarapp.Observaciones']},
            'observaciones_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Observaciones']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ObservacPiedra'", 'to': "orm['anarapp.Piedra']"}),
            'textoP': ('anarapp.models.CharField', [], {'max_length': '65000'})
        },
        'anarapp.obtencioninfo': {
            'Meta': {'object_name': 'ObtencionInfo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'anarapp.obtinfopiedra': {
            'Meta': {'object_name': 'ObtInfoPiedra', '_ormbases': ['anarapp.ObtencionInfo']},
            'blogP': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'comunicacionP': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'direccionP': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'fechaP': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'isinfo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mailP': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'nombreFacebookP': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'nombreP': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'obtencioninfo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.ObtencionInfo']", 'unique': 'True', 'primary_key': 'True'}),
            'paginaWebP': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ObtInfoPiedra'", 'to': "orm['anarapp.Piedra']"}),
            'prospeccionP': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'telefonoCelP': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'telefonoP': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'twitterP': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'verificadoP': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'anarapp.obtinfoyac': {
            'Meta': {'object_name': 'ObtInfoYac', '_ormbases': ['anarapp.ObtencionInfo']},
            'blogY': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'comunicacionY': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'direccionY': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'fechaY': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'isinfo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mailY': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'nombreFacebookY': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'nombreY': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'obtencioninfo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.ObtencionInfo']", 'unique': 'True', 'primary_key': 'True'}),
            'paginaWebY': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'prospeccionY': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'telefonoCelY': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'telefonoY': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'twitterY': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'verificadoY': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ObtInfoYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.orientacionyacimiento': {
            'Meta': {'object_name': 'OrientacionYacimiento'},
            'haciaCerro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'haciaCielo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'haciaCosta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'haciaRio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'haciaValle': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orientacion': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'OrientacionYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.otrosvalores': {
            'Meta': {'object_name': 'OtrosValores'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'anarapp.otrosvalpiedra': {
            'Meta': {'object_name': 'OtrosValPiedra', '_ormbases': ['anarapp.OtrosValores']},
            'otrosvalores_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.OtrosValores']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'OtrosValPiedra'", 'to': "orm['anarapp.Piedra']"}),
            'texto': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'})
        },
        'anarapp.otrosvalyac': {
            'Meta': {'object_name': 'OtrosValYac', '_ormbases': ['anarapp.OtrosValores']},
            'otrosvalores_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.OtrosValores']", 'unique': 'True', 'primary_key': 'True'}),
            'texto': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'OtrosValYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.paginaweb': {
            'Meta': {'object_name': 'PaginaWeb'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'anarapp.paginawebpiedra': {
            'Meta': {'object_name': 'PaginaWebPiedra', '_ormbases': ['anarapp.PaginaWeb']},
            'direccionURLP': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'paginaweb_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.PaginaWeb']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'PaginaWebPiedra'", 'to': "orm['anarapp.Piedra']"}),
            'tieneWb': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'anarapp.paginawebyac': {
            'Meta': {'object_name': 'PaginaWebYac', '_ormbases': ['anarapp.PaginaWeb']},
            'direccionURLy': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'paginaweb_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.PaginaWeb']", 'unique': 'True', 'primary_key': 'True'}),
            'tieneWb': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'PaginaWebYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.pelicula': {
            'Meta': {'object_name': 'Pelicula', '_ormbases': ['anarapp.Video']},
            'video_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Video']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.peliculapiedra': {
            'Meta': {'object_name': 'PeliculaPiedra', '_ormbases': ['anarapp.Pelicula']},
            'archivoy': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'autory': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'formatoy': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'instituciony': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'isFromAnary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isvidyac': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'numCopiaPiedra': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'numReferenciay': ('django.db.models.fields.IntegerField', [], {}),
            'pelicula_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Pelicula']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'PeliculaPiedra'", 'to': "orm['anarapp.Piedra']"}),
            'tituloy': ('anarapp.models.CharField', [], {'max_length': '65000'})
        },
        'anarapp.peliyacimiento': {
            'Meta': {'object_name': 'PeliYacimiento', '_ormbases': ['anarapp.Pelicula']},
            'anioy': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'archivoy': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'autory': ('anarapp.models.CharField', [], {'max_length': '65000', 'null': 'True', 'blank': 'True'}),
            'formatoy': ('anarapp.models.CharField', [], {'max_length': '65000', 'null': 'True', 'blank': 'True'}),
            'instituciony': ('anarapp.models.CharField', [], {'max_length': '65000', 'null': 'True', 'blank': 'True'}),
            'isFromAnary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isvidyac': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'numCopiayac': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'numReferenciay': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pelicula_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Pelicula']", 'unique': 'True', 'primary_key': 'True'}),
            'tituloy': ('anarapp.models.CharField', [], {'max_length': '65000', 'null': 'True', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'PeliYacimiento'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.piedra': {
            'Meta': {'object_name': 'Piedra'},
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Yacimiento'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.piedra2': {
            'Meta': {'object_name': 'Piedra2'},
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'EstadoPied'", 'null': 'True', 'to': "orm['anarapp.Estado']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreFiguras': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'numeroCaras': ('django.db.models.fields.IntegerField', [], {}),
            'numeroCarasTrajabadas': ('django.db.models.fields.IntegerField', [], {}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Piedra2'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.plano': {
            'Meta': {'object_name': 'Plano'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numeroPlano': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Plano'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.repgrafpiedra': {
            'Meta': {'object_name': 'RepGrafPiedra'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'RepGrafPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.supervisadopiedra': {
            'Meta': {'object_name': 'SupervisadoPiedra', '_ormbases': ['anarapp.SupervisadoPor']},
            'fechaP': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombreP': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'SupervisadoPiedra'", 'to': "orm['anarapp.Piedra']"}),
            'supervisadopor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.SupervisadoPor']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.supervisadopor': {
            'Meta': {'object_name': 'SupervisadoPor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'anarapp.supervisadoyac': {
            'Meta': {'object_name': 'SupervisadoYac', '_ormbases': ['anarapp.SupervisadoPor']},
            'fechaY': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombreY': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'supervisadopor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.SupervisadoPor']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'SupervisadoYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tecnicaparageoglifo': {
            'Meta': {'object_name': 'TecnicaParaGeoglifo'},
            'esGeoflifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tecnicas': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TecnicaParaGeoglifo'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tecnicaparamicropetro': {
            'Meta': {'object_name': 'TecnicaParaMicroPetro'},
            'esAbrasion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAbrasionArena': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAbrasionPiedra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esConcha': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusionDirecta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusionIndirecta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMicro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TecnicaParaMicroPetro'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tecnicaparamonumentos': {
            'Meta': {'object_name': 'TecnicaParaMonumentos'},
            'esDolmen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMenhir': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMonolito': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMonumento': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'tecnicas': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TecnicaParaMonumentos'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tecnicaparapetroglifo': {
            'Meta': {'object_name': 'TecnicaParaPetroglifo'},
            'esAbrasion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAbrasionArena': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAbrasionPiedra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esConcha': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusionDirecta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusionIndirecta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TecnicaParaPetroglifo'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tecnicaparapintura': {
            'Meta': {'object_name': 'TecnicaParaPintura'},
            'conDedo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPintura': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fibra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'soplado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TecnicaParaPintura'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tenenciadetierra': {
            'Meta': {'object_name': 'TenenciaDeTierra'},
            'esABRAE': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esComunal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esEjido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMunicipal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPrivada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esTenenciaOtros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TenenciaDeTierra'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.texturasuelo': {
            'Meta': {'object_name': 'TexturaSuelo'},
            'esArcilloso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esArenoso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPedregoso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esRocaMadre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mixto': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TexturaSuelo'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tipoexposicionyac': {
            'Meta': {'object_name': 'TipoExposicionYac'},
            'expuesto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'expuestoPeriodicamente': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noExpuesto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'observaciones': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TipoExposicionYac'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tipoyacimiento': {
            'Meta': {'object_name': 'TipoYacimiento'},
            'esAbrigo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCueva': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCuevadeRec': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esDolmen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esParedRocosa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esRoca': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esTerrenoPro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esTerrenoSup': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TipoYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tratfoto': {
            'Meta': {'object_name': 'TratFoto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limpiezaCon': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'otrosTratamientos': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'programaVersion': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'rellenoSurcos': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'tratamientoDigital': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'})
        },
        'anarapp.tratfotopiedra': {
            'Meta': {'object_name': 'TratFotoPiedra', '_ormbases': ['anarapp.TratFoto']},
            'piedra': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TratFotoPiedra'", 'unique': 'True', 'to': "orm['anarapp.Piedra']"}),
            'tratfoto_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.TratFoto']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.ubicacioncaras': {
            'Meta': {'object_name': 'UbicacionCaras'},
            'areasEspecificas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'claraboya': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'heights': ('anarapp.models.CharField', [], {'max_length': '65000', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lagoInterior': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'luminosity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'otraSala': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'piedra': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'UbicacionCaras'", 'unique': 'True', 'to': "orm['anarapp.Piedra']"}),
            'principalMouth': ('anarapp.models.CharField', [], {'max_length': '65000', 'null': 'True', 'blank': 'True'}),
            'requiereAndamiaje': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'salaPrincipal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'todaLaCaverna': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'anarapp.ubicacionyacimiento': {
            'Meta': {'object_name': 'UbicacionYacimiento'},
            'enCerro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enCerroAcantilado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enCerroBarranco': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enCerroCima': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enCerroFalda': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enCerroFila': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enCerroLadera': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enCerroPieDeMonte': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enRio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enRioCosta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enRioIsla': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enRioLecho': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enRioMargenDerecha': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enRioMargenIzquierda': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enRioRaudal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enValle': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'UbicacionYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.usoactsuelo': {
            'Meta': {'object_name': 'UsoActSuelo'},
            'esAgriRiesgo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAgriTemp': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esForestal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGanadero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esSueloTuristico': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esSueloUrbano': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'UsoActSuelo'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.video': {
            'Meta': {'object_name': 'Video'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'anarapp.videopiedra': {
            'Meta': {'object_name': 'VideoPiedra', '_ormbases': ['anarapp.Video']},
            'anioy': ('django.db.models.fields.IntegerField', [], {}),
            'archivoy': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'autory': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'formatoy': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'instituciony': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'isFromAnary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isvidyac': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'numCopiaPiedra': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'numReferenciay': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'VideoPiedra'", 'to': "orm['anarapp.Piedra']"}),
            'tituloy': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'video_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Video']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.videoyacimiento': {
            'Meta': {'object_name': 'VideoYacimiento', '_ormbases': ['anarapp.Video']},
            'anioy': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'archivoy': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'autory': ('anarapp.models.CharField', [], {'max_length': '65000', 'null': 'True', 'blank': 'True'}),
            'formatoy': ('anarapp.models.CharField', [], {'max_length': '65000', 'null': 'True', 'blank': 'True'}),
            'instituciony': ('anarapp.models.CharField', [], {'max_length': '65000', 'null': 'True', 'blank': 'True'}),
            'isFromAnary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isvidyac': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'numCopiayac': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'numReferenciay': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tituloy': ('anarapp.models.CharField', [], {'max_length': '65000', 'null': 'True', 'blank': 'True'}),
            'video_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Video']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'VideoYacimiento'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.yacimiento': {
            'Meta': {'object_name': 'Yacimiento'},
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'EstadoYac'", 'null': 'True', 'to': "orm['anarapp.Estado']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('smart_selects.db_fields.ChainedForeignKey', [], {'blank': 'True', 'related_name': "'MunicipioYac'", 'null': 'True', 'to': "orm['anarapp.Municipio']"}),
            'nombre': ('anarapp.models.CharField', [], {'max_length': '65000', 'null': 'True', 'blank': 'True'}),
            'pais': ('anarapp.models.CharField', [], {'default': "'Venezuela'", 'max_length': '65000'})
        }
    }

    complete_apps = ['anarapp']