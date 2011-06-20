import datetime
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.list_detail import object_list
from gallery.models import Gallery, Photo

def gallery_detail(request, id, Gallery, gallery):
    gallery = Gallery.objects.all()
    context = RequestContext(request, {'gallery': gallery})    
    return render_to_response('gallery.html', context)

def photo_detail(request, id, Photo, image):
    image = Photo.objects.all(pk=id)
    context = ResquestContext(request, {'image': image})
    return render_to_response('gallery-detail.html', context)
