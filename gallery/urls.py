from django.urls import path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns=[
    url('',views.welcome, name = 'welcome'),
    url('image_upload/',views.imageView, name='image_upload'),
    url('success/', views.uploadok, name = 'success'),
    url('search_images/', views.search_category, name='search_images'),
    url('image/<int:id>',views.view_image,name='view_image'),
    url('delete_image/<int:id>', views.delete_image, name='delete_image'),
    url('update_image/<int:id>', views.update_image, name='update_image'),
    url('save_category/',views.save_category, name='category'),
    url('save_location/',views.save_location, name='location'),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)