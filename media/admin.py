from django.contrib import admin
from media.models import Artist, Album

class AlbumAdmin(admin.ModelAdmin):
    list_display = ['artist','name', 'date']
    list_display_links = ['name']
    list_filter = ['artist']
    search_fields = ['name']

class AlbumInline(admin.TabularInline):
    model = Album
    extra = 1

class ArtistAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [AlbumInline]

admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
