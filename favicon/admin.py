from django.contrib import admin
from favicon.models import Favicon, FaviconImg


class FaviconAdmin(admin.ModelAdmin):
    list_display = ('title', 'isFavicon')

admin.site.register(Favicon, FaviconAdmin)


class FaviconImgAdmin(admin.ModelAdmin):
    list_display = ('faviconFK', 'rel', 'size', 'faviconImage')

    def queryset(self, request):
        qs = super(FaviconImgAdmin, self).queryset(request)
        isFavicon = Favicon.objects.filter(isFavicon = True)
        if not len(isFavicon) == 1:
            for n in Favicon.objects.all():
                n.isFavicon = False
                return qs
        isFavicon = isFavicon[0]
        return qs.filter(faviconFK = isFavicon)

admin.site.register(FaviconImg, FaviconImgAdmin)
