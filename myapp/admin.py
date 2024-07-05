from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import SongRank


@admin.register(SongRank)
class SongRankAdmin(ImportExportModelAdmin):
    list_display = ['rank', 'song', 'streams', 'artist']
