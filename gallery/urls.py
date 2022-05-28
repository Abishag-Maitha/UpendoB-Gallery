from django.urls import path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns=[
    url('',views.welcome,name = 'welcome'),
    url('image_upload/',views.imageView, name='image_upload'),
    url('success/', views.uploadok, name = 'success'),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)