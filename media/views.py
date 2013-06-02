from django.shortcuts import render

from media.models import Album

def index(request):
    context = {'album_list': Album.objects.all()}
    return render(request, 'media/index.html', context)