# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Category.slug'
        db.add_column('puzzle_category', 'slug', self.gf('django.db.models.fields.SlugField')(default=['name'], max_length=50, db_index=True), keep_default=False)

        # Adding field 'Category.description'
        db.add_column('puzzle_category', 'description', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True), keep_default=False)

        # Adding field 'Category.uri'
        db.add_column('puzzle_category', 'uri', self.gf('django.db.models.fields.CharField')(default=True, max_length=200), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Category.slug'
        db.delete_column('puzzle_category', 'slug')

        # Deleting field 'Category.description'
        db.delete_column('puzzle_category', 'description')

        # Deleting field 'Category.uri'
        db.delete_column('puzzle_category', 'uri')


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
