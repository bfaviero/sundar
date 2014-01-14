# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Item.dying'
        db.delete_column(u'backend_item', 'dying')

        # Adding field 'Item.price_on_request'
        db.add_column(u'backend_item', 'price_on_request',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Item.made_to_order'
        db.add_column(u'backend_item', 'made_to_order',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Item.dyeing'
        db.add_column(u'backend_item', 'dyeing',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)


        # Changing field 'Item.wholesale_price'
        db.alter_column(u'backend_item', 'wholesale_price', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2))

        # Changing field 'Item.cost'
        db.alter_column(u'backend_item', 'cost', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2))

        # Changing field 'Item.fabric_width'
        db.alter_column(u'backend_item', 'fabric_width', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=5))

    def backwards(self, orm):
        # Adding field 'Item.dying'
        db.add_column(u'backend_item', 'dying',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Deleting field 'Item.price_on_request'
        db.delete_column(u'backend_item', 'price_on_request')

        # Deleting field 'Item.made_to_order'
        db.delete_column(u'backend_item', 'made_to_order')

        # Deleting field 'Item.dyeing'
        db.delete_column(u'backend_item', 'dyeing')


        # Changing field 'Item.wholesale_price'
        db.alter_column(u'backend_item', 'wholesale_price', self.gf('django.db.models.fields.CharField')(max_length=32))

        # Changing field 'Item.cost'
        db.alter_column(u'backend_item', 'cost', self.gf('django.db.models.fields.CharField')(max_length=32))

        # Changing field 'Item.fabric_width'
        db.alter_column(u'backend_item', 'fabric_width', self.gf('django.db.models.fields.CharField')(max_length=32))

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
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'country_origin': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '512', 'blank': 'True'}),
            'dyeing': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'fabric_width': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '5'}),
            'fabric_width_units': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'fiber_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image1_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'image2_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'image3_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'image4_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'image5_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'in_stock': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'lead_time': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'made_to_order': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'material_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'price_on_request': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'wholesale_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
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