from django import template
from favicon.models import Favicon
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from favicon.models import Favicon
from favicon.models import config

register = template.Library()

media_url = getattr(settings, 'MEDIA_URL', False)


@register.simple_tag(takes_context=True)
def placeFavicon(context):
    """
    Gets Favicon-URL for the Model.

    Template Syntax:

        {% placeFavicon %}
    """

    if not media_url:
        raise ImproperlyConfigured('MEDIA_URL not found in settings')

    fav = Favicon.objects.filter(isFavicon=True)
    if not fav:
        return '<!-- no favicon -->'
    for n in fav[1:]:
        n.isFavicon = False
    fav = fav[0]
    '''
    if a:
        fav = a[0]
    else:
        return '<!-- %s -->' % ('no favicon found',)
    '''
    favs = fav.get_favicons()
    request = context['request']
    html = ''
    #html += '<link rel="shortcut icon" href="http://%s/favicon.ico"/>' % (request.get_host(),)
    #html += '<link rel="shortcut icon" href="http://%s/favicon.ico"/>'

    '''
    for rel in config:
        for size in sorted(config[rel], reverse=True)[:-1]:
            n = fav.get_favicon(size=size, rel=rel)
            html += '<link rel="%s" size ="%sx%s" href="%s%s"/>' % (
                n.rel, n.size, n.size, media_url, n.faviconImage.name)
        for size in sorted(config[rel], reverse=True)[-1:]:
            n = fav.get_favicon(size=size, rel=rel)
            html += '<link rel="%s" size ="any" href="%s%s"/>' % (
                n.rel, media_url, n.faviconImage.name)
    '''
    for rel in config:
        for size in sorted(config[rel], reverse=True):
            n = fav.get_favicon(size=size, rel=rel)
            html += '<link rel="%s" size ="%sx%s" href="%s%s"/>' % (
                n.rel, n.size, n.size, media_url, n.faviconImage.name)

    default_fav = fav.get_favicon(size=32, rel='shortcut icon')
    html += '<link rel="%s" size ="%sx%s" href="%s%s"/>' % (
        default_fav.rel, default_fav.size, default_fav.size, media_url, default_fav.faviconImage.name)

    return html
