# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'contact_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('title_contact', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('title_research', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('research_interest', self.gf('django.db.models.fields.TextField')(max_length=200)),
        ))
        db.send_create_signal(u'contact', ['Contact'])

        # Adding model 'Supervisor'
        db.create_table(u'contact_supervisor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contact.Contact'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('display_order', self.gf('django.db.models.fields.IntegerField')()),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('field', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('university', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('image_path', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('research_interest', self.gf('django.db.models.fields.TextField')(max_length=200)),
        ))
        db.send_create_signal(u'contact', ['Supervisor'])

        # Adding model 'Supervisor_Affiliation'
        db.create_table(u'contact_supervisor_affiliation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('supervisor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contact.Supervisor'])),
            ('title', self.gf('django.db.models.fields.CharField')(default='none', max_length=200)),
        ))
        db.send_create_signal(u'contact', ['Supervisor_Affiliation'])

        # Adding model 'Supervisor_Department'
        db.create_table(u'contact_supervisor_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('supervisor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contact.Supervisor'])),
            ('title', self.gf('django.db.models.fields.CharField')(default='none', max_length=200)),
        ))
        db.send_create_signal(u'contact', ['Supervisor_Department'])

        # Adding model 'Supervisor_Famous_paper'
        db.create_table(u'contact_supervisor_famous_paper', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('supervisor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contact.Supervisor'])),
            ('title', self.gf('django.db.models.fields.CharField')(default='none', max_length=200)),
            ('author', self.gf('django.db.models.fields.CharField')(default='none', max_length=200)),
            ('conference', self.gf('django.db.models.fields.CharField')(default='none', max_length=200)),
        ))
        db.send_create_signal(u'contact', ['Supervisor_Famous_paper'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'contact_contact')

        # Deleting model 'Supervisor'
        db.delete_table(u'contact_supervisor')

        # Deleting model 'Supervisor_Affiliation'
        db.delete_table(u'contact_supervisor_affiliation')

        # Deleting model 'Supervisor_Department'
        db.delete_table(u'contact_supervisor_department')

        # Deleting model 'Supervisor_Famous_paper'
        db.delete_table(u'contact_supervisor_famous_paper')


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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contact.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'research_interest': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'title_contact': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title_research': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'contact.supervisor': {
            'Meta': {'object_name': 'Supervisor'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contact.Contact']"}),
            'display_order': ('django.db.models.fields.IntegerField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'field': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_path': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'research_interest': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'university': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'contact.supervisor_affiliation': {
            'Meta': {'object_name': 'Supervisor_Affiliation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'supervisor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contact.Supervisor']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '200'})
        },
        u'contact.supervisor_department': {
            'Meta': {'object_name': 'Supervisor_Department'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'supervisor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contact.Supervisor']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '200'})
        },
        u'contact.supervisor_famous_paper': {
            'Meta': {'object_name': 'Supervisor_Famous_paper'},
            'author': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '200'}),
            'conference': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'supervisor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contact.Supervisor']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '200'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['contact']