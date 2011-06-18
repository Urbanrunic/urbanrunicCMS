from django.conf.urls.defaults import *
from gallery.models import *



urlpatterns = patterns('',
        (r'^gallery/(?P<id>\d+)/$', 'gallery.views.gallery', {
                'model': Gallery,
                'template_name': 'gallery.html',
        }),
        (r'^photo/(?P<id>\d+)/$', 'gallery.views.photo', {
                'model': Photo,
                'template_name': 'photo.html',
        }),
)