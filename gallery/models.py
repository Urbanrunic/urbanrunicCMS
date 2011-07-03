import datetime
from django.db import models
from django.conf import settings
from django.db.models import signals
from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from imagekit.models import ImageModel

class Gallery(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    def main_image(self):
        image = Photo.objects.get(gallery=self, main_gallery=True)
        return image

    class Meta:
        ordering = ['-pub_date']
    
    def __unicode__(self):
        return self.name

class Photo(ImageModel):
    title = models.CharField(max_length=100)
    caption = models.TextField(blank=True)
    gallery = models.ManyToManyField(Gallery, related_name="photo_gallery")
    image = models.ImageField(upload_to='gallery-photos')
    num_views = models.PositiveIntegerField(editable=False, default=0)
    published = models.BooleanField(default=True)
    main_gallery = models.BooleanField(default=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        ordering = ['-pub_date']

    class IKOptions:
        # This inner class is where we define the ImageKit options for the model
        spec_module = 'gallery.specs'
        cache_dir = 'gallery-photos'
        image_field = 'image'
        save_count_as = 'num_views'

    def __unicode__(self):
        return self.title
