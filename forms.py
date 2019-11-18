from django import forms
from django.forms import ValidationError
from Accounts.models import UserProfile
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter valid email'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Email must be unique')
            return email

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'username': forms.fields.TextInput(attrs={'placeholder': 'Choose a username'}),
            'first_name': forms.fields.TextInput(attrs={'placeholder': 'Enter firstname'}),
            'last_name': forms.fields.TextInput(attrs={'placeholder': 'Enter lastname'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Choose a username'}),

        }

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



class EditProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']