import datetime
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.list_detail import object_list
from gallery.models import Gallery, Photo

def gallery(request):
    gallery = Gallery.objects.all()
    context = RequestContext(request, {'gallery': gallery})    
    return render_to_response('gallery/gallery.html', context)

def gallery_detail(request, id):
    gallery = get_object_or_404(Gallery, pk=id)
    images = Photo.objects.filter(gallery=gallery)
    context = RequestContext(request, {'images': images})
    return render_to_response('gallery/gallery-detail.html', context)
