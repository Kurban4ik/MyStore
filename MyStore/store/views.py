from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


# TODO перевести urlки Index.html на динамические ссылки

# Create your views here.
def main(req):
    dc = {'title': 'Zay Shop'}
    return render(req, 'store/index.html', dc)


def pageNotFound(req, exception):
    return HttpResponseNotFound('123')


def about(req):
    dc = {'title': 'Zay Shop'}
    return render(req, 'store/about.html', dc)


def contact(req):
    dc = {'title': 'Zay Shop'}
    return render(req, 'store/contact.html', dc)


def base(req):
    dc = {'title': 'Zay Shop'}
    return render(req, 'store/based.html', dc)


def shop_single(req, name):
    dc = {'title': 'Zay Shop'}
    return render(req, 'store/shop-single.html', dc)


def shop(req):
    dc = {'title': 'Zay Shop'}
    return render(req, 'store/shop.html', dc)
