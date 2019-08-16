from django import forms
from .models import Product
import re
from .models import Accounts


class ProductForm(forms.Form):
    title = forms.CharField(max_length=20, min_length=3,
                            widget=forms.Textarea(attrs={'placeholder': 'Title of Product',
                                                         'rows': '3', 'columns': '3'}
                                                  )
                            )
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Describe your product',
                                                               'rows': '10', 'columns': '1'}
                                                        )
                                  )
    price = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Price Of Product'}
                                                     ),
                            initial='price of goods')


class AccountCreateForm(forms.Form):
    username = forms.CharField(max_length=20, label='Username',
                               min_length=4,
                               initial='',
                               show_hidden_initial=False,
                               widget=forms.TextInput(attrs={'placeholder': 'username'}
                                                      )
                               )
    phone = forms.IntegerField(label='Phone',
                               widget=forms.TextInput(attrs={'placeholder': 'Contact Number', 'max-length': 11},
                                                      )
                               )

    email = forms.EmailField(label='Email',
                             widget=forms.TextInput(attrs={'placeholder': 'Enter a valid email'},
                                                    )
                             )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Input Password'}),
                               label='Password',
                               initial='', help_text="")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password Again'}),
                                       label='Confirm Password')

    # class Meta:
    #     model = Accounts
    #     fields = '__all__'

    def clean_password(self):
        try:
            pword = self.cleaned_data.get('password')
            pattern = re.compile(r'[a-zA-Z0-9@+%$&_.!-]+')
            if len(pword) < 7:
                raise forms.ValidationError("Password must be at least 7 characters")
            if re.match(pattern, pword):
                return pword
            else:
                raise forms.ValidationError('Password not strong', code='password')
        except:
            raise forms.ValidationError('I just said it')

    def clean_confirm_password(self):
        try:
            pword = self.cleaned_data.get('password')
            pword2 = self.cleaned_data.get('confirm_password')
            pattern = re.compile(r'[a-zA-Z0-9@+%$&_.!-]+[a-zA-Z0-9@+%$&_.!-]+[a-zA-Z0-9@+%$&_.!-]+')
            if not re.match(pattern, str(pword)):
                raise forms.ValidationError('Passwords does not match')
            if len(pword) < 7:
                raise forms.ValidationError("Password must be at least 7 characters", code='password1')
            else:
                if pword2 == pword:
                    return pword2
        except:
            raise forms.ValidationError('I just said it')

    def clean_phone(self, *args, **kwargs):
        try:
            phone = self.cleaned_data.get('phone')
            pattern = re.compile(r'[-.]?\d+[-.]?\d+[-.]?\d+[-.]?\d+')
            if re.match(pattern, str(phone)):
                print(phone)
                return phone
            else:
                raise forms.ValidationError('The phone number supplied doesn\'t seem valid')
        except FloatingPointError:
            raise forms.ValidationError('Floating numbers not allowed')

    def clean_email(self, *args, **kwargs):
        try:
            email = self.cleaned_data.get('email')
            pattern = re.compile(r'[a-zA-Z0-9-.+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+')
            if re.match(pattern, email):
                print(email)
                return email
            else:
                print('inactive')
                raise forms.ValidationError('This is not a valid email')
        except LookupError:
            raise forms.ValidationError('Email already exists')





    # def cleaned_data(self):
    #     clean = self.cleaned_data['AccountCreate']
    #     password = self.cleaned_data['password']
    #     confirm_password = self.cleaned_data['confirm_password']
    #
    #     if password != confirm_password:
    #         raise forms.ValidationError('Passwords do not match')
    #     return clean
    #
    # def clean_first_name(self):
    #     first_name = self.cleaned_data['First_name']
    #     return first_name
