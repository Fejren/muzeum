from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models
from taggit.managers import TaggableManager


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Mark(models.Model):
    mark = models.CharField(max_length=35, null=True)

    def __str__(self):
        return self.mark


class Phone(models.Model):
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    picture = models.ImageField(default="defaultPhonePicture.png")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self)\
            .get_queryset()\
            .filter(status='published')


class Article(models.Model):
    STATUS = (
        ('draft', 'Roboczy'),
        ('published', 'Opublikowany')
    )

    title = models.CharField(max_length=50)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='muzeum_articles')
    body = tinymce_models.HTMLField()
    picture = models.ImageField(default="defaultArticlePicture.png")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default='draft')
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
