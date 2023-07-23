from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# TODO обязательно доработать выход на один товар
# TODO добавить выборку на комментарии
# TODO развить спецификацию
# TODO добавить размеры
# TODO Quantity
# TODO файловую систему
# TODO написать комментарии ко всему проекту

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


def shop_single(req, name):  # на вход подается "название файла + _ + id этого товара"
    name = name.split('_')
    pk = int(name[-1])

    stuff = Stuff.objects.get(pk=pk)
    colors = []
    sizes = []

    for i in stuff.colors.split(';'):
        color_name, quantity = i.split('_')
        colors.append({'quantity': int(quantity), 'color': color_name})  # обрабатываю все доступные
        # цвета товара по принципу цвет_количество

    for i in stuff.sizes.split(';'):
        size, quantity = i.split('_')
        sizes.append({'size': size, 'quantity': int(quantity)})  # обрабатываю все доступные
        # размеры товара по принципу размер_количество

    dc = {'title': 'Zay Shop', 'stuff': stuff,
          'rng': range(stuff.rating),
          'rv_rng': range(5 - stuff.rating), # rng и rv_rng это количество желтых и серых звездочек
          'clrs': colors,
          'specification': stuff.compound.split(';'),
          'sizes': sizes,
          'stuff_name': stuff.name.split('_')[0],
          }

    return render(req, 'store/shop-single.html', dc)


def shop(req):
    dc = {'title': 'Zay Shop'}
    return render(req, 'store/shop.html', dc)
