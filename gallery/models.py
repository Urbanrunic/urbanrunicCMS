from django.db import models
from imagekit.models import ImageModel

class GalleryPhoto(ImageModel):
    name = models.CharField(max_length=100)
    original_image = models.ImageField(upload_to='gallery-photos')
    num_views = models.PositiveIntegerField(editable=False, default=0)

    class IKOptions:
        # This inner class is where we define the ImageKit options for the model
        spec_module = 'blog.specs'
        cache_dir = 'gallery-photos'
        image_field = 'original_image'
        save_count_as = 'num_views'

class CommercialPhoto(ImageModel):
    name = models.CharField(max_length=100)
    original_image = models.ImageField(upload_to='commercial-photos')
    num_views = models.PositiveIntegerField(editable=False, default=0)

    class IKOptions:
        # This inner class is where we define the ImageKit options for the model
        spec_module = 'blog.specs'
        cache_dir = 'commercial-photos'
        image_field = 'original_image'
        save_count_as = 'num_views'


class MusicPhoto(ImageModel):
    name = models.CharField(max_length=100)
    original_image = models.ImageField(upload_to='music-photos')
    num_views = models.PositiveIntegerField(editable=False, default=0)

    class IKOptions:
        # This inner class is where we define the ImageKit options for the model
        spec_module = 'blog.specs'
        cache_dir = 'music-photos'
        image_field = 'original_image'
        save_count_as = 'num_views'
