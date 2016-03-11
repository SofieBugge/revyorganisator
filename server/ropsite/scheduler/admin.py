from django.contrib import admin

from .models import Lokaler, Øvedag, Segmenter

# Register your models here.


admin.site.register(Øvedag)
admin.site.register(Lokaler)
admin.site.register(Segmenter)

