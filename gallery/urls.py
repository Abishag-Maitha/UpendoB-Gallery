from django.urls import re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import *

urlpatterns=[
    url('',views.welcome,name = 'welcome'),
    url('image_upload/',imageView, name='image_upload'),
    url('success/', uploadok, name = 'success'),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)