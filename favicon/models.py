from compat import python_2_unicode_compatible
from django.db import models

from django.conf import settings


from PIL import Image
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile


#sizes = [16,32,64]
sizes = [16,32,57,72,86,96,114,120,128,144,152,195,228]
sizes = getattr(settings, 'FAVICON_SIZES', sizes)

config = {
    'shortcut icon': [16,32,48,128],
    'apple-touch-icon': [57, 72, 114, 144],
    'apple-touch-icon-precomposed': [57, 72, 114, 144],
}


@python_2_unicode_compatible
class Favicon(models.Model):
    verbose_name = 'Favicon'
    verbose_name_plural = 'Favicons'

    title = models.CharField(max_length=100)
    faviconImage = models.ImageField(upload_to="favicon")
    precomposed = models.BooleanField(default=False)

    isFavicon = models.BooleanField(default=True)


    def get_favicons(self):
        favicons = []
        for rel in config:
            for size in config[rel]:
                favicons.append(FaviconImg.objects.get(faviconFK=self, size=size, rel=rel))
        return favicons

    '''
    def get_favicons(self):
        return [self.get_favicon(n).faviconImage.name for n in sizes]
        '''


    '''
    def get_favicons(self):
        #favicons = []
        #for n in sizes:
        #    fav = self.get_favicon(n)
        #    favicons.append(fav.faviconImages.name)

        return favicons
    '''

    '''
    def get_favicons(self):
        objs = FaviconImg.objects.filter(faviconFK=self)
        favicons = []
        for n in sizes:
            favs = objs.filter(size=n)
            fav = favs.get()
            favicons.append(fav.faviconImage.name)
        return favicons
    '''

    '''
    def get_favicons(self):
        objs = FaviconImg.objects.filter(faviconFK=self)
        favicons = []
        for n in sizes:
            favs = objs.filter(size=n)
            try:
                fav = objs.get()
            except:
                if favs:
                    for obj in favs:
                        obj.delete()
                fav = self.get_favicon(n)
            favicons.append(fav.faviconImage.name)
        return favicons
    '''



    def __str__(self):
        return self.faviconImage.name

    # def __unicode__(self):
    #    return self.faviconImage.name

    def get_absolute_url(self):
        return "%s" % self.faviconImage.name

    def get_favicon(self, size, rel, update=False):
        fav, _ = FaviconImg.objects.get_or_create(faviconFK=self, size=size, rel=rel)
        if update and fav.faviconImage:
            fav.faviconImage.delete()
        if (self.faviconImage and not fav.faviconImage):
            tmp = Image.open(self.faviconImage.path)
            tmp.thumbnail((size,size), Image.ANTIALIAS)

            tmpIO = StringIO.StringIO()
            tmp.save(tmpIO, format='PNG')
            tmpFile = InMemoryUploadedFile(tmpIO, None, 'fav-%s.png' % (size,), 'image/png', tmpIO.len, None)

            fav.faviconImage=tmpFile
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

