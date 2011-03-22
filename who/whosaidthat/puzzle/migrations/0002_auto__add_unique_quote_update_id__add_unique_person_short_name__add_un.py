# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding unique constraint on 'Quote', fields ['update_id']
        db.create_unique('puzzle_quote', ['update_id'])

        # Adding unique constraint on 'Person', fields ['short_name']
        db.create_unique('puzzle_person', ['short_name'])

        # Adding unique constraint on 'Category', fields ['name']
        db.create_unique('puzzle_category', ['name'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Category', fields ['name']
        db.delete_unique('puzzle_category', ['name'])

        # Removing unique constraint on 'Person', fields ['short_name']
        db.delete_unique('puzzle_person', ['short_name'])

        # Removing unique constraint on 'Quote', fields ['update_id']
        db.delete_unique('puzzle_quote', ['update_id'])


    models = {
        'puzzle.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'puzzle.person': {
            'Meta': {'object_name': 'Person'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['puzzle.Category']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageurl': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
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
