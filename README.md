# django-favicon #

 

##How to use:##
Install django-favicon using PIP.

    pip install git+https://github.com/yannik-ammann/django-favicon-plus.git


add app to `INSTALLED_APPS` List in your `settings.py` file, make sure `sites`-app is also installed and a url is specified in the admin backend


    INSTALLED_APPS = (
        ...
        'django.contrib.sites',
        ...
        'favicon',
        ...
    )
    
The defaulf `FAVICON_CONFIG` look like this, if you want something else you can define it in your settings.py. The key of the dictionary is the value for the `rel` attribut of the link tag, while the list in the value are the sizes for the `size` attribute and the image resizing.

    FAVICON_CONFIG = {
        'shortcut icon': [16 ,32 ,48 ,128, 192],
        'touch-icon': [196],
        'icon': [196],
        'apple-touch-icon': [57, 72, 114, 144, 180],
        'apple-touch-icon-precomposed': [57, 72, 76, 114, 120, 144, 152,180],
    }

Upload an image in the admin backend --> all the size will be created, its best to take a larger base favicon eg. 256x256

use the templatetag in your base.html

    {% load favtags %}
    
    {% placeFavicon %}

this will create (if MEDIA_URL is set to /media/ and if you didnt specified `FAVICON_CONFIG` in you settings.py):

    <link rel="apple-touch-icon-precomposed" size="180x180" href="/media/favicon/fav-180_OLm8xkp.png">
    <link rel="apple-touch-icon-precomposed" size="152x152" href="/media/favicon/fav-152_9Jc67he.png">
    <link rel="apple-touch-icon-precomposed" size="144x144" href="/media/favicon/fav-144_ZvxBOFK.png">
    <link rel="apple-touch-icon-precomposed" size="120x120" href="/media/favicon/fav-120_RbBHHaY.png">
    <link rel="apple-touch-icon-precomposed" size="114x114" href="/media/favicon/fav-114_61boHJ0.png">
    <link rel="apple-touch-icon-precomposed" size="76x76" href="/media/favicon/fav-76_LMjcgGC.png">
    <link rel="apple-touch-icon-precomposed" size="72x72" href="/media/favicon/fav-72_GSBPE5W.png">
    <link rel="apple-touch-icon-precomposed" size="any" href="/media/favicon/fav-57_oPOGYKW.png">
    <link rel="apple-touch-icon" size="180x180" href="/media/favicon/fav-180_h9ozLZs.png">
    <link rel="apple-touch-icon" size="144x144" href="/media/favicon/fav-144_RWrDXut.png">
    <link rel="apple-touch-icon" size="114x114" href="/media/favicon/fav-114_rw5MSSo.png">
    <link rel="apple-touch-icon" size="72x72" href="/media/favicon/fav-72_ZLXeuvm.png">
    <link rel="apple-touch-icon" size="any" href="/media/favicon/fav-57_I8FDkD3.png">
    <link rel="touch-icon" size="any" href="/media/favicon/fav-196_dLcxCkI.png">
    <link rel="shortcut icon" size="192x192" href="/media/favicon/fav-192_A1TsFrv.png">
    <link rel="shortcut icon" size="128x128" href="/media/favicon/fav-128_h7IeovO.png">
    <link rel="shortcut icon" size="48x48" href="/media/favicon/fav-48_PH92BdV.png">
    <link rel="shortcut icon" size="32x32" href="/media/favicon/fav-32_HbSGwrB.png">
    <link rel="shortcut icon" size="any" href="/media/favicon/fav-16_oQulYqJ.png">
    <link rel="icon" size="any" href="/media/favicon/fav-196_3XOHSqi.png">

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

https://mathiasbynens.be/notes/touch-icons
