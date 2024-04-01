from time import strftime, strptime

from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {
        'books': Book.objects.all()
    }
    return render(request, template, context)


def date_view(request, pub_date):
    template = 'books/books_date.html'
    data = Book.objects.filter(pub_date=pub_date)
    data_p = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
    data_n = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
    if data_p:
        data_prev = data_p.pub_date.strftime('%Y-%m-%d')
    else:
        data_prev = None
    if data_n:
        data_next = data_n.pub_date.strftime('%Y-%m-%d')
    else:
        data_next = None

    context = {
        'books': data,
        'data_prev': data_prev,
        'data_next': data_next,
    }
    return render(request, template, context)