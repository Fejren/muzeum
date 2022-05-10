from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('createPhone/', views.createPhone, name='createPhone'),
    path('createArticle/', views.createArticle, name='createArticle'),
    # path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('articles/', views.articles, name='articles'),
]
