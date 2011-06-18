from django.shortcuts import get_object_404, render_to_response
from django.views.generic.list_detail import object_list
from gallery.models import *

def gallery_detail(request, id, Gallery, gallery):
    gallery = Gallery.objects.all(pk=id)
	context = RequestContext(request, {'gallery': gallery})    
    return render_to_response('gallery.html', context)

def photo_detail(request, id, Photo, photo):
	photo = Photo.objects.all(pk=id)
	context = ResquestContext(request, {'photo': photo})
	return render_to_response('photo.html', context)
