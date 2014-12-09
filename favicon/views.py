from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.list_detail import object_list

from favicon.models import Favicon

from django.conf import settings

#from appname.models import Example


def favicon(request, template_name='favicon/index.html'):
    fav = get_object_or_404(Favicon, isFavicon=True)
    link = settings.MEDIA_URL
    link += fav.faviconImage.name
    return redirect(link)
    pass
    raise Http404


