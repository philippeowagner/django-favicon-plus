from django import template
from favicon.models import Favicon
from django.conf import settings

from favicon.models import Favicon
from favicon.models import config

from django.core.exceptions import ImproperlyConfigured

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

    fav = Favicon.objects.get(isFavicon=True)
    '''
    if a:
        fav = a[0]
    else:
        return '<!-- %s -->' % ('no favicon found',)
    '''

    favs = fav.get_favicons()



    request = context['request']

    html = '<link rel="shortcut icon" href="http://%s/favicon.ico"/>' % (request.get_host(),)



    '''
    for rel in config:
        for size in sorted(config[rel],reverse=True):
            n = fav.get_favicon(size=size,rel=rel)
            html += '<link rel="%s" size ="%sx%s" href="%s%s"/>' % ( n.rel, n.size, n.size, media_url, n.faviconImage.name)
    '''

    
    for rel in config:
        for size in sorted(config[rel],reverse=True)[:-1]:
            n = fav.get_favicon(size=size,rel=rel)
            html += '<link rel="%s" size ="%sx%s" href="%s%s"/>' % ( n.rel, n.size, n.size, media_url, n.faviconImage.name)
        for size in sorted(config[rel],reverse=True)[-1:]:
            n = fav.get_favicon(size=size,rel=rel)
            html += '<link rel="%s" size ="any" href="%s%s"/>' % ( n.rel, media_url, n.faviconImage.name)
    

    

    return html


'''
    try:
        icon = Favicon.objects.all()[0]
        return """<link rel='shortcut icon' href='%s%s'/>
        <!-- %i -->""" %  ( str(settings.MEDIA_URL), str(icon.get_absolute_url()), icon.id )
    except:
        pass
    return "<!-- ERROR: No valid favicon found, see https://bitbucket.org/arteria/django-favicon for more info. -->"
'''
