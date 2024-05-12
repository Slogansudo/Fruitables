from django.contrib import admin
from .models import Artist, Album, Songs
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Artist)
class ArtistAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_date', 'last_updated')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_filter = ('name',)
    ordering = ('id',)


@admin.register(Album)
class AlbumAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'created_date', 'last_updated')
    list_display_links = ('id', 'title', 'created_date', 'last_updated')
    search_fields = ('id', 'title', 'artist')
    list_filter = ('id', )
    ordering = ('id', )


@admin.register(Songs)
class SongsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'created_date', 'last_updated')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_filter = ('id', 'title')
    ordering = ('id', )

