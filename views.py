from django.shortcuts import render
from .models import Product, Accounts
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from Products.forms import AccountCreateForm, ProductForm
from django.contrib import messages


def products_detail_view(request):
    obj = Product.objects.all()  # Get a list of products in the database
    context = {
        "object": obj,
    }
    return render(request, 'products/products_detail.html', context)


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "Welcome to the about page",
        "length": 123,
        "main": "The newer one's are here",
        "others": 4
    }
    print(request.user.is_authenticated)
    print(args, kwargs)
    return render(request, "about.html", my_context)


def signup(request):
    form = AccountCreateForm(request.POST)
    # username = request.POST.get('first_name')
    # raw_password = request.POST.get('password')
    # user = authenticate(username=username, password=raw_password)
    # enc_password = pbkdf2_sha256.encrypt(raw_password, salt_size=32)

    if not form.is_valid():
        form = AccountCreateForm()
        context = {
            'form': form,
            # 'enc_password': enc_password,
        }

    else:
        neat = Accounts()
        neat.username = form.cleaned_data['username']
        neat.phone = form.cleaned_data['phone']
        neat.email = form.cleaned_data['email']
        neat.password = form.cleaned_data['password']
        neat.confirm_password = form.cleaned_data['confirm_password']
        # neat.password = pbkdf2_sha256.(neat.password, salt_size=32)

        neat.save()
        return HttpResponseRedirect('', 'success')
        # if len(neat.password) < 7:
        #     raise ValidationError

        # login(request, user)
    return render(request, 'products/products_account.html', context)


def products_create_view(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    # context = {
    #     "form": form,
    # }
    if form.is_valid():
        form.title = form.cleaned_data.get('title')
        form.description = form.cleaned_data.get('description')
        form.price = form.cleaned_data.get('price')
        form.image = form.cleaned_data.get('image')
        form = Product.objects.create(**form.cleaned_data)
        form.save()
        messages.success(request, 'Successfully Created')
        # context = {
        #     "form": form,
        # }

        return HttpResponseRedirect('/create')

    else:
        form = ProductForm(request.POST or None, request.FILES or None)
        messages.error(request, 'Not successful')
        context = {
                "form": form,
            }

        return render(request, 'products/products_create.html', context)


def products_goods_view(request, id):
    obj = Product.objects.get(id=id)
    context = {
        'object': obj
    }
    return render(request, 'products/products_goods.html', context)


def home_view(request, *args, **kwargs):
    print(request)
    print(request.user)
    print(args, kwargs)
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "Welcome to the about page",
        "length": 123,
        "main": "The newer one's are here",
        "others": 4
    }
    print(request.user.is_authenticated)
    print(args, kwargs)
    return render(request, "about.html", my_context)


def contact_view(request, *args, **kwargs):
    print(request.user.is_authenticated)
    print(args, kwargs)
    return render(request, "contact.html", {})


# Create your views here.
