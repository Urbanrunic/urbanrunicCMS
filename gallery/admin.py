from django.contrib import admin

from gallery.models import GalleryPhoto, CommercialPhoto, MusicPhoto


class GalleryPhotoAdmin(admin.ModelAdmin):
    pass

class CommercialPhotoAdmin(admin.ModelAdmin):
    pass

class MusicPhotoAdmin(admin.ModelAdmin):
    pass


admin.site.register(GalleryPhoto, GalleryPhotoAdmin)
admin.site.register(CommercialPhoto, CommercialPhotoAdmin)
admin.site.register(MusicPhoto, MusicPhotoAdmin)