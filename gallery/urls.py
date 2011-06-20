from django.conf.urls.defaults import *
from gallery.views import *



urlpatterns = patterns('',
    url(r'^(?P<slug>[-\w]+)/$',
        view='gallery.views.gallery_detail',
        name='gallery_detail',
    ),
    url(r'^$',
        view='gallery.views.gallery',
        name='gallery',
    ),
)