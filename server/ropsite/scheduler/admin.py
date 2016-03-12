from django.contrib import admin

from .models import Lokaler, Øvedage, Segmenter

# Register your models here.


admin.site.register(Øvedage)
admin.site.register(Lokaler)
admin.site.register(Segmenter)

