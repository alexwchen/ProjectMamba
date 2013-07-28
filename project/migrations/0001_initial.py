# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'project_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('authors', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('complete_date', self.gf('django.db.models.fields.DateField')()),
            ('short_description', self.gf('django.db.models.fields.TextField')()),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('rank_img', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('vote_up', self.gf('django.db.models.fields.IntegerField')()),
            ('base_vote', self.gf('django.db.models.fields.IntegerField')()),
            ('PDF', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('video_url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('motivation_content', self.gf('django.db.models.fields.TextField')()),
            ('motivation_image', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'project', ['Project'])

        # Adding model 'Feature'
        db.create_table(u'project_feature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Project'])),
            ('feature_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('feature_content', self.gf('django.db.models.fields.TextField')()),
            ('feature_image', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('display_choice', self.gf('django.db.models.fields.IntegerField')()),
            ('feature_order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'project', ['Feature'])

        # Adding model 'Project_Type'
        db.create_table(u'project_project_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Project'])),
            ('project_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'project', ['Project_Type'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'project_project')

        # Deleting model 'Feature'
        db.delete_table(u'project_feature')

        # Deleting model 'Project_Type'
        db.delete_table(u'project_project_type')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'project.feature': {
            'Meta': {'object_name': 'Feature'},
            'display_choice': ('django.db.models.fields.IntegerField', [], {}),
            'feature_content': ('django.db.models.fields.TextField', [], {}),
            'feature_image': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'feature_order': ('django.db.models.fields.IntegerField', [], {}),
            'feature_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Project']"})
        },
        u'project.project': {
            'Meta': {'object_name': 'Project'},
            'PDF': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'base_vote': ('django.db.models.fields.IntegerField', [], {}),
            'complete_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'motivation_content': ('django.db.models.fields.TextField', [], {}),
            'motivation_image': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rank_img': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'short_description': ('django.db.models.fields.TextField', [], {}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'video_url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'vote_up': ('django.db.models.fields.IntegerField', [], {})
        },
        u'project.project_type': {
            'Meta': {'object_name': 'Project_Type'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Project']"}),
            'project_type': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['project']