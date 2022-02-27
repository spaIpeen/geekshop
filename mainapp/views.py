from django.shortcuts import render


def main(request):
    # content = {
    #     'title': 'Продукты',
    #     'links_menu': links_menu,
    #     'same_products': same_products,
    # }

    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')


def contact(request):
    return render(request, 'mainapp/contact.html')
