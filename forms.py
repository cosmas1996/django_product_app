from django import forms
from Products.models import Product
from django.core.exceptions import ValidationError



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'image']




#
# class ProductForm(forms.Form):
#     title = forms.CharField(max_length=20, min_length=3,
#                             widget=forms.Textarea(attrs={'placeholder': 'Title of Product',
#                                                          'rows': '3', 'columns': '3'},
#                                                   )
#                             )
#     description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Describe your product',
#                                                                'rows': '10', 'columns': '1'}
#                                                         )
#                                   )
#
#     price = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Price Of Product'}
#                                                      ),
#                             initial='price of goods')
#
#     image = forms.ImageField(widget=forms.ClearableFileInput, max_length=None, allow_empty_file=True, required=False)
