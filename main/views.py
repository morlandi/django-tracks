from django.shortcuts import render
from django.db.models import Count
from tracks.models import Artist


def index(request):

    artists = (Artist.objects
        .all()
        .annotate(
            num_albums=Count('album', distinct=True),
            num_tracks=Count('album__track', distinct=True),
        )
    )

    return render(request, 'pages/index.html', {
        'artists': artists,
    })
