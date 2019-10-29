from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout
from Accounts.forms import SignupForm
from Accounts.models import Users
from django.contrib import messages


def signup(request):
    form = SignupForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        form.profile_pic = form.cleaned_data.get("profile_pic")
        messages.success(request, 'Account created for ' + email)
        form.save()
        use = Users.objects.create(**form.cleaned_data)
        use.save()
        return redirect('signup')
    else:
        form = SignupForm(request.POST, request.FILES)
        return render(request, 'registration/signup.html', context={'form': form})


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
            return redirect('home')

    else:
        return render(request, 'registration/login.html')



# Create your views here.
