from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class newtable(models.Model):
    name = models.CharField(max_length=256,unique=True)
    def __str__(self):
        return self.name

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    site_portfolio =  models.URLField(blank = True)
    profile_picture = models.ImageField(blank = True, upload_to = 'profile_pics')

    def __str__(self):
        return self.user.username
