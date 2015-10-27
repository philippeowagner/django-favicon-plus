# django-favicon-plus #

Django favicon plus is a simple django app which allows you to upload a image and it renders a wide variety for html link tags to display the favicon. These different tags are used for bookmark links on mobile devices or they appear if you favorite a website in your browser. 

##How to use:
Install django-favicon using PIP.
```shell
pip install django-favicon-plus
 
pip install git+https://github.com/arteria/django-favicon-plus.git
```

Add app to `INSTALLED_APPS` List in your `settings.py` file, make sure `sites`-app is also installed and a URL is specified in the admin backend

```python
INSTALLED_APPS = (
    ...
    'django.contrib.sites',
    ...
    'favicon',
    ...
)
```    
The default `FAVICON_CONFIG` look like this, if you want something else you can define it in your settings.py. The key of the dictionary is the value for the `rel` attribute of the link tag, while the list in the value are the sizes for the `size` attribute and the image resizing.
```python
FAVICON_CONFIG = {
    'shortcut icon': [16 ,32 ,48 ,128, 192],
    'touch-icon': [196],
    'icon': [196],
    'apple-touch-icon': [57, 72, 114, 144, 180],
    'apple-touch-icon-precomposed': [57, 72, 76, 114, 120, 144, 152,180],
}
```
Upload an image in the admin backend --> all the size will be created, its best to take a larger base favicon

use the templatetag in your base.html
```html+django
{% load favtags %}
    
{% placeFavicon %}
```
this will create (if MEDIA_URL is set to /media/ and if you didnt specified `FAVICON_CONFIG` in you settings.py):
```html
<link rel="apple-touch-icon-precomposed" size ="180x180" href="/media/favicon/fav-180.png"/>
<link rel="apple-touch-icon-precomposed" size ="152x152" href="/media/favicon/fav-152.png"/>
<link rel="apple-touch-icon-precomposed" size ="144x144" href="/media/favicon/fav-144.png"/>
<link rel="apple-touch-icon-precomposed" size ="120x120" href="/media/favicon/fav-120.png"/>
<link rel="apple-touch-icon-precomposed" size ="114x114" href="/media/favicon/fav-114.png"/>
<link rel="apple-touch-icon-precomposed" size ="76x76" href="/media/favicon/fav-76.png"/>
<link rel="apple-touch-icon-precomposed" size ="72x72" href="/media/favicon/fav-72.png"/>
<link rel="apple-touch-icon-precomposed" size ="57x57" href="/media/favicon/fav-57.png"/>
<link rel="apple-touch-icon" size ="180x180" href="/media/favicon/fav-180_5l5PyO1.png"/>
<link rel="apple-touch-icon" size ="144x144" href="/media/favicon/fav-144_5A8THfC.png"/>
<link rel="apple-touch-icon" size ="114x114" href="/media/favicon/fav-114_GqBGFXA.png"/>
<link rel="apple-touch-icon" size ="72x72" href="/media/favicon/fav-72_UoWu9ik.png"/>
<link rel="apple-touch-icon" size ="57x57" href="/media/favicon/fav-57_sfX3XoJ.png"/>
<link rel="touch-icon" size ="192x192" href="/media/favicon/fav-192.png"/>
<link rel="shortcut icon" size ="192x192" href="/media/favicon/fav-192_rD0bCKr.png"/>
<link rel="shortcut icon" size ="128x128" href="/media/favicon/fav-128.png"/>
<link rel="shortcut icon" size ="48x48" href="/media/favicon/fav-48.png"/>
<link rel="shortcut icon" size ="32x32" href="/media/favicon/fav-32.png"/>
<link rel="shortcut icon" size ="16x16" href="/media/favicon/fav-16.png"/>
<link rel="icon" size ="192x192" href="/media/favicon/fav-192_Gw5Uu1M.png"/>
<link rel="shortcut icon" size ="32x32" href="/media/favicon/fav-32.png"/>
```
## Management

You can upload multiple images, but only one is set as favicon and used.


## Contribution

If you want to contribute something send a PR.


#Source

### Based on 

[Favicon Cheat Sheet on github](https://github.com/audreyr/favicon-cheat-sheet)

###Favicon
16x16 .ico or better .png
```html
<link rel="shortcut icon" href="/images/favicon.png" />
```
###apple-touch-icon(-precomposed)
57x57, 72x72, 114x114, and 144x144
highest resolution for ipad retina 144x144.png precomposed(=iOS won’t add any effects to the icon)
```html
<link rel="apple-touch-icon" sizes="144x144" href="/images/apple-touch-icon-144x144.png">
<link rel="apple-touch-icon" sizes="114x114" href="/images/apple-touch-icon-114x114.png">
<link rel="apple-touch-icon" sizes="72x72" href="/images/apple-touch-icon-72x72.png">
<link rel="apple-touch-icon" sizes="57x57" href="/images/apple-touch-icon-57x57.png">

<link rel="apple-touch-icon-precomposed" sizes="144x144" href="/images/apple-touch-icon-144x144.png">
<link rel="apple-touch-icon-precomposed" sizes="114x114" href="/images/apple-touch-icon-114x114.png">
<link rel="apple-touch-icon-precomposed" sizes="72x72" href="/images/apple-touch-icon-72x72.png">
<link rel="apple-touch-icon-precomposed" sizes="57x57" href="/images/apple-touch-icon-57x57.png">
```
Android versions 1.5 and 1.6 will read the second tag (with "-precomposed"), and versions 2.1 and newer will read the first tag.

Google's specifications say that you should use 48x48 pixel PNGs, but you can use a large image (128x128), like Google does for its own apps.

https://mathiasbynens.be/notes/touch-icons
