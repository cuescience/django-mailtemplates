# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field notifications on 'EMailTemplate'
        m2m_table_name = db.shorten_name(u'mailtemplates_emailtemplate_notifications')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_emailtemplate', models.ForeignKey(orm[u'mailtemplates.emailtemplate'], null=False)),
            ('to_emailtemplate', models.ForeignKey(orm[u'mailtemplates.emailtemplate'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_emailtemplate_id', 'to_emailtemplate_id'])


    def backwards(self, orm):
        # Removing M2M table for field notifications on 'EMailTemplate'
        db.delete_table(db.shorten_name(u'mailtemplates_emailtemplate_notifications'))


    models = {
        u'mailtemplates.emailtemplate': {
            'Meta': {'object_name': 'EMailTemplate'},
            'html': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128', 'primary_key': 'True'}),
            'notifications': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'notificated_by'", 'symmetrical': 'False', 'to': u"orm['mailtemplates.EMailTemplate']"}),
            'sender': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['mailtemplates']