# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CustomUser'
        db.create_table(u'backend_customuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email_addr', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=30, db_index=True)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_logged_in', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'backend', ['CustomUser'])

        # Adding model 'Supplier'
        db.create_table(u'backend_supplier', (
            (u'customuser_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['backend.CustomUser'], unique=True, primary_key=True)),
            ('company_name', self.gf('django.db.models.fields.CharField')(default='', max_length=128, db_index=True, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'backend', ['Supplier'])

        # Adding model 'Designer'
        db.create_table(u'backend_designer', (
            (u'customuser_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['backend.CustomUser'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'backend', ['Designer'])

        # Adding model 'Item'
        db.create_table(u'backend_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Supplier'])),
            ('image1_url', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('image2_url', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('image3_url', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('image4_url', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('image5_url', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('product_name', self.gf('django.db.models.fields.CharField')(default='', max_length=128, blank=True)),
            ('product_code', self.gf('django.db.models.fields.CharField')(default='', max_length=128, blank=True)),
            ('in_stock', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('lead_time', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('wholesale_price', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('wholesale_price_units', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('volume_discount', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('fabric_width', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('fabric_width_units', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('material_type', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('fiber_type', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('textile_type', self.gf('django.db.models.fields.CharField')(default='', max_length=512, blank=True)),
            ('weave_type', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=512, blank=True)),
            ('weight', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('color', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('dying', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('color_fast_testing', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('country_origin', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('sustainability', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('cost', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('time_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'backend', ['Item'])

        # Adding model 'PhotoUrl'
        db.create_table(u'backend_photourl', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('uploaded', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'backend', ['PhotoUrl'])


    def backwards(self, orm):
        # Deleting model 'CustomUser'
        db.delete_table(u'backend_customuser')

        # Deleting model 'Supplier'
        db.delete_table(u'backend_supplier')

        # Deleting model 'Designer'
        db.delete_table(u'backend_designer')

        # Deleting model 'Item'
        db.delete_table(u'backend_item')

        # Deleting model 'PhotoUrl'
        db.delete_table(u'backend_photourl')


    models = {
        u'backend.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'email_addr': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '30', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_logged_in': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'backend.designer': {
            'Meta': {'object_name': 'Designer', '_ormbases': [u'backend.CustomUser']},
            u'customuser_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['backend.CustomUser']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'backend.item': {
            'Meta': {'object_name': 'Item'},
            'color': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'color_fast_testing': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'cost': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'country_origin': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '512', 'blank': 'True'}),
            'dying': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'fabric_width': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'fabric_width_units': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'fiber_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image1_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'image2_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'image3_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'image4_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'image5_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'in_stock': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lead_time': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'material_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'product_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'product_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.Supplier']"}),
            'sustainability': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'textile_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '512', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'time_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'volume_discount': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'weave_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'weight': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'wholesale_price': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'wholesale_price_units': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'})
        },
        u'backend.photourl': {
            'Meta': {'object_name': 'PhotoUrl'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uploaded': ('django.db.models.fields.DateTimeField', [], {}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'backend.supplier': {
            'Meta': {'object_name': 'Supplier', '_ormbases': [u'backend.CustomUser']},
            'company_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'db_index': 'True', 'blank': 'True'}),
            u'customuser_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['backend.CustomUser']", 'unique': 'True', 'primary_key': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['backend']