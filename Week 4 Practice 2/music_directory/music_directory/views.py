from django.shortcuts import render
from album.models import Album
from musician.models import Musucian

def home(request):
    musicians = Musucian.objects.all()
    albums = Album.objects.all()
    # for album in albums:
    #     for m in album.musician.all():
            # print(m)

    # for m in musicians:
    #     for a in m.album.all():
    #         print(a)

    return render(request, 'home.html', {'musicians': musicians, 'albums': albums})