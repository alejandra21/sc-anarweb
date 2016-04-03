# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DimensionPiedra'
        db.create_table('anarapp_dimensionpiedra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('altoMaximo', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('largoMaximo', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('anchoMaximo', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
        ))
        db.send_create_signal('anarapp', ['DimensionPiedra'])

        # Adding model 'LlenadoPiedra'
        db.create_table('anarapp_llenadopiedra', (
            ('llenadopor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.LlenadoPor'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['LlenadoPiedra'])

        # Adding model 'Foto'
        db.create_table('anarapp_foto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('negativo', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('tipoFotografia', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('fotografo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('numReferencia', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('numRollo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('numFoto', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('numMarcaNegativo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('esDeAnar', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('numCopiaAnar', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['Foto'])

        # Adding model 'Piedra'
        db.create_table('anarapp_piedra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('manifiestacionAsociada', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('nombreFiguras', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('numeroCaras', self.gf('django.db.models.fields.IntegerField')()),
            ('numeroCarasTrajabadas', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['Piedra'])

        # Adding model 'SupervisadoPor'
        db.create_table('anarapp_supervisadopor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['SupervisadoPor'])

        # Adding model 'Observaciones'
        db.create_table('anarapp_observaciones', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('texto', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['Observaciones'])

        # Adding model 'VideoYacimiento'
        db.create_table('anarapp_videoyacimiento', (
            ('video_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Video'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['VideoYacimiento'])

        # Adding model 'Pelicula'
        db.create_table('anarapp_pelicula', (
            ('video_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Video'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['Pelicula'])

        # Adding model 'OtrosValPiedra'
        db.create_table('anarapp_otrosvalpiedra', (
            ('otrosvalores_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.OtrosValores'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['OtrosValPiedra'])

        # Adding model 'LlenadoPor'
        db.create_table('anarapp_llenadopor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('anarapp', ['LlenadoPor'])

        # Adding model 'MatAVYacimiento'
        db.create_table('anarapp_matavyacimiento', (
            ('mataudiovisual_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MatAudioVisual'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['MatAVYacimiento'])

        # Adding model 'MultimediaPiedra'
        db.create_table('anarapp_multimediapiedra', (
            ('multimedia_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Multimedia'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['MultimediaPiedra'])

        # Adding model 'Multimedia'
        db.create_table('anarapp_multimedia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tecnica', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['Multimedia'])

        # Adding model 'ObservacionesYac'
        db.create_table('anarapp_observacionesyac', (
            ('observaciones_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Observaciones'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['ObservacionesYac'])

        # Adding model 'SupervisadoYac'
        db.create_table('anarapp_supervisadoyac', (
            ('supervisadopor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.SupervisadoPor'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['SupervisadoYac'])

        # Adding model 'ObtInfoYac'
        db.create_table('anarapp_obtinfoyac', (
            ('obtencioninfo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.ObtencionInfo'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['ObtInfoYac'])

        # Adding model 'VideoPiedra'
        db.create_table('anarapp_videopiedra', (
            ('video_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Video'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['VideoPiedra'])

        # Adding model 'EscRedPiedra'
        db.create_table('anarapp_escredpiedra', (
            ('repgrafpiedra_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.RepGrafPiedra'], unique=True, primary_key=True)),
            ('tipoReproduccion', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['EscRedPiedra'])

        # Adding model 'FotoBibliografia'
        db.create_table('anarapp_fotobibliografia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('esFotografia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('escolor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esBlancoYNegro', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esDiapositiva', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esPapel', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esDigital', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('esNegativo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('tipoMapa', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['FotoBibliografia'])

        # Adding model 'PeliYacimiento'
        db.create_table('anarapp_peliyacimiento', (
            ('pelicula_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Pelicula'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['PeliYacimiento'])

        # Adding model 'ObservacPiedra'
        db.create_table('anarapp_observacpiedra', (
            ('observaciones_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Observaciones'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['ObservacPiedra'])

        # Adding model 'BibYacimiento'
        db.create_table('anarapp_bibyacimiento', (
            ('bibliografia_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Bibliografia'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['BibYacimiento'])

        # Adding model 'PeliculaPiedra'
        db.create_table('anarapp_peliculapiedra', (
            ('pelicula_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Pelicula'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['PeliculaPiedra'])

        # Adding model 'Bibliografia'
        db.create_table('anarapp_bibliografia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ano', self.gf('django.db.models.fields.IntegerField')()),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('conDibujo', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('anarapp', ['Bibliografia'])

        # Adding model 'Manifestaciones'
        db.create_table('anarapp_manifestaciones', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('tienePetroglifo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tienePinturaRupestre', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tieneAmoladores', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tienePuntosAcoplados', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tieneCupulas', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('anarapp', ['Manifestaciones'])

        # Adding model 'OtrosValYac'
        db.create_table('anarapp_otrosvalyac', (
            ('otrosvalores_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.OtrosValores'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['OtrosValYac'])

        # Adding model 'FotoBibPiedra'
        db.create_table('anarapp_fotobibpiedra', (
            ('fotobibliografia_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.FotoBibliografia'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['FotoBibPiedra'])

        # Adding model 'CaraTrabajada'
        db.create_table('anarapp_caratrabajada', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('orientacion', self.gf('django.db.models.fields.IntegerField')()),
            ('alto', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
            ('ancho', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
            ('largo', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
        ))
        db.send_create_signal('anarapp', ['CaraTrabajada'])

        # Adding model 'EsquemaPorCara'
        db.create_table('anarapp_esquemaporcara', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('textoCara', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('posicion', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['EsquemaPorCara'])

        # Adding model 'OtrosValores'
        db.create_table('anarapp_otrosvalores', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('texto', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['OtrosValores'])

        # Adding model 'EscNatPiedra'
        db.create_table('anarapp_escnatpiedra', (
            ('repgrafpiedra_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.RepGrafPiedra'], unique=True, primary_key=True)),
            ('tipoReproduccion', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['EscNatPiedra'])

        # Adding model 'ObtencionInfo'
        db.create_table('anarapp_obtencioninfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prospeccion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comunicacion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('telefonoCel', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('mail', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('paginaWeb', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('nombreFacebook', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('blog', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('verificado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('anarapp', ['ObtencionInfo'])

        # Adding model 'PaginaWebPiedra'
        db.create_table('anarapp_paginawebpiedra', (
            ('paginaweb_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.PaginaWeb'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['PaginaWebPiedra'])

        # Adding model 'MatAVPiedra'
        db.create_table('anarapp_matavpiedra', (
            ('mataudiovisual_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MatAudioVisual'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['MatAVPiedra'])

        # Adding model 'MultimediaYac'
        db.create_table('anarapp_multimediayac', (
            ('multimedia_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Multimedia'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['MultimediaYac'])

        # Adding model 'ObtInfoPiedra'
        db.create_table('anarapp_obtinfopiedra', (
            ('obtencioninfo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.ObtencionInfo'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['ObtInfoPiedra'])

        # Adding model 'SupervisadoPiedra'
        db.create_table('anarapp_supervisadopiedra', (
            ('supervisadopor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.SupervisadoPor'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['SupervisadoPiedra'])

        # Adding model 'FigurasPorTipo'
        db.create_table('anarapp_figurasportipo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('tipoFigura', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['FigurasPorTipo'])

        # Adding model 'LlenadoYac'
        db.create_table('anarapp_llenadoyac', (
            ('llenadopor_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.LlenadoPor'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['LlenadoYac'])

        # Adding model 'TratFoto'
        db.create_table('anarapp_tratfoto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('limpiezaCon', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('rellenoSurcos', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('tratamientoDigital', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('programaVersion', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('otrosTratamientos', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['TratFoto'])

        # Adding model 'PaginaWeb'
        db.create_table('anarapp_paginaweb', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('direccionURL', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('anarapp', ['PaginaWeb'])

        # Adding model 'PaginaWebYac'
        db.create_table('anarapp_paginawebyac', (
            ('paginaweb_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.PaginaWeb'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['PaginaWebYac'])

        # Adding model 'UbicacionCaras'
        db.create_table('anarapp_ubicacioncaras', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('todaLaCaverna', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('areasEspecificas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('salaPrincipal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otraSala', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('lagoInterior', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('claraboya', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bocaPrincipal', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('luminosidad', self.gf('django.db.models.fields.IntegerField')()),
            ('altura', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
            ('requiereAndamiaje', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('anarapp', ['UbicacionCaras'])

        # Adding model 'TratFotoPiedra'
        db.create_table('anarapp_tratfotopiedra', (
            ('tratfoto_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.TratFoto'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['TratFotoPiedra'])

        # Adding model 'MatAudioVisual'
        db.create_table('anarapp_mataudiovisual', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('formato', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('imagen', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
        ))
        db.send_create_signal('anarapp', ['MatAudioVisual'])

        # Adding model 'FotoBibYac'
        db.create_table('anarapp_fotobibyac', (
            ('fotobibliografia_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.FotoBibliografia'], unique=True, primary_key=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
        ))
        db.send_create_signal('anarapp', ['FotoBibYac'])

        # Adding model 'ConexionFiguras'
        db.create_table('anarapp_conexionfiguras', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('conexionFiguras', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['ConexionFiguras'])

        # Adding model 'RepGrafPiedra'
        db.create_table('anarapp_repgrafpiedra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('numPiezas', self.gf('django.db.models.fields.IntegerField')()),
            ('instituto', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('persona', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('anarapp', ['RepGrafPiedra'])

        # Adding model 'FotoPiedra'
        db.create_table('anarapp_fotopiedra', (
            ('foto_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Foto'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['FotoPiedra'])

        # Adding model 'BibPiedra'
        db.create_table('anarapp_bibpiedra', (
            ('bibliografia_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Bibliografia'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['BibPiedra'])

        # Adding model 'Video'
        db.create_table('anarapp_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('anio', self.gf('django.db.models.fields.IntegerField')()),
            ('formato', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('numReferencia', self.gf('django.db.models.fields.IntegerField')()),
            ('isFromAnar', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('numCopia', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['Video'])


    def backwards(self, orm):
        # Deleting model 'DimensionPiedra'
        db.delete_table('anarapp_dimensionpiedra')

        # Deleting model 'LlenadoPiedra'
        db.delete_table('anarapp_llenadopiedra')

        # Deleting model 'Foto'
        db.delete_table('anarapp_foto')

        # Deleting model 'Piedra'
        db.delete_table('anarapp_piedra')

        # Deleting model 'SupervisadoPor'
        db.delete_table('anarapp_supervisadopor')

        # Deleting model 'Observaciones'
        db.delete_table('anarapp_observaciones')

        # Deleting model 'VideoYacimiento'
        db.delete_table('anarapp_videoyacimiento')

        # Deleting model 'Pelicula'
        db.delete_table('anarapp_pelicula')

        # Deleting model 'OtrosValPiedra'
        db.delete_table('anarapp_otrosvalpiedra')

        # Deleting model 'LlenadoPor'
        db.delete_table('anarapp_llenadopor')

        # Deleting model 'MatAVYacimiento'
        db.delete_table('anarapp_matavyacimiento')

        # Deleting model 'MultimediaPiedra'
        db.delete_table('anarapp_multimediapiedra')

        # Deleting model 'Multimedia'
        db.delete_table('anarapp_multimedia')

        # Deleting model 'ObservacionesYac'
        db.delete_table('anarapp_observacionesyac')

        # Deleting model 'SupervisadoYac'
        db.delete_table('anarapp_supervisadoyac')

        # Deleting model 'ObtInfoYac'
        db.delete_table('anarapp_obtinfoyac')

        # Deleting model 'VideoPiedra'
        db.delete_table('anarapp_videopiedra')

        # Deleting model 'EscRedPiedra'
        db.delete_table('anarapp_escredpiedra')

        # Deleting model 'FotoBibliografia'
        db.delete_table('anarapp_fotobibliografia')

        # Deleting model 'PeliYacimiento'
        db.delete_table('anarapp_peliyacimiento')

        # Deleting model 'ObservacPiedra'
        db.delete_table('anarapp_observacpiedra')

        # Deleting model 'BibYacimiento'
        db.delete_table('anarapp_bibyacimiento')

        # Deleting model 'PeliculaPiedra'
        db.delete_table('anarapp_peliculapiedra')

        # Deleting model 'Bibliografia'
        db.delete_table('anarapp_bibliografia')

        # Deleting model 'Manifestaciones'
        db.delete_table('anarapp_manifestaciones')

        # Deleting model 'OtrosValYac'
        db.delete_table('anarapp_otrosvalyac')

        # Deleting model 'FotoBibPiedra'
        db.delete_table('anarapp_fotobibpiedra')

        # Deleting model 'CaraTrabajada'
        db.delete_table('anarapp_caratrabajada')

        # Deleting model 'EsquemaPorCara'
        db.delete_table('anarapp_esquemaporcara')

        # Deleting model 'OtrosValores'
        db.delete_table('anarapp_otrosvalores')

        # Deleting model 'EscNatPiedra'
        db.delete_table('anarapp_escnatpiedra')

        # Deleting model 'ObtencionInfo'
        db.delete_table('anarapp_obtencioninfo')

        # Deleting model 'PaginaWebPiedra'
        db.delete_table('anarapp_paginawebpiedra')

        # Deleting model 'MatAVPiedra'
        db.delete_table('anarapp_matavpiedra')

        # Deleting model 'MultimediaYac'
        db.delete_table('anarapp_multimediayac')

        # Deleting model 'ObtInfoPiedra'
        db.delete_table('anarapp_obtinfopiedra')

        # Deleting model 'SupervisadoPiedra'
        db.delete_table('anarapp_supervisadopiedra')

        # Deleting model 'FigurasPorTipo'
        db.delete_table('anarapp_figurasportipo')

        # Deleting model 'LlenadoYac'
        db.delete_table('anarapp_llenadoyac')

        # Deleting model 'TratFoto'
        db.delete_table('anarapp_tratfoto')

        # Deleting model 'PaginaWeb'
        db.delete_table('anarapp_paginaweb')

        # Deleting model 'PaginaWebYac'
        db.delete_table('anarapp_paginawebyac')

        # Deleting model 'UbicacionCaras'
        db.delete_table('anarapp_ubicacioncaras')

        # Deleting model 'TratFotoPiedra'
        db.delete_table('anarapp_tratfotopiedra')

        # Deleting model 'MatAudioVisual'
        db.delete_table('anarapp_mataudiovisual')

        # Deleting model 'FotoBibYac'
        db.delete_table('anarapp_fotobibyac')

        # Deleting model 'ConexionFiguras'
        db.delete_table('anarapp_conexionfiguras')

        # Deleting model 'RepGrafPiedra'
        db.delete_table('anarapp_repgrafpiedra')

        # Deleting model 'FotoPiedra'
        db.delete_table('anarapp_fotopiedra')

        # Deleting model 'BibPiedra'
        db.delete_table('anarapp_bibpiedra')

        # Deleting model 'Video'
        db.delete_table('anarapp_video')


    models = {
        'anarapp.altitud': {
            'Meta': {'object_name': 'Altitud'},
            'altura': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'superficie': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
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
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.bibyacimiento': {
            'Meta': {'object_name': 'BibYacimiento', '_ormbases': ['anarapp.Bibliografia']},
            'bibliografia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Bibliografia']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
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
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Yacimiento']", 'unique': 'True'})
        },
        'anarapp.caracdolmenart': {
            'ConPetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Meta': {'object_name': 'CaracDolmenArt'},
            'cantidadConPetroglifo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cantidadConPinturas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'conPinturas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notas': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Yacimiento']", 'unique': 'True'})
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
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Yacimiento']", 'unique': 'True'})
        },
        'anarapp.caracmonolitos': {
            'Meta': {'object_name': 'CaracMonolitos'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cantidadConGrabados': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'esPinturaRupestre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Yacimiento']", 'unique': 'True'})
        },
        'anarapp.caracsurcoamoladores': {
            'Meta': {'object_name': 'CaracSurcoAmoladores'},
            'ancho': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'diametro': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcobateas': {
            'Meta': {'object_name': 'CaracSurcoBateas'},
            'ancho': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcocupulas': {
            'Meta': {'object_name': 'CaracSurcoCupulas'},
            'ancho': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'diametro': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcomortero': {
            'Meta': {'object_name': 'CaracSurcoMortero'},
            'ancho': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
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
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcopuntosacopl': {
            'Meta': {'object_name': 'CaracSurcoPuntosAcopl'},
            'esPunteado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Yacimiento']", 'unique': 'True'})
        },
        'anarapp.caratrabajada': {
            'Meta': {'object_name': 'CaraTrabajada'},
            'alto': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'ancho': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'orientacion': ('django.db.models.fields.IntegerField', [], {}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.conexionfiguras': {
            'Meta': {'object_name': 'ConexionFiguras'},
            'conexionFiguras': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.considertemp': {
            'Meta': {'object_name': 'ConsiderTemp'},
            'cincoAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Yacimiento']", 'unique': 'True'})
        },
        'anarapp.constitucionyacimiento': {
            'Meta': {'object_name': 'ConstitucionYacimiento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nroPiedras': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nroPiedrasColocadas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nroPiedrasGrabadas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nroPiedrasPintadas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.coordenadas': {
            'Meta': {'object_name': 'Coordenadas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
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
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.croquis': {
            'Meta': {'object_name': 'Croquis'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'urlImagen': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.datum': {
            'Meta': {'object_name': 'Datum'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipoDatum': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.dimensionpiedra': {
            'Meta': {'object_name': 'DimensionPiedra'},
            'altoMaximo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'anchoMaximo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largoMaximo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
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
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
            'posicion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
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
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Yacimiento']", 'unique': 'True'})
        },
        'anarapp.faunayacimiento': {
            'Meta': {'object_name': 'FaunaYacimiento'},
            'fauna': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.figurasportipo': {
            'Meta': {'object_name': 'FigurasPorTipo'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
            'tipoFigura': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.florayacimiento': {
            'Meta': {'object_name': 'FloraYacimiento'},
            'flora': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
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
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.fotobibyac': {
            'Meta': {'object_name': 'FotoBibYac', '_ormbases': ['anarapp.FotoBibliografia']},
            'fotobibliografia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.FotoBibliografia']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.fotografiayac': {
            'Meta': {'object_name': 'FotografiaYac'},
            'esAerea': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esSatelital': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noEsAerea': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'urlImagen': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.fotopiedra': {
            'Meta': {'object_name': 'FotoPiedra', '_ormbases': ['anarapp.Foto']},
            'foto_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Foto']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
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
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.indicaciones': {
            'Meta': {'object_name': 'Indicaciones'},
            'direcciones': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puntoDatum': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.llenadopiedra': {
            'Meta': {'object_name': 'LlenadoPiedra', '_ormbases': ['anarapp.LlenadoPor']},
            'llenadopor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.LlenadoPor']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
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
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
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
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.manifestaciones': {
            'Meta': {'object_name': 'Manifestaciones'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
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
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Yacimiento']", 'unique': 'True'})
        },
        'anarapp.manifestubicacionyacimiento': {
            'Meta': {'object_name': 'ManifestUbicacionYacimiento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipoManifestacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ubicacionManifestacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'manifestacion'", 'to': "orm['anarapp.Yacimiento']"})
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
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.matavyacimiento': {
            'Meta': {'object_name': 'MatAVYacimiento', '_ormbases': ['anarapp.MatAudioVisual']},
            'mataudiovisual_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MatAudioVisual']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
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
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.multimedia': {
            'Meta': {'object_name': 'Multimedia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tecnica': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'anarapp.multimediapiedra': {
            'Meta': {'object_name': 'MultimediaPiedra', '_ormbases': ['anarapp.Multimedia']},
            'multimedia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Multimedia']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.multimediayac': {
            'Meta': {'object_name': 'MultimediaYac', '_ormbases': ['anarapp.Multimedia']},
            'multimedia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Multimedia']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.observaciones': {
            'Meta': {'object_name': 'Observaciones'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texto': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'anarapp.observacionesyac': {
            'Meta': {'object_name': 'ObservacionesYac', '_ormbases': ['anarapp.Observaciones']},
            'observaciones_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Observaciones']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.observacpiedra': {
            'Meta': {'object_name': 'ObservacPiedra', '_ormbases': ['anarapp.Observaciones']},
            'observaciones_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Observaciones']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
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
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.obtinfoyac': {
            'Meta': {'object_name': 'ObtInfoYac', '_ormbases': ['anarapp.ObtencionInfo']},
            'obtencioninfo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.ObtencionInfo']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
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
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.otrosvalores': {
            'Meta': {'object_name': 'OtrosValores'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texto': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'anarapp.otrosvalpiedra': {
            'Meta': {'object_name': 'OtrosValPiedra', '_ormbases': ['anarapp.OtrosValores']},
            'otrosvalores_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.OtrosValores']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.otrosvalyac': {
            'Meta': {'object_name': 'OtrosValYac', '_ormbases': ['anarapp.OtrosValores']},
            'otrosvalores_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.OtrosValores']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.paginaweb': {
            'Meta': {'object_name': 'PaginaWeb'},
            'direccionURL': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'anarapp.paginawebpiedra': {
            'Meta': {'object_name': 'PaginaWebPiedra', '_ormbases': ['anarapp.PaginaWeb']},
            'paginaweb_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.PaginaWeb']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.paginawebyac': {
            'Meta': {'object_name': 'PaginaWebYac', '_ormbases': ['anarapp.PaginaWeb']},
            'paginaweb_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.PaginaWeb']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.pelicula': {
            'Meta': {'object_name': 'Pelicula', '_ormbases': ['anarapp.Video']},
            'video_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Video']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.peliculapiedra': {
            'Meta': {'object_name': 'PeliculaPiedra', '_ormbases': ['anarapp.Pelicula']},
            'pelicula_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Pelicula']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.peliyacimiento': {
            'Meta': {'object_name': 'PeliYacimiento', '_ormbases': ['anarapp.Pelicula']},
            'pelicula_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Pelicula']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
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
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.plano': {
            'Meta': {'object_name': 'Plano'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numeroPlano': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.repgrafpiedra': {
            'Meta': {'object_name': 'RepGrafPiedra'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instituto': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'numPiezas': ('django.db.models.fields.IntegerField', [], {}),
            'persona': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.supervisadopiedra': {
            'Meta': {'object_name': 'SupervisadoPiedra', '_ormbases': ['anarapp.SupervisadoPor']},
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
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
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tecnicaparageoglifo': {
            'Meta': {'object_name': 'TecnicaParaGeoglifo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tecnicas': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
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
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tecnicaparamonumentos': {
            'Meta': {'object_name': 'TecnicaParaMonumentos'},
            'esDolmen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMenhir': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMonolito': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'tecnicas': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
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
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tecnicaparapintura': {
            'Meta': {'object_name': 'TecnicaParaPintura'},
            'conDedo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fibra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'soplado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
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
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.texturasuelo': {
            'Meta': {'object_name': 'TexturaSuelo'},
            'esArcilloso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esArenoso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPedregoso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esRocaMadre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mixto': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tipoexposicionyac': {
            'Meta': {'object_name': 'TipoExposicionYac'},
            'expuesto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'expuestoPeriodicamente': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observaciones': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
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
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
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
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
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
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
            'requiereAndamiaje': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'salaPrincipal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'todaLaCaverna': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
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
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Piedra']"}),
            'video_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Video']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.videoyacimiento': {
            'Meta': {'object_name': 'VideoYacimiento', '_ormbases': ['anarapp.Video']},
            'video_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Video']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anarapp.Yacimiento']"})
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