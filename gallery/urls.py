from django.conf.urls.defaults import *
from gallery.views import *
from gallery.models import *



urlpatterns = patterns('',
        (r'^/(?P<id>\d+)/$', 'gallery.views.gallery_detail', {
                'model': Gallery,
                'template_name': 'gallery.html',
        }),
        (r'^gallery-detail/(?P<id>\d+)/$', 'gallery.views.photo_detail', {
                'model': Photo,
                'template_name': 'gallery-detail.html',
        }),
)