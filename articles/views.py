from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Scope, Tags


def articles_list(request):
    ordering = '-published_at'
    template = 'articles/news.html'

    object_list = Article.objects.all()
    context = {
        'object_list': object_list
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by


    return render(request, template, context)
