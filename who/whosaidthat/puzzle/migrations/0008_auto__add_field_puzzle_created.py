# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Puzzle.created'
        db.add_column('puzzle_puzzle', 'created', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Puzzle.created'
        db.delete_column('puzzle_puzzle', 'created')


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
        'puzzle.puzzle': {
            'Meta': {'object_name': 'Puzzle'},
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'fakeauth0': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'blank': 'True', 'to': "orm['puzzle.Person']"}),
            'fakeauth1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'blank': 'True', 'to': "orm['puzzle.Person']"}),
            'fakeauth2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'blank': 'True', 'to': "orm['puzzle.Person']"}),
            'goodguess': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quote': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['puzzle.Quote']", 'blank': 'True'}),
            'totalguess': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'puzzle.quote': {
            'Meta': {'object_name': 'Quote'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['puzzle.Person']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'updateid': ('django.db.models.fields.CharField', [], {'default': '0', 'unique': 'True', 'max_length': '50'}),
            'votedown': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'voteup': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['puzzle']
