from django.db import models


class SongRank(models.Model):
    
    rank = models.IntegerField()
    song = models.CharField(max_length=255)
    streams = models.CharField(max_length=5)
    artist = models.CharField(max_length=500)
    release_date = models.DateField(null=True)

    def __str__(self):
        return self.song
    
