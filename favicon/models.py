from compat import python_2_unicode_compatible

import sys

from django.db import models
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile

from PIL import Image
from compat import BytesIO

config = {
    'shortcut icon': [16, 32, 48, 128, 192],
    'touch-icon': [192],
    'icon': [192],
    'apple-touch-icon': [57, 72, 114, 144, 180],
    'apple-touch-icon-precomposed': [57, 72, 76, 114, 120, 144, 152, 180],
}

config = getattr(settings, 'FAVICON_CONFIG', config)

def pre_delete_image(sender, instance, **kwargs):
    instance.del_image()


@python_2_unicode_compatible
class Favicon(models.Model):

    title = models.CharField(max_length=100)
    faviconImage = models.ImageField(upload_to="favicon")

    isFavicon = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Favicon'
        verbose_name_plural = 'Favicons'

    def get_favicons(self):
        favicons = []
        for rel in config:
            for size in config[rel]:
                favicons.append(self.get_favicon(size, rel))
        return favicons

    def __str__(self):
        return self.faviconImage.name

    def get_absolute_url(self):
        return "%s" % self.faviconImage.name

    def del_image(self):
        self.faviconImage.delete()

    def get_favicon(self, size, rel, update=False):
        """
        get or create a favicon for size, rel(attr) and uploaded favicon
        optional:
            update=True
        """
        fav, _ = FaviconImg.objects.get_or_create(
            faviconFK=self, size=size, rel=rel)
        if update and fav.faviconImage:
            fav.del_image()
        if self.faviconImage and not fav.faviconImage:
            tmp = Image.open(self.faviconImage.path)
            tmp.thumbnail((size, size), Image.ANTIALIAS)

            tmpIO = BytesIO()
            tmp.save(tmpIO, format='PNG')
            tmpFile = InMemoryUploadedFile(
                tmpIO, None, 'fav-%s.png' %
                (size,), 'image/png', sys.getsizeof(tmpIO), None)

            fav.faviconImage = tmpFile
            fav.save()
        return fav

    def save(self, *args, **kwargs):
        update = False

        if self.isFavicon:
            for n in Favicon.objects.exclude(pk=self.pk):
                n.isFavicon = False
                n.save()

        super(Favicon, self).save(*args, **kwargs)

        if self.faviconImage:
            for rel in config:
                for size in config[rel]:
                    self.get_favicon(size=size,rel=rel, update=update)


        #make sure default favicon is set
        self.get_favicon(size=32, rel='shortcut icon')


class FaviconImg(models.Model):
    faviconFK = models.ForeignKey(Favicon)
    size = models.IntegerField()
    rel = models.CharField(max_length=250, null=True)
    faviconImage = models.ImageField(upload_to='favicon')

    def del_image(self):
        self.faviconImage.delete()

from django.db.models import signals
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

signals.pre_delete.connect(pre_delete_image, sender=Favicon)
signals.pre_delete.connect(pre_delete_image, sender=FaviconImg)
