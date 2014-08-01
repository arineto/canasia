# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.address'
        db.add_column(u'core_project', 'address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.address'
        db.delete_column(u'core_project', 'address')


    models = {
        u'core.country': {
            'Meta': {'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'core.project': {
            'Meta': {'object_name': 'Project'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Sector']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.sector': {
            'Meta': {'object_name': 'Sector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['core']