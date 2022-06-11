from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=40,blank=True)
    bio = models.TextField(max_length=300)
    prof_pic = models.ImageField(upload_to="profile/")
    owner = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile',)