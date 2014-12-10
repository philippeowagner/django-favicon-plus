from django.conf.urls.defaults import *


urlpatterns = patterns('favicon.views',
                       url(r'^$',
                           view='favicon',
                           name='favicon',
                           ),
                       )
