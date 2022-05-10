from django import http
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import PhoneForm, ArticleForm, MessageForm
from .models import Phone, Article, Mark


class HomeView(TemplateView):
    template_name = 'muzeum/home.html'


def gallery(request):
    phones = Phone.objects.all()
    marks = Mark.objects.all()

    if request.method == 'GET':
        search = request.GET.get('mark_filter', None)
        if search is not None:
            phones = Phone.objects.filter(mark__mark=search)
        else:
            phones = Phone.objects.all()

    context = {
        'phones': phones,
        'marks': marks,
    }
    return render(request, 'muzeum/gallery/gallery.html', context)


def createPhone(request):
    count_of_phones = Phone.objects.count()
    if count_of_phones > 0:
        lastId = Phone.objects.last().id+1
    else:
        lastId = 'Pierwszy telefon należy dodać w panelu administratora'
    if request.method == 'POST':
        formset = PhoneForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return http.HttpResponseRedirect(request.path)
    else:
        formset = PhoneForm()
    context = {
        'formset': formset,
        'phones_count': count_of_phones,
        'lastId': lastId,
    }
    return render(request, 'muzeum/gallery/gallery_form.html', context)


def createArticle(request):
    articles_count = Article.objects.count()
    if request.method == 'POST':
        formset = ArticleForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return http.HttpResponseRedirect(request.path)
    else:
        formset = ArticleForm()
    context = {
        'formset': formset,
        'articles_count': articles_count,
    }
    return render(request, 'muzeum/articles/article_form.html', context)


def articles(request):
    news = Article.objects.order_by("-pk")
    page = request.GET.get('page', 1)
    # TODO: finish paginator template
    paginator = Paginator(news, 3)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {
        'news': news,
        'page': page,
    }
    return render(request, 'muzeum/articles/articles.html', context)


def contact(request):
    if request.method == 'POST':
        formset = MessageForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return http.HttpResponseRedirect(request.path)
    else:
        formset = MessageForm()
    context = {
        'formset': formset,
    }
    return render(request, 'muzeum/contact.html', context)
