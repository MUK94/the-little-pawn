from django.shortcuts import render

from home.models import Partners, Link

from .models import About, Achievement


def about(request):
    abouts = About.objects.all()
    achievements = Achievement.objects.all()
    partners = Partners.objects.all()
    links = Link.objects.all()
    title = 'About - The Little Pawn'
    context = {
            'abouts': abouts, 
            'achievements': achievements, 
            'partners':partners, 
            'links': links,
            'title': title,
        }
    return render(request, 'about.html', context)
