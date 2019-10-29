from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(blank=False)
    first_name = models.CharField(max_length=200, default='name')
    password1 = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(upload_to='profile_pics')

    class Meta:
        verbose_name_plural = 'Users'


# Create your models here.
