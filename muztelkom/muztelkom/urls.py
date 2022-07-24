from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),

    path('', include('core.urls')),

    path('gallery/', include('phone.urls')),
    path('articles/', include('article.urls')),
    path('contact/', include('contact.urls')),
]
