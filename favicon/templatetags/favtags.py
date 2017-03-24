from django import template
from django.utils.safestring import mark_safe

from favicon.models import Favicon, config

register = template.Library()


@register.simple_tag(takes_context=True)
def placeFavicon(context):
    """
    Gets Favicon-URL for the Model.

    Template Syntax:

        {% placeFavicon %}

    """
    fav = Favicon.objects.filter(isFavicon=True).first()
    if not fav:
        return mark_safe('<!-- no favicon -->')
    html = ''
    for rel in config:
        for size in sorted(config[rel], reverse=True):
            n = fav.get_favicon(size=size, rel=rel)
            html += '<link rel="%s" sizes="%sx%s" href="%s"/>' % (
                n.rel, n.size, n.size, n.faviconImage.url)

    default_fav = fav.get_favicon(size=32, rel='shortcut icon')
    html += '<link rel="%s" sizes="%sx%s" href="%s"/>' % (
        default_fav.rel, default_fav.size, default_fav.size, default_fav.faviconImage.url)

    return mark_safe(html)
