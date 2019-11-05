from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout
from Accounts.forms import UserForm, UserProfileForm
from django.contrib import messages


def signup(request):
    form = UserForm(request.POST or None, request.FILES or None)
    image_form = UserProfileForm(request.POST or None, request.FILES or None)
    if form.is_valid() and image_form.is_valid():
        email = form.cleaned_data.get("email")
        messages.success(request, 'Account created for ' + email)
        user = form.save()
        profile_image = image_form.save(commit=False)
        profile_image.user = user
        profile_image.save()

        return redirect('signup')
    else:
        form = UserForm(request.POST or None, request.FILES or None)
        image_form = UserProfileForm(request.POST or None, request.FILES or None)
        return render(request, 'registration/signup.html', context={'form': form, 'image_form': image_form})


def login(request):
    if request.method == 'POST' or None:
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'registration/home.html')


def logout(request):
    if request.method == 'POST' or None:
        logout(request, user)


def profile(request):
    context =  {}
    return render(request, 'registration/profile.html', context)




# Create your views here.
