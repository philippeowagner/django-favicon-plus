from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.list_detail import object_list

from favicon.models import Favicon

from django.conf import settings

#from appname.models import Example


def favicon(request, template_name='favicon/index.html'):
    if 'favicon' in request.path:
        fav = get_object_or_404(Favicon, isFavicon=True)
        link = settings.MEDIA_URL
        link += fav.faviconImage.name
        return redirect(link)
    if 'apple-touch-icon' in request.path:
        fav = get_object_or_404(Favicon, isFavicon=True)
        favicon = fav.get_favicon(57,'apple-touch-icon')
        link = settings.MEDIA_URL
        link += favicon.faviconImage.name
        return redirect(link)

    raise Http404

def favicon_apple(request):
    fav = get_object_or_404(Favicon, isFavicon=True)
    favicon = fav.get_favicon(57,'apple-touch-icon')
    link = settings.MEDIA_URL
    link += favicon.faviconImage.name
    return redirect(link)