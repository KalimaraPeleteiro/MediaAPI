from django.contrib import admin
from MediaApp.models import Video


class AdminVideo(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'descricao')
    list_display_links = ('titulo',)
    search_fields = ('titulo',)
    list_per_page = 5


admin.site.register(Video, AdminVideo)