from django.contrib import admin

from gallery.models import Gallery, Photo


class GalleryAdmin(admin.ModelAdmin):
    pass

class PhotoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Gallery)
admin.site.register(Photo)