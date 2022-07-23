from django.contrib import admin
from .models import *

admin.site.site_header = "Panel administacyjny muztelkom.pl"


class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'created']
    list_filter = ['name', 'title', 'created']


admin.site.register(Message, MessageAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish']
    list_filter = ['title', 'publish']


admin.site.register(Article, ArticleAdmin)

admin.site.register(Mark)


class PhoneAdmin(admin.ModelAdmin):
    list_display = ['mark', 'model', 'created']
    list_filter = ['mark', 'model', 'created']


admin.site.register(Phone, PhoneAdmin)
