# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Bibliografia'
        db.delete_table('anarapp_bibliografia')

        # Deleting model 'LlenadaPor'
        db.delete_table('anarapp_llenadapor')

        # Deleting model 'PaginaWEB'
        db.delete_table('anarapp_paginaweb')

        # Deleting model 'MaterialApoyo'
        db.delete_table('anarapp_materialapoyo')

        # Deleting model 'FotografiaBibliografia'
        db.delete_table('anarapp_fotografiabibliografia')

        # Deleting model 'DimensionPiedra'
        db.delete_table('anarapp_dimensionpiedra')

        # Deleting model 'ComunicacionPersonalPiedras'
        db.delete_table('anarapp_comunicacionpersonalpiedras')

        # Deleting model 'MecObtInformacion'
        db.delete_table('anarapp_mecobtinformacion')

        # Deleting model 'Piedra'
        db.delete_table('anarapp_piedra')

        # Deleting model 'MatAudiovisual'
        db.delete_table('anarapp_mataudiovisual')

        # Deleting model 'ReproGraf'
        db.delete_table('anarapp_reprograf')

        # Deleting model 'ImagenReproGraf'
        db.delete_table('anarapp_imagenreprograf')

        # Deleting model 'VideoPiedra'
        db.delete_table('anarapp_videopiedra')

        # Deleting model 'PeliculaPiedra'
        db.delete_table('anarapp_peliculapiedra')

        # Deleting model 'SupervisadaPor'
        db.delete_table('anarapp_supervisadapor')

        # Deleting model 'Pelicula'
        db.delete_table('anarapp_pelicula')

        # Deleting model 'FotografiaPiedra'
        db.delete_table('anarapp_fotografiapiedra')

        # Deleting model 'RecursoMultimedia'
        db.delete_table('anarapp_recursomultimedia')

        # Deleting model 'TratFotografia'
        db.delete_table('anarapp_tratfotografia')

        # Deleting model 'ReproGrafEscalaNaturalPiedra'
        db.delete_table('anarapp_reprografescalanaturalpiedra')

        # Deleting model 'ObtenidaPor'
        db.delete_table('anarapp_obtenidapor')

        # Deleting model 'MapaBibliografia'
        db.delete_table('anarapp_mapabibliografia')

        # Deleting model 'BibPiedra'
        db.delete_table('anarapp_bibpiedra')

        # Deleting model 'OtrosValoresSitio'
        db.delete_table('anarapp_otrosvaloressitio')

        # Deleting model 'ReproGrafEscalaNatural'
        db.delete_table('anarapp_reprografescalanatural')

        # Deleting model 'VerificadoEnPiedra'
        db.delete_table('anarapp_verificadoenpiedra')

        # Deleting model 'ReproGrafEscalaRedPied'
        db.delete_table('anarapp_reprografescalaredpied')

        # Deleting model 'Grabacion'
        db.delete_table('anarapp_grabacion')

        # Deleting model 'ProspSistPiedra'
        db.delete_table('anarapp_prospsistpiedra')

        # Deleting model 'ConjFiguraPorTipo'
        db.delete_table('anarapp_conjfiguraportipo')

        # Deleting model 'ReproGrafEscalaRed'
        db.delete_table('anarapp_reprografescalared')

        # Deleting model 'Video'
        db.delete_table('anarapp_video')

        # Deleting model 'Observacion'
        db.delete_table('anarapp_observacion')

        # Deleting model 'CaraTrabajada'
        db.delete_table('anarapp_caratrabajada')


    def backwards(self, orm):
        # Adding model 'Bibliografia'
        db.create_table('anarapp_bibliografia', (
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('conDibujo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('ano', self.gf('django.db.models.fields.IntegerField')()),
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['Bibliografia'])

        # Adding model 'LlenadaPor'
        db.create_table('anarapp_llenadapor', (
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['LlenadaPor'])

        # Adding model 'PaginaWEB'
        db.create_table('anarapp_paginaweb', (
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('direccionURL', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['PaginaWEB'])

        # Adding model 'MaterialApoyo'
        db.create_table('anarapp_materialapoyo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['MaterialApoyo'])

        # Adding model 'FotografiaBibliografia'
        db.create_table('anarapp_fotografiabibliografia', (
            ('bibliografia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Bibliografia'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['FotografiaBibliografia'])

        # Adding model 'DimensionPiedra'
        db.create_table('anarapp_dimensionpiedra', (
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('anchoMaximo', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('altoMaximo', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('largoMaximo', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['DimensionPiedra'])

        # Adding model 'ComunicacionPersonalPiedras'
        db.create_table('anarapp_comunicacionpersonalpiedras', (
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('telefonoCel', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('paginaWeb', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('direccionEmail', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('blog', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('mecobtinformacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MecObtInformacion'], unique=True, primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('nombreFacebook', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('anarapp', ['ComunicacionPersonalPiedras'])

        # Adding model 'MecObtInformacion'
        db.create_table('anarapp_mecobtinformacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['MecObtInformacion'])

        # Adding model 'Piedra'
        db.create_table('anarapp_piedra', (
            ('otrosValoresDeLaPiedra', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('supervisorFicha', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('numeroCarasTrajabadas', self.gf('django.db.models.fields.IntegerField')()),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
            ('fechaSupervisionFicha', self.gf('django.db.models.fields.DateField')()),
            ('numeroCaras', self.gf('django.db.models.fields.IntegerField')()),
            ('nombreFiguras', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('observaciones', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('fechaEscrituraFicha', self.gf('django.db.models.fields.DateField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('revisoFicha', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('autorFicha', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('manifiestacionAsociada', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('anarapp', ['Piedra'])

        # Adding model 'MatAudiovisual'
        db.create_table('anarapp_mataudiovisual', (
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
            ('formato', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('imagen', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('anarapp', ['MatAudiovisual'])

        # Adding model 'ReproGraf'
        db.create_table('anarapp_reprograf', (
            ('numPiezas', self.gf('django.db.models.fields.IntegerField')()),
            ('instituto', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
            ('persona', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('anarapp', ['ReproGraf'])

        # Adding model 'ImagenReproGraf'
        db.create_table('anarapp_imagenreprograf', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reproduccionGrafica', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.ReproGraf'])),
        ))
        db.send_create_signal('anarapp', ['ImagenReproGraf'])

        # Adding model 'VideoPiedra'
        db.create_table('anarapp_videopiedra', (
            ('grabacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Grabacion'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['VideoPiedra'])

        # Adding model 'PeliculaPiedra'
        db.create_table('anarapp_peliculapiedra', (
            ('grabacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Grabacion'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['PeliculaPiedra'])

        # Adding model 'SupervisadaPor'
        db.create_table('anarapp_supervisadapor', (
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['SupervisadaPor'])

        # Adding model 'Pelicula'
        db.create_table('anarapp_pelicula', (
            ('grabacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Grabacion'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['Pelicula'])

        # Adding model 'FotografiaPiedra'
        db.create_table('anarapp_fotografiapiedra', (
            ('tipoFotografia', self.gf('django.db.models.fields.IntegerField')()),
            ('numMarcaNegativo', self.gf('django.db.models.fields.IntegerField')()),
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('numReferencia', self.gf('django.db.models.fields.IntegerField')()),
            ('fotografo', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('numCopiaAnar', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('esDeAnar', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('numRollo', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['FotografiaPiedra'])

        # Adding model 'RecursoMultimedia'
        db.create_table('anarapp_recursomultimedia', (
            ('tecnica', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('imagen', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['RecursoMultimedia'])

        # Adding model 'TratFotografia'
        db.create_table('anarapp_tratfotografia', (
            ('tratamientoDigital', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('otrosTratamientosFotografia', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('rellenoSurcos', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('programaVersion', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('limpiezaCon', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['TratFotografia'])

        # Adding model 'ReproGrafEscalaNaturalPiedra'
        db.create_table('anarapp_reprografescalanaturalpiedra', (
            ('reprograf_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.ReproGraf'], unique=True, primary_key=True)),
            ('tipoReproduccion', self.gf('django.db.models.fields.IntegerField')()),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['ReproGrafEscalaNaturalPiedra'])

        # Adding model 'ObtenidaPor'
        db.create_table('anarapp_obtenidapor', (
            ('verificadoEnCampo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('porProspeccion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Yacimiento'])),
            ('fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('blog', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('porComunicacion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mail', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sitioweb', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('anarapp', ['ObtenidaPor'])

        # Adding model 'MapaBibliografia'
        db.create_table('anarapp_mapabibliografia', (
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('bibliografia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Bibliografia'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipoMapa', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['MapaBibliografia'])

        # Adding model 'BibPiedra'
        db.create_table('anarapp_bibpiedra', (
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('conDibujo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('ano', self.gf('django.db.models.fields.IntegerField')()),
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['BibPiedra'])

        # Adding model 'OtrosValoresSitio'
        db.create_table('anarapp_otrosvaloressitio', (
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Yacimiento'], unique=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('valores', self.gf('django.db.models.fields.CharField')(max_length=1200, blank=True)),
        ))
        db.send_create_signal('anarapp', ['OtrosValoresSitio'])

        # Adding model 'ReproGrafEscalaNatural'
        db.create_table('anarapp_reprografescalanatural', (
            ('reprograf_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.ReproGraf'], unique=True, primary_key=True)),
            ('tipoReproduccion', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['ReproGrafEscalaNatural'])

        # Adding model 'VerificadoEnPiedra'
        db.create_table('anarapp_verificadoenpiedra', (
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('mecobtinformacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MecObtInformacion'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['VerificadoEnPiedra'])

        # Adding model 'ReproGrafEscalaRedPied'
        db.create_table('anarapp_reprografescalaredpied', (
            ('reprograf_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.ReproGraf'], unique=True, primary_key=True)),
            ('tipoReproduccion', self.gf('django.db.models.fields.IntegerField')()),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
        ))
        db.send_create_signal('anarapp', ['ReproGrafEscalaRedPied'])

        # Adding model 'Grabacion'
        db.create_table('anarapp_grabacion', (
            ('videos', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('ano', self.gf('django.db.models.fields.IntegerField')()),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('numReferencia', self.gf('django.db.models.fields.IntegerField')()),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('formato', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('materialapoyo_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MaterialApoyo'], unique=True, primary_key=True)),
            ('isFromAnar', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('numCopia', self.gf('django.db.models.fields.IntegerField')()),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('anarapp', ['Grabacion'])

        # Adding model 'ProspSistPiedra'
        db.create_table('anarapp_prospsistpiedra', (
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('mecobtinformacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.MecObtInformacion'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['ProspSistPiedra'])

        # Adding model 'ConjFiguraPorTipo'
        db.create_table('anarapp_conjfiguraportipo', (
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('tipoFigura', self.gf('django.db.models.fields.IntegerField')()),
            ('seccion', self.gf('django.db.models.fields.IntegerField')()),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('cara', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.CaraTrabajada'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['ConjFiguraPorTipo'])

        # Adding model 'ReproGrafEscalaRed'
        db.create_table('anarapp_reprografescalared', (
            ('reprograf_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.ReproGraf'], unique=True, primary_key=True)),
            ('tipoReproduccion', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('anarapp', ['ReproGrafEscalaRed'])

        # Adding model 'Video'
        db.create_table('anarapp_video', (
            ('grabacion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Grabacion'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['Video'])

        # Adding model 'Observacion'
        db.create_table('anarapp_observacion', (
            ('observaciones', self.gf('django.db.models.fields.CharField')(max_length=1200, blank=True)),
            ('yacimiento', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anarapp.Yacimiento'], unique=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('anarapp', ['Observacion'])

        # Adding model 'CaraTrabajada'
        db.create_table('anarapp_caratrabajada', (
            ('luminosidad', self.gf('django.db.models.fields.IntegerField')()),
            ('tienePetroglifo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ubicadaEnOtraSala', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ubicadaEnTodaLaCaverna', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tieneCupulas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ubicadaEnClaraboya', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('orientacionDeLaCara', self.gf('django.db.models.fields.IntegerField')()),
            ('piedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anarapp.Piedra'])),
            ('conexionFiguras', self.gf('django.db.models.fields.IntegerField')()),
            ('tienePuntosAcoplados', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ancho', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
            ('ubicadaEnSalaPrincipal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tieneAmoladores', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('alto', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
            ('requiereAndamiaje', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ubicadaEnLagoInterior', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('distanciaBocaPrincipal', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('largo', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
            ('tienePinturaRupestre', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('altura', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
        ))
        db.send_create_signal('anarapp', ['CaraTrabajada'])


    models = {
        'anarapp.altitud': {
            'Meta': {'object_name': 'Altitud'},
            'altura': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'superficie': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
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
        'anarapp.florayacimiento': {
            'Meta': {'object_name': 'FloraYacimiento'},
            'flora': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
        'anarapp.plano': {
            'Meta': {'object_name': 'Plano'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numeroPlano': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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