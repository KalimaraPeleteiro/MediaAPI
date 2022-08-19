from django.contrib import admin
from MediaApp.models import Video, Categoria


class AdminVideo(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'descricao')
    list_display_links = ('titulo',)
    search_fields = ('titulo',)
    list_per_page = 5


class AdminCategoria(admin.ModelAdmin):
    list_display = ('titulo', 'cor')
    list_display_links = ('titulo',)
    search_fields = ('titulo',)
    list_per_page = 5


admin.site.register(Video, AdminVideo)
admin.site.register(Categoria, AdminCategoria)