# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Photo.original_image'
        db.delete_column('gallery_photo', 'original_image')

        # Adding field 'Photo.image'
        db.add_column('gallery_photo', 'image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Photo.original_image'
        db.add_column('gallery_photo', 'original_image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100), keep_default=False)

        # Deleting field 'Photo.image'
        db.delete_column('gallery_photo', 'image')


    models = {
        'gallery.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'gallery.photo': {
            'Meta': {'object_name': 'Photo'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'photo_gallery'", 'symmetrical': 'False', 'to': "orm['gallery.Gallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'num_views': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['gallery']
