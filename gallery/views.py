from django.shortcuts import render

from home.models import Partners, Link

from .models import GalleryColOne, GalleryColThree, GalleryColTwo


def gallery(request):
    galOnes = GalleryColOne.objects.all()
    galTwos = GalleryColTwo.objects.all()
    galThrees = GalleryColThree.objects.all()

    title = 'Gallery - The Little Pawn'
    partners = Partners.objects.all()
    links = Link.objects.all()


    context = {
        'galOnes': galOnes, 
        'galTwos': galTwos,
        'galThrees': galThrees,
        'partners': partners,
        'links': links,
        'title': title,
    }
    return render(request, 'gallery.html', context)
