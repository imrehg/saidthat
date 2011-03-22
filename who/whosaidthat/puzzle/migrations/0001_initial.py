# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('puzzle_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('puzzle', ['Category'])

        # Adding model 'Person'
        db.create_table('puzzle_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('imageurl', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('verified', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('puzzle', ['Person'])

        # Adding M2M table for field category on 'Person'
        db.create_table('puzzle_person_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm['puzzle.person'], null=False)),
            ('category', models.ForeignKey(orm['puzzle.category'], null=False))
        ))
        db.create_unique('puzzle_person_category', ['person_id', 'category_id'])

        # Adding model 'Quote'
        db.create_table('puzzle_quote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('update_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['puzzle.Person'])),
            ('posted', self.gf('django.db.models.fields.DateTimeField')()),
            ('vote_up', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('vote_down', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('puzzle', ['Quote'])


    def backwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('puzzle_category')

        # Deleting model 'Person'
        db.delete_table('puzzle_person')

        # Removing M2M table for field category on 'Person'
        db.delete_table('puzzle_person_category')

        # Deleting model 'Quote'
        db.delete_table('puzzle_quote')


    models = {
        'puzzle.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'puzzle.person': {
            'Meta': {'object_name': 'Person'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['puzzle.Category']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageurl': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'puzzle.quote': {
            'Meta': {'object_name': 'Quote'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['puzzle.Person']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'update_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'vote_down': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'vote_up': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['puzzle']
