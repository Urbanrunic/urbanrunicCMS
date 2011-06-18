import datetime

from django.db import models
from imagekit.models import ImageModel

class Gallery(ImageModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        ordering = ['-pub_date']
    

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
        spec_module = 'blog.specs'
        cache_dir = 'gallery-photos'
        image_field = 'image'
        save_count_as = 'num_views'
