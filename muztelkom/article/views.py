from django.shortcuts import render
from django import http
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from core.models import Article

from article.forms import ArticleForm


def create_article(request):
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
