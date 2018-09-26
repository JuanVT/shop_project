from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from shop_project.shop.forms import ReviewForm
from shop_project.shop.models import Product, Category, Review


def get_products(request):

    context = {

        'products': Product.objects.all(),
    }

    template = loader.get_template("shop/products.html")
    return HttpResponse(template.render(context=context, request=request))


def get_product(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':

        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()

    review_form = ReviewForm()
    context = {
        'product': product,
        'form': review_form
    }

    template = loader.get_template("shop/product-detail.html")
    return HttpResponse(template.render(context=context, request=request))


def delete_product(request, product_id):

    product = Product.objects.get(id=product_id)
    product.delete()
    context = {

        'product': product
    }

    template = loader.get_template("shop/deleted_product.html")
    return HttpResponse(template.render(context=context, request=request))


def update_product(request, product_id):

    name = request.POST.dict().get('name')
    price = request.POST.dict().get('price')
    description = request.POST.dict().get('description')

    product = Product.objects.get(id=product_id)
    product.name = name
    product.price = price
    product.description = description
    product.save()

    context = {

        'product': product
    }

    template = loader.get_template("shop/product.html")
    return HttpResponse(template.render(context=context, request=request))


def get_categories(request):

    categories = Category.objects.all()

    context = {
        'categories': categories

    }

    template = loader.get_template("shop/categories.html")
    return HttpResponse(template.render(context=context, request=request))


def get_category(request, category_slug):

    category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category__slug=category_slug)
    categories = Category.objects.all()

    context = {
        'category': category,
        'products': products,
        'categories': categories,
    }

    template = loader.get_template("shop/category.html")
    return HttpResponse(template.render(context=context, request=request))


def add_review(request):

    if request.method == 'POST':

        form = ReviewForm(request.POST)

        if form.is_valid():

            form.save()
            return HttpResponseRedirect('get_product')


def product_reviews(request, product_id):

    product = Product.objects.get(id=product_id)

    context = {

        'product': product,

    }
    template = loader.get_template("shop/product_review.html")
    return HttpResponse(template.render(context=context, request=request))


