from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignupForm(UserCreationForm):
    email = forms.EmailField(help_text='Enter a valid Email', required=True)
    first_name = forms.CharField(required=True)
    profile_pic = forms.ImageField(max_length=None, label='Profile Image')

    #
    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError('Email already exists')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'password1', 'password2', 'profile_pic')

        def save(self, commit):
            user = super(UserCreationForm, self).save(commit=False)
            user.email = self.cleaned_data.get("email")
            if commit:
                user.save()
                return user

