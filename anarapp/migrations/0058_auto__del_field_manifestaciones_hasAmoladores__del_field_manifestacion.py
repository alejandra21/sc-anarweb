# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Manifestaciones.hasAmoladores'
        db.delete_column('anarapp_manifestaciones', 'hasAmoladores')

        # Deleting field 'Manifestaciones.hasPuntosAcoplados'
        db.delete_column('anarapp_manifestaciones', 'hasPuntosAcoplados')

        # Deleting field 'Manifestaciones.hasPetroglifo'
        db.delete_column('anarapp_manifestaciones', 'hasPetroglifo')

        # Deleting field 'Manifestaciones.hasCupulas'
        db.delete_column('anarapp_manifestaciones', 'hasCupulas')

        # Deleting field 'Manifestaciones.hasPinturaRupestre'
        db.delete_column('anarapp_manifestaciones', 'hasPinturaRupestre')

        # Adding field 'Manifestaciones.tienePetroglifos'
        db.add_column('anarapp_manifestaciones', 'tienePetroglifos',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Manifestaciones.tieneRupestres'
        db.add_column('anarapp_manifestaciones', 'tieneRupestres',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Manifestaciones.tieneAmoladore'
        db.add_column('anarapp_manifestaciones', 'tieneAmoladore',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Manifestaciones.tienePuntosAc'
        db.add_column('anarapp_manifestaciones', 'tienePuntosAc',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Manifestaciones.tieneCupula'
        db.add_column('anarapp_manifestaciones', 'tieneCupula',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Manifestaciones.hasAmoladores'
        db.add_column('anarapp_manifestaciones', 'hasAmoladores',
                      self.gf('anarapp.models.CharField')(default='', max_length=65000, blank=True),
                      keep_default=False)

        # Adding field 'Manifestaciones.hasPuntosAcoplados'
        db.add_column('anarapp_manifestaciones', 'hasPuntosAcoplados',
                      self.gf('anarapp.models.CharField')(default='', max_length=65000, blank=True),
                      keep_default=False)

        # Adding field 'Manifestaciones.hasPetroglifo'
        db.add_column('anarapp_manifestaciones', 'hasPetroglifo',
                      self.gf('anarapp.models.CharField')(default='', max_length=65000, blank=True),
                      keep_default=False)

        # Adding field 'Manifestaciones.hasCupulas'
        db.add_column('anarapp_manifestaciones', 'hasCupulas',
                      self.gf('anarapp.models.CharField')(default='', max_length=65000, blank=True),
                      keep_default=False)

        # Adding field 'Manifestaciones.hasPinturaRupestre'
        db.add_column('anarapp_manifestaciones', 'hasPinturaRupestre',
                      self.gf('anarapp.models.CharField')(default='', max_length=65000, blank=True),
                      keep_default=False)

        # Deleting field 'Manifestaciones.tienePetroglifos'
        db.delete_column('anarapp_manifestaciones', 'tienePetroglifos')

        # Deleting field 'Manifestaciones.tieneRupestres'
        db.delete_column('anarapp_manifestaciones', 'tieneRupestres')

        # Deleting field 'Manifestaciones.tieneAmoladore'
        db.delete_column('anarapp_manifestaciones', 'tieneAmoladore')

        # Deleting field 'Manifestaciones.tienePuntosAc'
        db.delete_column('anarapp_manifestaciones', 'tienePuntosAc')

        # Deleting field 'Manifestaciones.tieneCupula'
        db.delete_column('anarapp_manifestaciones', 'tieneCupula')


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
            'esCantidadInexacta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'piedra': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Manifestaciones'", 'unique': 'True', 'to': "orm['anarapp.Piedra']"}),
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
            'tecnicaP': ('anarapp.models.CharField', [], {'max_length': '65000'})
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
            'anioy': ('django.db.models.fields.IntegerField', [], {}),
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
            'anioy': ('django.db.models.fields.IntegerField', [], {}),
            'archivoy': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'autory': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'formatoy': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'instituciony': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'isFromAnary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isvidyac': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'numCopiayac': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'numReferenciay': ('django.db.models.fields.IntegerField', [], {}),
            'pelicula_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Pelicula']", 'unique': 'True', 'primary_key': 'True'}),
            'tituloy': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'PeliYacimiento'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.piedra': {
            'Meta': {'object_name': 'Piedra'},
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manifiestacionAsociada': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
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
            'numReferenciay': ('django.db.models.fields.IntegerField', [], {}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'VideoPiedra'", 'to': "orm['anarapp.Piedra']"}),
            'tituloy': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'video_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Video']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.videoyacimiento': {
            'Meta': {'object_name': 'VideoYacimiento', '_ormbases': ['anarapp.Video']},
            'anioy': ('django.db.models.fields.IntegerField', [], {}),
            'archivoy': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'autory': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'formatoy': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'instituciony': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'isFromAnary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isvidyac': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'numCopiayac': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'numReferenciay': ('django.db.models.fields.IntegerField', [], {}),
            'tituloy': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'video_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Video']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'VideoYacimiento'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.yacimiento': {
            'Meta': {'object_name': 'Yacimiento'},
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'EstadoYac'", 'null': 'True', 'to': "orm['anarapp.Estado']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('smart_selects.db_fields.ChainedForeignKey', [], {'blank': 'True', 'related_name': "'MunicipioYac'", 'null': 'True', 'to': "orm['anarapp.Municipio']"}),
            'nombre': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'pais': ('anarapp.models.CharField', [], {'default': "'Venezuela'", 'max_length': '65000'})
        }
    }

    complete_apps = ['anarapp']