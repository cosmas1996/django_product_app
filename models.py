from django.db import models
from django.utils import timezone
from django.shortcuts import reverse

class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField('Describe your product', blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    summary = models.TextField(blank=True, null=False)
    date_created = models.DateTimeField(default=timezone.now, editable=False)
    featured = models.BooleanField(default=False, editable=True)  # null=False, default= True

    def get_absolute_url(self):
        return reverse('create', kwargs={'id': self.id})
        # return f"{self.id}/"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Product'


class Accounts(models.Model):
    username = models.CharField(max_length=20, default='')
    phone = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20, default='')
    confirm_password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Accounts'



# Create your models here.
