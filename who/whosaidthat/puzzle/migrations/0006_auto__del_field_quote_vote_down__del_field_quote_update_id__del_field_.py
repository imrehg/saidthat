# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Quote.vote_down'
        db.delete_column('puzzle_quote', 'vote_down')

        # Deleting field 'Quote.update_id'
        db.delete_column('puzzle_quote', 'update_id')

        # Deleting field 'Quote.vote_up'
        db.delete_column('puzzle_quote', 'vote_up')

        # Adding field 'Quote.updateid'
        db.add_column('puzzle_quote', 'updateid', self.gf('django.db.models.fields.CharField')(default=0, unique=True, max_length=50), keep_default=False)

        # Adding field 'Quote.voteup'
        db.add_column('puzzle_quote', 'voteup', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Quote.votedown'
        db.add_column('puzzle_quote', 'votedown', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Quote.vote_down'
        db.add_column('puzzle_quote', 'vote_down', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Quote.update_id'
        raise RuntimeError("Cannot reverse this migration. 'Quote.update_id' and its values cannot be restored.")

        # Adding field 'Quote.vote_up'
        db.add_column('puzzle_quote', 'vote_up', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Deleting field 'Quote.updateid'
        db.delete_column('puzzle_quote', 'updateid')

        # Deleting field 'Quote.voteup'
        db.delete_column('puzzle_quote', 'voteup')

        # Deleting field 'Quote.votedown'
        db.delete_column('puzzle_quote', 'votedown')


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
