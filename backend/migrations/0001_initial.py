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
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=254)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('last_logged_in', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'backend', ['CustomUser'])

        # Adding M2M table for field groups on 'CustomUser'
        m2m_table_name = db.shorten_name(u'backend_customuser_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customuser', models.ForeignKey(orm[u'backend.customuser'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customuser_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'CustomUser'
        m2m_table_name = db.shorten_name(u'backend_customuser_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customuser', models.ForeignKey(orm[u'backend.customuser'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customuser_id', 'permission_id'])

        # Adding model 'Supplier'
        db.create_table(u'backend_supplier', (
            (u'customuser_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['backend.CustomUser'], unique=True, primary_key=True)),
            ('company_name', self.gf('django.db.models.fields.CharField')(default='', max_length=128, db_index=True, blank=True)),
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
            ('in_stock', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('price_on_request', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('made_to_order', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('lead_time', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2)),
            ('wholesale_price', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2)),
            ('wholesale_price_units', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('volume_discount', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('fabric_width', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=5)),
            ('fabric_width_units', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('material_type', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('fiber_type', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('textile_type', self.gf('django.db.models.fields.CharField')(default='', max_length=512, blank=True)),
            ('weave_type', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=512, blank=True)),
            ('weight', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('color', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('dyeing', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('color_fast_testing', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('country_origin', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
            ('sustainability', self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True)),
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

        # Removing M2M table for field groups on 'CustomUser'
        db.delete_table(db.shorten_name(u'backend_customuser_groups'))

        # Removing M2M table for field user_permissions on 'CustomUser'
        db.delete_table(db.shorten_name(u'backend_customuser_user_permissions'))

        # Deleting model 'Supplier'
        db.delete_table(u'backend_supplier')

        # Deleting model 'Designer'
        db.delete_table(u'backend_designer')

        # Deleting model 'Item'
        db.delete_table(u'backend_item')

        # Deleting model 'PhotoUrl'
        db.delete_table(u'backend_photourl')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'backend.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_logged_in': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'backend.designer': {
            'Meta': {'object_name': 'Designer', '_ormbases': [u'backend.CustomUser']},
            u'customuser_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['backend.CustomUser']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'backend.item': {
            'Meta': {'object_name': 'Item'},
            'color': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'color_fast_testing': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
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
            'lead_time': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
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
            u'customuser_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['backend.CustomUser']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['backend']