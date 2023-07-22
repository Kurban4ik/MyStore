from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# TODO обязательно доработать выход на один товар
# TODO добавить выборку на комментарии

# Create your views here.
from store.models import Stuff


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
    name = name.split('_')
    nm = name[0]
    pk = int(name[1])
    stuff = Stuff.objects.get(pk=pk)
    dc = {'title': 'Zay Shop', 'stuff': stuff,
          'rng': range(stuff.rating),
          'rv_rng': range(5 - stuff.rating)
          }
    return render(req, 'store/shop-single.html', dc)


def shop(req):
    dc = {'title': 'Zay Shop'}
    return render(req, 'store/shop.html', dc)
