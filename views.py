from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout
from Accounts.forms import UserForm, UserProfileForm, EditProfileForm
from Accounts.models import UserProfile
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


def signup(request):
    form = UserForm(request.POST or None, request.FILES or None)
    image_form = UserProfileForm(request.POST or None, request.FILES or None)
    if form.is_valid() and image_form.is_valid():
        username = form.cleaned_data.get("username")
        messages.success(request, 'Account created for ' + username)
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

@login_required(login_url='/login')
def profile_update(request):
    form =  EditProfileForm(request.POST or None, instance=request.user)
    if request.method == 'POST' or None:
        form =  EditProfileForm(request.POST or None, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            form =  EditProfileForm(request.POST or None, instance=request.user)

    return render(request, 'registration/profile_update.html', {'form': form})


@login_required(login_url='/login')
def profile_image_upload(request):
    instance = UserProfile.objects.get(user=request.user)
    form = UserProfileForm(data=request.POST or None, files=request.FILES or None, instance=instance)
    if request.method == 'POST' or None:
        form = UserProfileForm(data=request.POST or None, files=request.FILES or None, instance=instance)
        if form.is_valid():
            image = request.FILES['image']
            UserProfile.image = request.user
            UserProfile.save(self=instance)
            return redirect('profile')
        else:
            return render(request, 'registration/image_upload.html', {'form': form})

    else:
        form = UserProfileForm(data=request.POST or None, files=request.FILES or None, instance=request.user)
    return render(request, 'registration/image_upload.html', {'form': form})


def profile(request):
    context =  {}
    return render(request, 'registration/profile.html', context)

@login_required(login_url='/login')
def user_images(request, pk=None):
    u = get_object_or_404(UserProfile, pk=request.user.id)
    all_pics = u.image.all()
    context = {
        'all_pics': all_pics,
        'u': u
    }
    return render_to_response('registration/all_images.html', context)



# Create your views here.
