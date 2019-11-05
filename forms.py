from django import forms
from django.forms import ValidationError
from Accounts.models import UserProfile
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

        def save(self, commit):
            user = super(UserCreationForm, self).save(commit=False)

            user.email = self.cleaned_data.get("email")
            if commit:
                user.save()
                return user


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image',)