# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EMailTemplate'
        db.create_table(u'mailtemplates_emailtemplate', (
            ('id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('sender', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('html', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'mailtemplates', ['EMailTemplate'])


    def backwards(self, orm):
        # Deleting model 'EMailTemplate'
        db.delete_table(u'mailtemplates_emailtemplate')


    models = {
        u'mailtemplates.emailtemplate': {
            'Meta': {'object_name': 'EMailTemplate'},
            'html': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128', 'primary_key': 'True'}),
            'sender': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['mailtemplates']