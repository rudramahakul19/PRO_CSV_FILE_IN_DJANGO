from import_export import resources
from .models import SongRank

class SongRankResource(resources.ModelResource):
    class Meta:
        model = SongRank