from compat import python_2_unicode_compatible
from django.db import models

from django.conf import settings


from PIL import Image
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile

config = {
    'shortcut icon': [16, 32, 48, 128, 192],
    'touch-icon': [196],
    'icon': [196],
    'apple-touch-icon': [57, 72, 114, 144, 180],
    'apple-touch-icon-precomposed': [57, 72, 76, 114, 120, 144, 152, 180],
}

config = getattr(settings, 'FAVICON_CONFIG', config)


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

    def get_favicon(self, size, rel, update=False):
        fav, _ = FaviconImg.objects.get_or_create(
            faviconFK=self, size=size, rel=rel)
        if update and fav.faviconImage:
            fav.faviconImage.delete()
        if (self.faviconImage and not fav.faviconImage):
            tmp = Image.open(self.faviconImage.path)
            tmp.thumbnail((size, size), Image.ANTIALIAS)

            tmpIO = StringIO.StringIO()
            tmp.save(tmpIO, format='PNG')
            tmpFile = InMemoryUploadedFile(
                tmpIO, None, 'fav-%s.png' %
                (size,), 'image/png', tmpIO.len, None)

            fav.faviconImage = tmpFile
            fav.save()
        return fav

    def save(self, *args, **kwargs):
        print 'testtesttest'
        if self.isFavicon:
            for n in Favicon.objects.exclude(pk=self.pk):
                n.isFavicon = False
                n.save()

        super(Favicon, self).save(*args, **kwargs)
        orig = Favicon.objects.get(pk=self.pk)
        update = True
        #if self.faviconImage.name is not orig.faviconImage.name:
        #    update = True
        #print '%s , -------------------- upadte --------' % (update,)

        if self.faviconImage:
            for rel in config:
                for size in config[rel]:
                    self.get_favicon(size=size,rel=rel, update=update)


        #if self.faviconImage:
        #    for n in sizes:
        #        self.get_favicon(n,update=update)


class FaviconImg(models.Model):
    faviconFK = models.ForeignKey(Favicon)
    size = models.IntegerField()
    rel = models.CharField(max_length=250, null=True)
    faviconImage = models.ImageField(upload_to='favicon')
