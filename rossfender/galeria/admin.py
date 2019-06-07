from django.contrib import admin
from .models import Gallery
# Register your models here.
class GalleryAdmin(admin.ModelAdmin):
    readonly_fields = ('date')
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 


admin.site.register(Gallery)
