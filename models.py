from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator


class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField('Describe your product', blank=True, null=True)
    price = models.FloatField()
    date_created = models.DateTimeField(default=timezone.now, editable=False)
    image = models.ImageField(upload_to='product_images', blank=True, help_text='Image of your product')

    def get_absolute_url(self):
        return reverse('create', kwargs={'id': self.id})
        # return f"{self.id}/"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Product'

#
# class Accounts(models.Model):
#     username = models.CharField(max_length=200, blank=False)
#     email = models.EmailField(unique=True, blank=False)
#     password = models.CharField(max_length=100, blank=False)
#     password1 = models.CharField(max_length=100, blank=False)
#     date_registered = models.DateTimeField(auto_now_add=True, editable=False)

    #
    # class Meta:
    #     verbose_name_plural = 'Accounts'



USERNAME_REGEX = r'[a-zA-Z0-9]+'

