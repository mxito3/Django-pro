from django.http import HttpResponse, HttpResponseNotFound
from django.template.response import TemplateResponse


def test(request):
    return HttpResponse("this is blog test")


def index(request):
    return TemplateResponse(request, "index.html")


def my_custom_page_not_found(request):
    return HttpResponseNotFound("页面没找到")
