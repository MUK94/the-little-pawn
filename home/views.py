from django.shortcuts import render
from about.models import About
from .models import Partners, Link

def home(request):
    abouts = About.objects.all()
    partners = Partners.objects.all()
    links = Link.objects.all()
    title = 'Home - The Little Pawn'
    context = {
            'abouts': abouts, 
            'partners': partners, 
            'links': links,
            'title': title,
        }
    return render(request, 'base.html', context)
