from django.contrib import admin

from .models import Main, MainId


class MainStyle(admin.ModelAdmin):
    list_display = ('gender',)
    prepopulated_fields = {'slug': ('gender',)}


admin.site.register(Main)
admin.site.register(MainId, MainStyle)
admin.site.site_header = 'Hello world'
