# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ManifestUbicacionYacimiento'
        db.delete_table('anarapp_manifestubicacionyacimiento')

        # Adding model 'NotasYacimiento'
        db.create_table('anarapp_notasyacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(related_name='NotasYacimiento', unique=True, to=orm['anarapp.Yacimiento'])),
            ('notas', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
        ))
        db.send_create_signal('anarapp', ['NotasYacimiento'])

        # Adding model 'ManifestacionYacimiento'
        db.create_table('anarapp_manifestacionyacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ManifestacionYacimiento', to=orm['anarapp.Yacimiento'])),
            ('tipoManifestacion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['ManifestacionYacimiento'])

        # Adding model 'UbicacionYacimiento'
        db.create_table('anarapp_ubicacionyacimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='UbicacionYacimiento', to=orm['anarapp.Yacimiento'])),
            ('ubicacionManifestacion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['UbicacionYacimiento'])


        # Changing field 'TenenciaDeTierra.yacimiento'
        db.alter_column('anarapp_tenenciadetierra', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'TenenciaDeTierra', fields ['yacimiento']
        db.create_unique('anarapp_tenenciadetierra', ['yacimiento_id'])


        # Changing field 'DimensionPiedra.piedra'
        db.alter_column('anarapp_dimensionpiedra', 'piedra_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Piedra']))
        # Adding unique constraint on 'DimensionPiedra', fields ['piedra']
        db.create_unique('anarapp_dimensionpiedra', ['piedra_id'])


        # Changing field 'Piedra.yacimiento'
        db.alter_column('anarapp_piedra', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'Piedra', fields ['yacimiento']
        db.create_unique('anarapp_piedra', ['yacimiento_id'])


        # Changing field 'FloraYacimiento.yacimiento'
        db.alter_column('anarapp_florayacimiento', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'FloraYacimiento', fields ['yacimiento']
        db.create_unique('anarapp_florayacimiento', ['yacimiento_id'])

        # Adding field 'Coordenadas.utmAdicional'
        db.add_column('anarapp_coordenadas', 'utmAdicional',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=400, blank=True),
                      keep_default=False)


        # Changing field 'Coordenadas.yacimiento'
        db.alter_column('anarapp_coordenadas', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'Coordenadas', fields ['yacimiento']
        db.create_unique('anarapp_coordenadas', ['yacimiento_id'])


        # Changing field 'LocalidadYacimiento.yacimiento'
        db.alter_column('anarapp_localidadyacimiento', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'LocalidadYacimiento', fields ['yacimiento']
        db.create_unique('anarapp_localidadyacimiento', ['yacimiento_id'])


        # Changing field 'CronologiaTentativa.yacimiento'
        db.alter_column('anarapp_cronologiatentativa', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'CronologiaTentativa', fields ['yacimiento']
        db.create_unique('anarapp_cronologiatentativa', ['yacimiento_id'])


        # Changing field 'TipoYacimiento.yacimiento'
        db.alter_column('anarapp_tipoyacimiento', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'TipoYacimiento', fields ['yacimiento']
        db.create_unique('anarapp_tipoyacimiento', ['yacimiento_id'])

        # Adding field 'CaracSurcoBateas.diametro'
        db.add_column('anarapp_caracsurcobateas', 'diametro',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True),
                      keep_default=False)

        # Adding field 'CaracSurcoBateas.profundidad'
        db.add_column('anarapp_caracsurcobateas', 'profundidad',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True),
                      keep_default=False)


        # Changing field 'CaracSurcoBateas.yacimiento'
        db.alter_column('anarapp_caracsurcobateas', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'CaracSurcoBateas', fields ['yacimiento']
        db.create_unique('anarapp_caracsurcobateas', ['yacimiento_id'])


        # Changing field 'CaracSurcoAmoladores.yacimiento'
        db.alter_column('anarapp_caracsurcoamoladores', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'CaracSurcoAmoladores', fields ['yacimiento']
        db.create_unique('anarapp_caracsurcoamoladores', ['yacimiento_id'])


        # Changing field 'Plano.yacimiento'
        db.alter_column('anarapp_plano', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'Plano', fields ['yacimiento']
        db.create_unique('anarapp_plano', ['yacimiento_id'])


        # Changing field 'Plano.numeroPlano'
        db.alter_column('anarapp_plano', 'numeroPlano', self.gf('django.db.models.fields.CharField')(default='', max_length=250))

        # Changing field 'TecnicaParaPintura.yacimiento'
        db.alter_column('anarapp_tecnicaparapintura', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'TecnicaParaPintura', fields ['yacimiento']
        db.create_unique('anarapp_tecnicaparapintura', ['yacimiento_id'])

        # Adding field 'CaracSurcoPuntosAcopl.diametro'
        db.add_column('anarapp_caracsurcopuntosacopl', 'diametro',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True),
                      keep_default=False)

        # Adding field 'CaracSurcoPuntosAcopl.profundidad'
        db.add_column('anarapp_caracsurcopuntosacopl', 'profundidad',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True),
                      keep_default=False)

        # Adding field 'CaracSurcoPuntosAcopl.otros'
        db.add_column('anarapp_caracsurcopuntosacopl', 'otros',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True),
                      keep_default=False)


        # Changing field 'CaracSurcoMortero.yacimiento'
        db.alter_column('anarapp_caracsurcomortero', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'CaracSurcoMortero', fields ['yacimiento']
        db.create_unique('anarapp_caracsurcomortero', ['yacimiento_id'])

        # Deleting field 'CaracDolmenArt.notas'
        db.delete_column('anarapp_caracdolmenart', 'notas')

        # Adding field 'CaracSurcoCupulas.profundidad'
        db.add_column('anarapp_caracsurcocupulas', 'profundidad',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True),
                      keep_default=False)

        # Adding field 'CaracSurcoCupulas.otros'
        db.add_column('anarapp_caracsurcocupulas', 'otros',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True),
                      keep_default=False)


        # Changing field 'CaracSurcoCupulas.yacimiento'
        db.alter_column('anarapp_caracsurcocupulas', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'CaracSurcoCupulas', fields ['yacimiento']
        db.create_unique('anarapp_caracsurcocupulas', ['yacimiento_id'])


        # Changing field 'Manifestaciones.piedra'
        db.alter_column('anarapp_manifestaciones', 'piedra_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Piedra']))
        # Adding unique constraint on 'Manifestaciones', fields ['piedra']
        db.create_unique('anarapp_manifestaciones', ['piedra_id'])


        # Changing field 'CaraTrabajada.numero'
        db.alter_column('anarapp_caratrabajada', 'numero', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'TecnicaParaPetroglifo.yacimiento'
        db.alter_column('anarapp_tecnicaparapetroglifo', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'TecnicaParaPetroglifo', fields ['yacimiento']
        db.create_unique('anarapp_tecnicaparapetroglifo', ['yacimiento_id'])


        # Changing field 'UsoActSuelo.yacimiento'
        db.alter_column('anarapp_usoactsuelo', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'UsoActSuelo', fields ['yacimiento']
        db.create_unique('anarapp_usoactsuelo', ['yacimiento_id'])


        # Changing field 'Datum.yacimiento'
        db.alter_column('anarapp_datum', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'Datum', fields ['yacimiento']
        db.create_unique('anarapp_datum', ['yacimiento_id'])

        # Adding field 'TipoExposicionYac.noExpuesto'
        db.add_column('anarapp_tipoexposicionyac', 'noExpuesto',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'TipoExposicionYac.yacimiento'
        db.alter_column('anarapp_tipoexposicionyac', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'TipoExposicionYac', fields ['yacimiento']
        db.create_unique('anarapp_tipoexposicionyac', ['yacimiento_id'])


        # Changing field 'OrientacionYacimiento.yacimiento'
        db.alter_column('anarapp_orientacionyacimiento', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'OrientacionYacimiento', fields ['yacimiento']
        db.create_unique('anarapp_orientacionyacimiento', ['yacimiento_id'])


        # Changing field 'EsquemaPorCara.posicion'
        db.alter_column('anarapp_esquemaporcara', 'posicion', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'EsquemaPorCara.numero'
        db.alter_column('anarapp_esquemaporcara', 'numero', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'ConstitucionYacimiento.yacimiento'
        db.alter_column('anarapp_constitucionyacimiento', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'ConstitucionYacimiento', fields ['yacimiento']
        db.create_unique('anarapp_constitucionyacimiento', ['yacimiento_id'])


        # Changing field 'MaterialYacimiento.yacimiento'
        db.alter_column('anarapp_materialyacimiento', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'MaterialYacimiento', fields ['yacimiento']
        db.create_unique('anarapp_materialyacimiento', ['yacimiento_id'])


        # Changing field 'TexturaSuelo.yacimiento'
        db.alter_column('anarapp_texturasuelo', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'TexturaSuelo', fields ['yacimiento']
        db.create_unique('anarapp_texturasuelo', ['yacimiento_id'])


        # Changing field 'HidrologiaYacimiento.yacimiento'
        db.alter_column('anarapp_hidrologiayacimiento', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'HidrologiaYacimiento', fields ['yacimiento']
        db.create_unique('anarapp_hidrologiayacimiento', ['yacimiento_id'])


        # Changing field 'CaracSurcoPetroglifo.yacimiento'
        db.alter_column('anarapp_caracsurcopetroglifo', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'CaracSurcoPetroglifo', fields ['yacimiento']
        db.create_unique('anarapp_caracsurcopetroglifo', ['yacimiento_id'])

        # Adding field 'FigurasPorTipo.esCantidadInexacta'
        db.add_column('anarapp_figurasportipo', 'esCantidadInexacta',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'FigurasPorTipo.cantidad'
        db.alter_column('anarapp_figurasportipo', 'cantidad', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'FigurasPorTipo.numero'
        db.alter_column('anarapp_figurasportipo', 'numero', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'TecnicaParaGeoglifo.yacimiento'
        db.alter_column('anarapp_tecnicaparageoglifo', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'TecnicaParaGeoglifo', fields ['yacimiento']
        db.create_unique('anarapp_tecnicaparageoglifo', ['yacimiento_id'])


        # Changing field 'UbicacionCaras.piedra'
        db.alter_column('anarapp_ubicacioncaras', 'piedra_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Piedra']))
        # Adding unique constraint on 'UbicacionCaras', fields ['piedra']
        db.create_unique('anarapp_ubicacioncaras', ['piedra_id'])

        # Adding field 'Altitud.texto'
        db.add_column('anarapp_altitud', 'texto',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=400, blank=True),
                      keep_default=False)

        # Adding field 'Altitud.desarrollo'
        db.add_column('anarapp_altitud', 'desarrollo',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=400, blank=True),
                      keep_default=False)

        # Adding field 'Altitud.desnivel'
        db.add_column('anarapp_altitud', 'desnivel',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=400, blank=True),
                      keep_default=False)


        # Changing field 'Altitud.yacimiento'
        db.alter_column('anarapp_altitud', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'Altitud', fields ['yacimiento']
        db.create_unique('anarapp_altitud', ['yacimiento_id'])


        # Changing field 'TratFotoPiedra.piedra'
        db.alter_column('anarapp_tratfotopiedra', 'piedra_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Piedra']))
        # Adding unique constraint on 'TratFotoPiedra', fields ['piedra']
        db.create_unique('anarapp_tratfotopiedra', ['piedra_id'])


        # Changing field 'FaunaYacimiento.yacimiento'
        db.alter_column('anarapp_faunayacimiento', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'FaunaYacimiento', fields ['yacimiento']
        db.create_unique('anarapp_faunayacimiento', ['yacimiento_id'])


        # Changing field 'ConexionFiguras.piedra'
        db.alter_column('anarapp_conexionfiguras', 'piedra_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Piedra']))
        # Adding unique constraint on 'ConexionFiguras', fields ['piedra']
        db.create_unique('anarapp_conexionfiguras', ['piedra_id'])


        # Changing field 'Indicaciones.yacimiento'
        db.alter_column('anarapp_indicaciones', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'Indicaciones', fields ['yacimiento']
        db.create_unique('anarapp_indicaciones', ['yacimiento_id'])


        # Changing field 'TecnicaParaMicroPetro.yacimiento'
        db.alter_column('anarapp_tecnicaparamicropetro', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'TecnicaParaMicroPetro', fields ['yacimiento']
        db.create_unique('anarapp_tecnicaparamicropetro', ['yacimiento_id'])


        # Changing field 'TecnicaParaMonumentos.yacimiento'
        db.alter_column('anarapp_tecnicaparamonumentos', 'yacimiento_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['anarapp.Yacimiento']))
        # Adding unique constraint on 'TecnicaParaMonumentos', fields ['yacimiento']
        db.create_unique('anarapp_tecnicaparamonumentos', ['yacimiento_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'TecnicaParaMonumentos', fields ['yacimiento']
        db.delete_unique('anarapp_tecnicaparamonumentos', ['yacimiento_id'])

        # Removing unique constraint on 'TecnicaParaMicroPetro', fields ['yacimiento']
        db.delete_unique('anarapp_tecnicaparamicropetro', ['yacimiento_id'])

        # Removing unique constraint on 'Indicaciones', fields ['yacimiento']
        db.delete_unique('anarapp_indicaciones', ['yacimiento_id'])

        # Removing unique constraint on 'ConexionFiguras', fields ['piedra']
        db.delete_unique('anarapp_conexionfiguras', ['piedra_id'])

        # Removing unique constraint on 'FaunaYacimiento', fields ['yacimiento']
        db.delete_unique('anarapp_faunayacimiento', ['yacimiento_id'])

        # Removing unique constraint on 'TratFotoPiedra', fields ['piedra']
        db.delete_unique('anarapp_tratfotopiedra', ['piedra_id'])

        # Removing unique constraint on 'Altitud', fields ['yacimiento']
        db.delete_unique('anarapp_altitud', ['yacimiento_id'])

        # Removing unique constraint on 'UbicacionCaras', fields ['piedra']
        db.delete_unique('anarapp_ubicacioncaras', ['piedra_id'])

        # Removing unique constraint on 'TecnicaParaGeoglifo', fields ['yacimiento']
        db.delete_unique('anarapp_tecnicaparageoglifo', ['yacimiento_id'])

        # Removing unique constraint on 'CaracSurcoPetroglifo', fields ['yacimiento']
        db.delete_unique('anarapp_caracsurcopetroglifo', ['yacimiento_id'])

        # Removing unique constraint on 'HidrologiaYacimiento', fields ['yacimiento']
        db.delete_unique('anarapp_hidrologiayacimiento', ['yacimiento_id'])

        # Removing unique constraint on 'TexturaSuelo', fields ['yacimiento']
        db.delete_unique('anarapp_texturasuelo', ['yacimiento_id'])

        # Removing unique constraint on 'MaterialYacimiento', fields ['yacimiento']
        db.delete_unique('anarapp_materialyacimiento', ['yacimiento_id'])

        # Removing unique constraint on 'ConstitucionYacimiento', fields ['yacimiento']
        db.delete_unique('anarapp_constitucionyacimiento', ['yacimiento_id'])

        # Removing unique constraint on 'OrientacionYacimiento', fields ['yacimiento']
        db.delete_unique('anarapp_orientacionyacimiento', ['yacimiento_id'])

        # Removing unique constraint on 'TipoExposicionYac', fields ['yacimiento']
        db.delete_unique('anarapp_tipoexposicionyac', ['yacimiento_id'])

        # Removing unique constraint on 'Datum', fields ['yacimiento']
        db.delete_unique('anarapp_datum', ['yacimiento_id'])

        # Removing unique constraint on 'UsoActSuelo', fields ['yacimiento']
        db.delete_unique('anarapp_usoactsuelo', ['yacimiento_id'])

        # Removing unique constraint on 'TecnicaParaPetroglifo', fields ['yacimiento']
        db.delete_unique('anarapp_tecnicaparapetroglifo', ['yacimiento_id'])

        # Removing unique constraint on 'Manifestaciones', fields ['piedra']
        db.delete_unique('anarapp_manifestaciones', ['piedra_id'])

        # Removing unique constraint on 'CaracSurcoCupulas', fields ['yacimiento']
        db.delete_unique('anarapp_caracsurcocupulas', ['yacimiento_id'])

        # Removing unique constraint on 'CaracSurcoMortero', fields ['yacimiento']
        db.delete_unique('anarapp_caracsurcomortero', ['yacimiento_id'])

        # Removing unique constraint on 'TecnicaParaPintura', fields ['yacimiento']
        db.delete_unique('anarapp_tecnicaparapintura', ['yacimiento_id'])

        # Removing unique constraint on 'Plano', fields ['yacimiento']
        db.delete_unique('anarapp_plano', ['yacimiento_id'])

        # Removing unique constraint on 'CaracSurcoAmoladores', fields ['yacimiento']
        db.delete_unique('anarapp_caracsurcoamoladores', ['yacimiento_id'])

        # Removing unique constraint on 'CaracSurcoBateas', fields ['yacimiento']
        db.delete_unique('anarapp_caracsurcobateas', ['yacimiento_id'])

        # Removing unique constraint on 'TipoYacimiento', fields ['yacimiento']
        db.delete_unique('anarapp_tipoyacimiento', ['yacimiento_id'])

        # Removing unique constraint on 'CronologiaTentativa', fields ['yacimiento']
        db.delete_unique('anarapp_cronologiatentativa', ['yacimiento_id'])

        # Removing unique constraint on 'LocalidadYacimiento', fields ['yacimiento']
        db.delete_unique('anarapp_localidadyacimiento', ['yacimiento_id'])

        # Removing unique constraint on 'Coordenadas', fields ['yacimiento']
        db.delete_unique('anarapp_coordenadas', ['yacimiento_id'])

        # Removing unique constraint on 'FloraYacimiento', fields ['yacimiento']
        db.delete_unique('anarapp_florayacimiento', ['yacimiento_id'])

        # Removing unique constraint on 'Piedra', fields ['yacimiento']
        db.delete_unique('anarapp_piedra', ['yacimiento_id'])

        # Removing unique constraint on 'DimensionPiedra', fields ['piedra']
        db.delete_unique('anarapp_dimensionpiedra', ['piedra_id'])

        # Removing unique constraint on 'TenenciaDeTierra', fields ['yacimiento']
        db.delete_unique('anarapp_tenenciadetierra', ['yacimiento_id'])

        # Adding model 'ManifestUbicacionYacimiento'
        db.create_table('anarapp_manifestubicacionyacimiento', (
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='manifestacion', to=orm['anarapp.Yacimiento'])),
            ('ubicacionManifestacion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tipoManifestacion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['ManifestUbicacionYacimiento'])

        # Deleting model 'NotasYacimiento'
        db.delete_table('anarapp_notasyacimiento')

        # Deleting model 'ManifestacionYacimiento'
        db.delete_table('anarapp_manifestacionyacimiento')

        # Deleting model 'UbicacionYacimiento'
        db.delete_table('anarapp_ubicacionyacimiento')


        # Changing field 'TenenciaDeTierra.yacimiento'
        db.alter_column('anarapp_tenenciadetierra', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

        # Changing field 'DimensionPiedra.piedra'
        db.alter_column('anarapp_dimensionpiedra', 'piedra_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra']))

        # Changing field 'Piedra.yacimiento'
        db.alter_column('anarapp_piedra', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

        # Changing field 'FloraYacimiento.yacimiento'
        db.alter_column('anarapp_florayacimiento', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))
        # Deleting field 'Coordenadas.utmAdicional'
        db.delete_column('anarapp_coordenadas', 'utmAdicional')


        # Changing field 'Coordenadas.yacimiento'
        db.alter_column('anarapp_coordenadas', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

        # Changing field 'LocalidadYacimiento.yacimiento'
        db.alter_column('anarapp_localidadyacimiento', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

        # Changing field 'CronologiaTentativa.yacimiento'
        db.alter_column('anarapp_cronologiatentativa', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

        # Changing field 'TipoYacimiento.yacimiento'
        db.alter_column('anarapp_tipoyacimiento', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))
        # Deleting field 'CaracSurcoBateas.diametro'
        db.delete_column('anarapp_caracsurcobateas', 'diametro')

        # Deleting field 'CaracSurcoBateas.profundidad'
        db.delete_column('anarapp_caracsurcobateas', 'profundidad')


        # Changing field 'CaracSurcoBateas.yacimiento'
        db.alter_column('anarapp_caracsurcobateas', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

        # Changing field 'CaracSurcoAmoladores.yacimiento'
        db.alter_column('anarapp_caracsurcoamoladores', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

        # Changing field 'Plano.yacimiento'
        db.alter_column('anarapp_plano', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

        # Changing field 'Plano.numeroPlano'
        db.alter_column('anarapp_plano', 'numeroPlano', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'TecnicaParaPintura.yacimiento'
        db.alter_column('anarapp_tecnicaparapintura', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))
        # Deleting field 'CaracSurcoPuntosAcopl.diametro'
        db.delete_column('anarapp_caracsurcopuntosacopl', 'diametro')

        # Deleting field 'CaracSurcoPuntosAcopl.profundidad'
        db.delete_column('anarapp_caracsurcopuntosacopl', 'profundidad')

        # Deleting field 'CaracSurcoPuntosAcopl.otros'
        db.delete_column('anarapp_caracsurcopuntosacopl', 'otros')


        # Changing field 'CaracSurcoMortero.yacimiento'
        db.alter_column('anarapp_caracsurcomortero', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))
        # Adding field 'CaracDolmenArt.notas'
        db.add_column('anarapp_caracdolmenart', 'notas',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=400, blank=True),
                      keep_default=False)

        # Deleting field 'CaracSurcoCupulas.profundidad'
        db.delete_column('anarapp_caracsurcocupulas', 'profundidad')

        # Deleting field 'CaracSurcoCupulas.otros'
        db.delete_column('anarapp_caracsurcocupulas', 'otros')


        # Changing field 'CaracSurcoCupulas.yacimiento'
        db.alter_column('anarapp_caracsurcocupulas', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

        # Changing field 'Manifestaciones.piedra'
        db.alter_column('anarapp_manifestaciones', 'piedra_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra']))

        # Changing field 'CaraTrabajada.numero'
        db.alter_column('anarapp_caratrabajada', 'numero', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TecnicaParaPetroglifo.yacimiento'
        db.alter_column('anarapp_tecnicaparapetroglifo', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

        # Changing field 'UsoActSuelo.yacimiento'
        db.alter_column('anarapp_usoactsuelo', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

        # Changing field 'Datum.yacimiento'
        db.alter_column('anarapp_datum', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))
        # Deleting field 'TipoExposicionYac.noExpuesto'
        db.delete_column('anarapp_tipoexposicionyac', 'noExpuesto')


        # Changing field 'TipoExposicionYac.yacimiento'
        db.alter_column('anarapp_tipoexposicionyac', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

        # Changing field 'OrientacionYacimiento.yacimiento'
        db.alter_column('anarapp_orientacionyacimiento', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

        # Changing field 'EsquemaPorCara.posicion'
        db.alter_column('anarapp_esquemaporcara', 'posicion', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'EsquemaPorCara.numero'
        db.alter_column('anarapp_esquemaporcara', 'numero', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'ConstitucionYacimiento.yacimiento'
        db.alter_column('anarapp_constitucionyacimiento', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

        # Changing field 'MaterialYacimiento.yacimiento'
        db.alter_column('anarapp_materialyacimiento', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

        # Changing field 'TexturaSuelo.yacimiento'
        db.alter_column('anarapp_texturasuelo', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

        # Changing field 'HidrologiaYacimiento.yacimiento'
        db.alter_column('anarapp_hidrologiayacimiento', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

        # Changing field 'CaracSurcoPetroglifo.yacimiento'
        db.alter_column('anarapp_caracsurcopetroglifo', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))
        # Deleting field 'FigurasPorTipo.esCantidadInexacta'
        db.delete_column('anarapp_figurasportipo', 'esCantidadInexacta')


        # Changing field 'FigurasPorTipo.cantidad'
        db.alter_column('anarapp_figurasportipo', 'cantidad', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'FigurasPorTipo.numero'
        db.alter_column('anarapp_figurasportipo', 'numero', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TecnicaParaGeoglifo.yacimiento'
        db.alter_column('anarapp_tecnicaparageoglifo', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

        # Changing field 'UbicacionCaras.piedra'
        db.alter_column('anarapp_ubicacioncaras', 'piedra_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra']))
        # Deleting field 'Altitud.texto'
        db.delete_column('anarapp_altitud', 'texto')

        # Deleting field 'Altitud.desarrollo'
        db.delete_column('anarapp_altitud', 'desarrollo')

        # Deleting field 'Altitud.desnivel'
        db.delete_column('anarapp_altitud', 'desnivel')


        # Changing field 'Altitud.yacimiento'
        db.alter_column('anarapp_altitud', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

        # Changing field 'TratFotoPiedra.piedra'
        db.alter_column('anarapp_tratfotopiedra', 'piedra_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra']))

        # Changing field 'FaunaYacimiento.yacimiento'
        db.alter_column('anarapp_faunayacimiento', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

        # Changing field 'ConexionFiguras.piedra'
        db.alter_column('anarapp_conexionfiguras', 'piedra_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra']))

        # Changing field 'Indicaciones.yacimiento'
        db.alter_column('anarapp_indicaciones', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

        # Changing field 'TecnicaParaMicroPetro.yacimiento'
        db.alter_column('anarapp_tecnicaparamicropetro', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

        # Changing field 'TecnicaParaMonumentos.yacimiento'
        db.alter_column('anarapp_tecnicaparamonumentos', 'yacimiento_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento']))

    models = {
        'anarapp.altitud': {
            'Meta': {'object_name': 'Altitud'},
            'altura': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'desarrollo': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'desnivel': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'superficie': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'texto': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Altitud'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.bibliografia': {
            'Meta': {'object_name': 'Bibliografia'},
            'ano': ('django.db.models.fields.IntegerField', [], {}),
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'conDibujo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'anarapp.bibpiedra': {
            'Meta': {'object_name': 'BibPiedra', '_ormbases': ['anarapp.Bibliografia']},
            'bibliografia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Bibliografia']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'BibPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.bibyacimiento': {
            'Meta': {'object_name': 'BibYacimiento', '_ormbases': ['anarapp.Bibliografia']},
            'bibliografia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Bibliografia']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'BibYacimiento'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracdelapintura': {
            'Meta': {'object_name': 'CaracDeLaPintura'},
            'anchoA': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'anchoAComp': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'anchoDe': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'anchoDeComp': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'esImpresionDeManos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esImpresionDeManosNegativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esImpresionDeManosPositivo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esLineaCompuesta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esLineaSencilla': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPinturaRupestre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esTecnicaDactilar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esTecnicaFibra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'tienesFigurasSuperpuestas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracDeLaPintura'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracdolmenart': {
            'ConPetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Meta': {'object_name': 'CaracDolmenArt'},
            'cantidadConPetroglifo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cantidadConPinturas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'conPinturas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sonPiedrasVerticales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracMehnires'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracmonolitos': {
            'Meta': {'object_name': 'CaracMonolitos'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cantidadConGrabados': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'esPinturaRupestre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracMonolitos'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcoamoladores': {
            'Meta': {'object_name': 'CaracSurcoAmoladores'},
            'ancho': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'diametro': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracSurcoAmoladores'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcobateas': {
            'Meta': {'object_name': 'CaracSurcoBateas'},
            'ancho': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'diametro': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'profundidad': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracSurcoBateas'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcocupulas': {
            'Meta': {'object_name': 'CaracSurcoCupulas'},
            'ancho': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'diametro': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'profundidad': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracSurcoCupulas'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcomortero': {
            'Meta': {'object_name': 'CaracSurcoMortero'},
            'ancho': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracSurcoMortero'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcopetroglifo': {
            'Meta': {'object_name': 'CaracSurcoPetroglifo'},
            'anchoA': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'anchoDe': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
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
            'esGrabadoRebajado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoSuperpuesto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'produndidadDe': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'profundidadA': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracSurcoPetroglifo'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcopuntosacopl': {
            'Meta': {'object_name': 'CaracSurcoPuntosAcopl'},
            'diametro': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'esPunteado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'profundidad': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracSurcoPuntosAcopl'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caratrabajada': {
            'Meta': {'object_name': 'CaraTrabajada'},
            'alto': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'ancho': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'orientacion': ('django.db.models.fields.IntegerField', [], {}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'CaraTrabajada'", 'to': "orm['anarapp.Piedra']"})
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
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'ConsiderTemp'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.constitucionyacimiento': {
            'Meta': {'object_name': 'ConstitucionYacimiento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nroPiedras': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nroPiedrasColocadas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nroPiedrasGrabadas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nroPiedrasPintadas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'ConstitucionYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.coordenadas': {
            'Meta': {'object_name': 'Coordenadas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'utmAdicional': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Coordenadas'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.cronologiatentativa': {
            'Meta': {'object_name': 'CronologiaTentativa'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'bibliografia': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'esCrono1': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono3': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono4': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono5': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono6': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono7': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'mail': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'tecnica': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CronologiaTentativa'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.croquis': {
            'Meta': {'object_name': 'Croquis'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'urlImagen': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Croquis'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.datum': {
            'Meta': {'object_name': 'Datum'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipoDatum': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Datum'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.dimensionpiedra': {
            'Meta': {'object_name': 'DimensionPiedra'},
            'altoMaximo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'anchoMaximo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largoMaximo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'piedra': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'DimensionPiedra'", 'unique': 'True', 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.escnatpiedra': {
            'Meta': {'object_name': 'EscNatPiedra', '_ormbases': ['anarapp.RepGrafPiedra']},
            'repgrafpiedra_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.RepGrafPiedra']", 'unique': 'True', 'primary_key': 'True'}),
            'tipoReproduccion': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.escredpiedra': {
            'Meta': {'object_name': 'EscRedPiedra', '_ormbases': ['anarapp.RepGrafPiedra']},
            'repgrafpiedra_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.RepGrafPiedra']", 'unique': 'True', 'primary_key': 'True'}),
            'tipoReproduccion': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.esquemaporcara': {
            'Meta': {'object_name': 'EsquemaPorCara'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'EsquemaPorCara'", 'to': "orm['anarapp.Piedra']"}),
            'posicion': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'textoCara': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'anarapp.estadoconseryac': {
            'Meta': {'object_name': 'EstadoConserYac'},
            'cincoAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'crecimientoVeg': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'crecimientoVegPa': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'cuatroAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'destruccionPotencial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'destruido': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'destruidoPa': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'dosAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enBuenEstado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enPorCausaHumana': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enPorCausaHumanaAguda': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enPorCausaHumanaLigera': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enPorCausaNaturalAguda': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enPorCausaNaturalLigera': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enterrado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'enterradoPa': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'erosion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'erosionPa': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'esDeTiempo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esInmediato': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPorCausaNatural': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'especificar': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'estaDestruido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estadoModificado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mas': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'observaciones': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'patina': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'patinaPa': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'perdido': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'perdidoPa': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
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
            'sumergido': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sumergidoPa': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'trasladado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trasladadoPa': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'tresAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'EstadoConserYac'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.faunayacimiento': {
            'Meta': {'object_name': 'FaunaYacimiento'},
            'fauna': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'FaunaYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.figurasportipo': {
            'Meta': {'object_name': 'FigurasPorTipo'},
            'cantidad': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'esCantidadInexacta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'FigurasPorTipo'", 'to': "orm['anarapp.Piedra']"}),
            'tipoFigura': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.florayacimiento': {
            'Meta': {'object_name': 'FloraYacimiento'},
            'flora': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'FloraYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.foto': {
            'Meta': {'object_name': 'Foto'},
            'esDeAnar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'fotografo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'negativo': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'numCopiaAnar': ('django.db.models.fields.IntegerField', [], {}),
            'numFoto': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numMarcaNegativo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numReferencia': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numRollo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tipoFotografia': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.fotobibliografia': {
            'Meta': {'object_name': 'FotoBibliografia'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'esBlancoYNegro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esDiapositiva': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esDigital': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esFotografia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esNegativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPapel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'escolor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipoMapa': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.fotobibpiedra': {
            'Meta': {'object_name': 'FotoBibPiedra', '_ormbases': ['anarapp.FotoBibliografia']},
            'fotobibliografia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.FotoBibliografia']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'FotoBibPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.fotobibyac': {
            'Meta': {'object_name': 'FotoBibYac', '_ormbases': ['anarapp.FotoBibliografia']},
            'fotobibliografia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.FotoBibliografia']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'FotoBibYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.fotografiayac': {
            'Meta': {'object_name': 'FotografiaYac'},
            'esAerea': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esSatelital': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noEsAerea': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'urlImagen': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
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
            'distancia': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'laguna': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manantial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manantialIntermitente': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'observaciones': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'rio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'HidrologiaYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.indicaciones': {
            'Meta': {'object_name': 'Indicaciones'},
            'direcciones': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puntoDatum': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Indicaciones'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.llenadopiedra': {
            'Meta': {'object_name': 'LlenadoPiedra', '_ormbases': ['anarapp.LlenadoPor']},
            'llenadopor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.LlenadoPor']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'LlenadoPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.llenadopor': {
            'Meta': {'object_name': 'LlenadoPor'},
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'anarapp.llenadoyac': {
            'Meta': {'object_name': 'LlenadoYac', '_ormbases': ['anarapp.LlenadoPor']},
            'llenadopor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.LlenadoPor']", 'unique': 'True', 'primary_key': 'True'}),
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
            'nombreNoPoblado': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'nombrePoblado': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'LocalidadYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.manifestaciones': {
            'Meta': {'object_name': 'Manifestaciones'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Manifestaciones'", 'unique': 'True', 'to': "orm['anarapp.Piedra']"}),
            'tieneAmoladores': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tieneCupulas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tienePetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tienePinturaRupestre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tienePuntosAcoplados': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'anarapp.manifestacionesasociadas': {
            'Meta': {'object_name': 'ManifestacionesAsociadas'},
            'descripcionCarbon': ('django.db.models.fields.CharField', [], {'max_length': '1200', 'blank': 'True'}),
            'descripcionCementerio': ('django.db.models.fields.CharField', [], {'max_length': '1200', 'blank': 'True'}),
            'descripcionCeramica': ('django.db.models.fields.CharField', [], {'max_length': '1200', 'blank': 'True'}),
            'descripcionConcha': ('django.db.models.fields.CharField', [], {'max_length': '1200', 'blank': 'True'}),
            'descripcionLitica': ('django.db.models.fields.CharField', [], {'max_length': '1200', 'blank': 'True'}),
            'descripcionMito': ('django.db.models.fields.CharField', [], {'max_length': '1200', 'blank': 'True'}),
            'descripcionMonticulo': ('django.db.models.fields.CharField', [], {'max_length': '1200', 'blank': 'True'}),
            'descripcionOseo': ('django.db.models.fields.CharField', [], {'max_length': '1200', 'blank': 'True'}),
            'esCarbon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCementerio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCeramica': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esConcha': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esLitica': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMito': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMonticulo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esOseo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '1200', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'ManifestacionesAsociadas'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.manifestacionyacimiento': {
            'Meta': {'object_name': 'ManifestacionYacimiento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipoManifestacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ManifestacionYacimiento'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.mataudiovisual': {
            'Meta': {'object_name': 'MatAudioVisual'},
            'formato': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'})
        },
        'anarapp.matavpiedra': {
            'Meta': {'object_name': 'MatAVPiedra', '_ormbases': ['anarapp.MatAudioVisual']},
            'mataudiovisual_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MatAudioVisual']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'MatAVPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.matavyacimiento': {
            'Meta': {'object_name': 'MatAVYacimiento', '_ormbases': ['anarapp.MatAudioVisual']},
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
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'MaterialYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.multimedia': {
            'Meta': {'object_name': 'Multimedia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tecnica': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'anarapp.multimediapiedra': {
            'Meta': {'object_name': 'MultimediaPiedra', '_ormbases': ['anarapp.Multimedia']},
            'multimedia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Multimedia']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'MultimediaPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.multimediayac': {
            'Meta': {'object_name': 'MultimediaYac', '_ormbases': ['anarapp.Multimedia']},
            'multimedia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Multimedia']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'MultimediaYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.notasyacimiento': {
            'Meta': {'object_name': 'NotasYacimiento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notas': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'NotasYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.observaciones': {
            'Meta': {'object_name': 'Observaciones'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texto': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'anarapp.observacionesyac': {
            'Meta': {'object_name': 'ObservacionesYac', '_ormbases': ['anarapp.Observaciones']},
            'observaciones_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Observaciones']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ObservacionesYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.observacpiedra': {
            'Meta': {'object_name': 'ObservacPiedra', '_ormbases': ['anarapp.Observaciones']},
            'observaciones_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Observaciones']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ObservacPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.obtencioninfo': {
            'Meta': {'object_name': 'ObtencionInfo'},
            'blog': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'comunicacion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nombreFacebook': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'paginaWeb': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'prospeccion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'telefonoCel': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'verificado': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'anarapp.obtinfopiedra': {
            'Meta': {'object_name': 'ObtInfoPiedra', '_ormbases': ['anarapp.ObtencionInfo']},
            'obtencioninfo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.ObtencionInfo']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ObtInfoPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.obtinfoyac': {
            'Meta': {'object_name': 'ObtInfoYac', '_ormbases': ['anarapp.ObtencionInfo']},
            'obtencioninfo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.ObtencionInfo']", 'unique': 'True', 'primary_key': 'True'}),
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
            'orientacion': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'OrientacionYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.otrosvalores': {
            'Meta': {'object_name': 'OtrosValores'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texto': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'anarapp.otrosvalpiedra': {
            'Meta': {'object_name': 'OtrosValPiedra', '_ormbases': ['anarapp.OtrosValores']},
            'otrosvalores_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.OtrosValores']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'OtrosValPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.otrosvalyac': {
            'Meta': {'object_name': 'OtrosValYac', '_ormbases': ['anarapp.OtrosValores']},
            'otrosvalores_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.OtrosValores']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'OtrosValYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.paginaweb': {
            'Meta': {'object_name': 'PaginaWeb'},
            'direccionURL': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'anarapp.paginawebpiedra': {
            'Meta': {'object_name': 'PaginaWebPiedra', '_ormbases': ['anarapp.PaginaWeb']},
            'paginaweb_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.PaginaWeb']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'PaginaWebPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.paginawebyac': {
            'Meta': {'object_name': 'PaginaWebYac', '_ormbases': ['anarapp.PaginaWeb']},
            'paginaweb_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.PaginaWeb']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'PaginaWebYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.pelicula': {
            'Meta': {'object_name': 'Pelicula', '_ormbases': ['anarapp.Video']},
            'video_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Video']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.peliculapiedra': {
            'Meta': {'object_name': 'PeliculaPiedra', '_ormbases': ['anarapp.Pelicula']},
            'pelicula_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Pelicula']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'PeliculaPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.peliyacimiento': {
            'Meta': {'object_name': 'PeliYacimiento', '_ormbases': ['anarapp.Pelicula']},
            'pelicula_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Pelicula']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'PeliYacimiento'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.piedra': {
            'Meta': {'object_name': 'Piedra'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manifiestacionAsociada': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombreFiguras': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'numeroCaras': ('django.db.models.fields.IntegerField', [], {}),
            'numeroCarasTrajabadas': ('django.db.models.fields.IntegerField', [], {}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Piedra'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.plano': {
            'Meta': {'object_name': 'Plano'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numeroPlano': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Plano'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.repgrafpiedra': {
            'Meta': {'object_name': 'RepGrafPiedra'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instituto': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'numPiezas': ('django.db.models.fields.IntegerField', [], {}),
            'persona': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'RepGrafPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.supervisadopiedra': {
            'Meta': {'object_name': 'SupervisadoPiedra', '_ormbases': ['anarapp.SupervisadoPor']},
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'SupervisadoPiedra'", 'to': "orm['anarapp.Piedra']"}),
            'supervisadopor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.SupervisadoPor']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.supervisadopor': {
            'Meta': {'object_name': 'SupervisadoPor'},
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'anarapp.supervisadoyac': {
            'Meta': {'object_name': 'SupervisadoYac', '_ormbases': ['anarapp.SupervisadoPor']},
            'supervisadopor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.SupervisadoPor']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'SupervisadoYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tecnicaparageoglifo': {
            'Meta': {'object_name': 'TecnicaParaGeoglifo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tecnicas': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TecnicaParaGeoglifo'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tecnicaparamicropetro': {
            'Meta': {'object_name': 'TecnicaParaMicroPetro'},
            'esAbrasion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAbrasionArena': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAbrasionPiedra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusionDirecta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusionIndirecta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TecnicaParaMicroPetro'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tecnicaparamonumentos': {
            'Meta': {'object_name': 'TecnicaParaMonumentos'},
            'esDolmen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMenhir': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMonolito': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'tecnicas': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TecnicaParaMonumentos'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tecnicaparapetroglifo': {
            'Meta': {'object_name': 'TecnicaParaPetroglifo'},
            'esAbrasion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAbrasionArena': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAbrasionPiedra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusionDirecta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusionIndirecta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TecnicaParaPetroglifo'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tecnicaparapintura': {
            'Meta': {'object_name': 'TecnicaParaPintura'},
            'conDedo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fibra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
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
            'esTenenciaOtros': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
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
            'mixto': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TexturaSuelo'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tipoexposicionyac': {
            'Meta': {'object_name': 'TipoExposicionYac'},
            'expuesto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'expuestoPeriodicamente': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noExpuesto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'observaciones': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
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
            'limpiezaCon': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'otrosTratamientos': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'programaVersion': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'rellenoSurcos': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'tratamientoDigital': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'anarapp.tratfotopiedra': {
            'Meta': {'object_name': 'TratFotoPiedra', '_ormbases': ['anarapp.TratFoto']},
            'piedra': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TratFotoPiedra'", 'unique': 'True', 'to': "orm['anarapp.Piedra']"}),
            'tratfoto_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.TratFoto']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.ubicacioncaras': {
            'Meta': {'object_name': 'UbicacionCaras'},
            'altura': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'areasEspecificas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bocaPrincipal': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'claraboya': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lagoInterior': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'luminosidad': ('django.db.models.fields.IntegerField', [], {}),
            'otraSala': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'piedra': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'UbicacionCaras'", 'unique': 'True', 'to': "orm['anarapp.Piedra']"}),
            'requiereAndamiaje': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'salaPrincipal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'todaLaCaverna': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'anarapp.ubicacionyacimiento': {
            'Meta': {'object_name': 'UbicacionYacimiento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ubicacionManifestacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'UbicacionYacimiento'", 'to': "orm['anarapp.Yacimiento']"})
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
            'anio': ('django.db.models.fields.IntegerField', [], {}),
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'formato': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'isFromAnar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'numCopia': ('django.db.models.fields.IntegerField', [], {}),
            'numReferencia': ('django.db.models.fields.IntegerField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'anarapp.videopiedra': {
            'Meta': {'object_name': 'VideoPiedra', '_ormbases': ['anarapp.Video']},
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'VideoPiedra'", 'to': "orm['anarapp.Piedra']"}),
            'video_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Video']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.videoyacimiento': {
            'Meta': {'object_name': 'VideoYacimiento', '_ormbases': ['anarapp.Video']},
            'video_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Video']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'VideoYacimiento'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.yacimiento': {
            'Meta': {'object_name': 'Yacimiento'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['anarapp']