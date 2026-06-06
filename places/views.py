from django.shortcuts import render, get_object_or_404
from .models import Place


def feed(request):
    places = Place.objects.filter(status='published').prefetch_related('photos')
    return render(request, 'places/feed.html', {'places': places})


def place_detail(request, slug):
    place = get_object_or_404(Place, slug=slug, status='published')
    return render(request, 'places/detail.html', {'place': place})
