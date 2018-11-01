# -*- coding:   UTF-8 -*-
from django.http import HttpResponse, HttpResponseNotFound
from django.template.response import TemplateResponse
from .models import *


def test(request):
    book_cnt = Book.objects.count()
    book_name = 'book%d' % book_cnt
    book = Book(name=book_name)
    book.save()
    return TemplateResponse(request, "test.html", {'name': book_name})


def index(request):
    return TemplateResponse(request, "index.html")


def my_custom_page_not_found(request):
    return HttpResponseNotFound("页面没找到")
