from django.shortcuts import render
from .models import SongRank
from .resources import SongRankResource
from django.contrib import messages
from tablib import Dataset
import csv,io


def upload(request):
    if request.method == 'POST':
        songrank_resource = SongRankResource()
        dataset = Dataset()
        new_songrank = request.FILES['myfile']

        if not new_songrank.name.endswith('csv'):
            messages.info(request,'Please Upload the CSV File only')
            return render(request,'home.html')

        data_set = new_songrank.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            created = SongRank.objects.update_or_create(
                rank=column[0],
                song=column[1],
                streams=column[2],
                artist=column[3])
    return render(request, 'home.html')