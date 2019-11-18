from django.db import models
from django.contrib.auth.forms import User
import uuid


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token_id = models.UUIDField(default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='profile_pics', max_length=30, blank=True, default='profile_pics/user.png')
    date_created = models.DateTimeField(auto_now_add=True, editable=False)


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'UsersImage'



# Create your models here.
