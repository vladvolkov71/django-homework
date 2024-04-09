from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    context = {'articles': Article.objects.order_by('published_at').prefetch_related('tags')}

    return render(request, template, context)
