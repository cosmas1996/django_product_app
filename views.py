from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from Products.forms import ProductForm
from django.contrib import messages


def products_detail_view(request):
    obj = Product.objects.all()  # Get a list of products in the database
    # kind = Product.objects.filter(title='card')
    # print(kind)
    context = {
        "object": obj,
    }
    return render(request, 'products/products_products.html', context)


def about_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "about.html", my_context)


def products_create_view(request):
    # Get the form
    form = ProductForm(request.POST or None, request.FILES or None)
   # check if the form is valid
    if form.is_valid():
        form.title = form.cleaned_data.get('title')
        form.description = form.cleaned_data.get('description')
        form.price = form.cleaned_data.get('price')
        form.image = form.cleaned_data.get('image')
        form = Product.objects.create(**form.cleaned_data)
        form.save()
        # message to display if form is saved
        messages.success(request, form.title +' Successfully Created')
        # context = {
        #     "form": form,
        # }

        return HttpResponseRedirect('/create')

    else:
        form = ProductForm(request.POST or None, request.FILES or None)
        # messages.error(request, 'Not successful')
        context = {
                "form": form,
            }

        return render(request, 'products/products_create.html', context)


def products_update_view(request, id=None):
    instance = get_object_or_404(Product, id=id)
    if request.method == 'POST' or None:
        form = ProductForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Successfully Updated')

        return HttpResponseRedirect('/products')

    else:
        instance = get_object_or_404(Product, id=id)
        form = ProductForm(request.POST or None, request.FILES or None, instance=instance)
        context = {
            "form": form,
            "instance": instance
        }

        return render(request, 'products/products_update.html', context)


def products_goods_view(request, id):
    obj = Product.objects.get(id=id)
    context = {
        'object': obj
    }
    return render(request, 'products/products_goods.html', context)


def products_delete(request, id):
    item = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST' or None:
        obj.delete()

        return HttpResponseRedirect('/products')
    return render(request, 'products/products_delete.html', {'item': item})


def home_view(request, *args, **kwargs):
    print(request.user)

    return render(request, "index.html", {})


def about_view(request, *args, **kwargs):
    my_context = {}

    return render(request, "about.html", my_context)


def contact_view(request, *args, **kwargs):
    print(request.user.is_authenticated)
    print(args, kwargs)
    return render(request, "contact.html", {})



# Create your views here.
