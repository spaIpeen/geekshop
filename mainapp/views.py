from django.shortcuts import render
import datetime
import json
import pathlib


def main(request):
    title = 'главная'
    with open(f'{pathlib.Path().absolute()}/mainapp/templates/mainapp/json/products.json') as f:
        products = json.load(f)
    content = {
        'title': title,
        'products': products,
    }

    return render(request, 'mainapp/index.html', content)


def products(request):
    title = 'продукты'
    with open(f'{pathlib.Path().absolute()}/mainapp/templates/mainapp/json/links.json') as f:
        links_menu = json.load(f)
    with open(f'{pathlib.Path().absolute()}/mainapp/templates/mainapp/json/same_products.json') as f:
        same_products = json.load(f)
    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = 'контакты'
    visit_date = datetime.datetime.now()
    with open(f'{pathlib.Path().absolute()}/mainapp/templates/mainapp/json/locations.json') as f:
        locations = json.load(f)
    content = {
        'title': title,
        'visit_date': visit_date,
        'locations': locations,
    }
    return render(request, 'mainapp/contact.html', content)
