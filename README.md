# django-favicon #

 

##How to use:##
Install django-favicon using PIP.

    pip install -e git+ssh://git@bitbucket.org/arteria/django-favicon.git#egg=favicon


add app to `INSTALLED_APPS` List in your `settings.py` file, make sure `sites`-app is also installed and a url is specified in the admin backend


    INSTALLED_APPS = (
        ...
        'django.contrib.sites',
        ...
        'favicon',
        ...
    )
    

upload an image in the admin backend

use the templatetag in your base.html

    {% load favtags %}
    
    {% placeFavicon %}

this will create (if MEDIA_URL is set to /media/):

    <link rel="shortcut icon" href="/media/favicon/favicon_1.png" />

##favicon##
16x16 .ico or better .png
    
    <link rel="shortcut icon" href="/images/favicon.png" />

###apple-touch-icon(-precomposed)###
57x57, 72x72, 114x114, and 144x144
highest resolution for ipad retina 144x144.png precomposed(=iOS won’t add any effects to the icon)
    
    <link rel="apple-touch-icon" sizes="144x144" href="/images/apple-touch-icon-144x144.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/images/apple-touch-icon-114x114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/images/apple-touch-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="57x57" href="/images/apple-touch-icon-57x57.png">

    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/images/apple-touch-icon-144x144.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/images/apple-touch-icon-114x114.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/images/apple-touch-icon-72x72.png">
    <link rel="apple-touch-icon-precomposed" sizes="57x57" href="/images/apple-touch-icon-57x57.png">

Android versions 1.5 and 1.6 will read the second tag (with "-precomposed"), and versions 2.1 and newer will read the first tag.

Google's specifications say that you should use 48x48 pixel PNGs, but you can use a large image (128x128), like Google does for its own apps.
