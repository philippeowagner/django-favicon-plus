from django.contrib import admin
from favicon.models import Favicon


class FaviconAdmin(admin.ModelAdmin):
    list_display = ('title', 'isFavicon')

admin.site.register(Favicon, FaviconAdmin)
