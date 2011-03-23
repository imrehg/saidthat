# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Person.screen_name'
        db.delete_column('puzzle_person', 'screen_name')

        # Deleting field 'Person.twitter_id'
        db.delete_column('puzzle_person', 'twitter_id')

        # Adding field 'Person.screenname'
        db.add_column('puzzle_person', 'screenname', self.gf('django.db.models.fields.CharField')(default='-missing-', unique=True, max_length=50), keep_default=False)

        # Adding field 'Person.twitterid'
        db.add_column('puzzle_person', 'twitterid', self.gf('django.db.models.fields.CharField')(default=True, max_length=200), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Person.screen_name'
        db.add_column('puzzle_person', 'screen_name', self.gf('django.db.models.fields.CharField')(default='-missing-', max_length=50, unique=True), keep_default=False)

        # Adding field 'Person.twitter_id'
        db.add_column('puzzle_person', 'twitter_id', self.gf('django.db.models.fields.CharField')(default=True, max_length=200), keep_default=False)

        # Deleting field 'Person.screenname'
        db.delete_column('puzzle_person', 'screenname')

        # Deleting field 'Person.twitterid'
        db.delete_column('puzzle_person', 'twitterid')


    models = {
        'puzzle.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "['name']", 'max_length': '50', 'db_index': 'True'}),
            'uri': ('django.db.models.fields.CharField', [], {'default': 'True', 'max_length': '200'})
        },
        'puzzle.person': {
            'Meta': {'object_name': 'Person'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['puzzle.Category']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'default': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageurl': ('django.db.models.fields.URLField', [], {'default': 'True', 'max_length': '200'}),
            'location': ('django.db.models.fields.CharField', [], {'default': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'True', 'max_length': '200'}),
            'screenname': ('django.db.models.fields.CharField', [], {'default': "'-missing-'", 'unique': 'True', 'max_length': '50'}),
            'twitterid': ('django.db.models.fields.CharField', [], {'default': 'True', 'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'default': 'True', 'max_length': '200'}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'puzzle.quote': {
            'Meta': {'object_name': 'Quote'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['puzzle.Person']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'update_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'vote_down': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'vote_up': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['puzzle']
