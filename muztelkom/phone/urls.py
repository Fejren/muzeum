from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('create/', views.create_phone, name='create_phone'),
]
