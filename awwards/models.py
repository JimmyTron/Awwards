from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=40,blank=True)
    bio = models.TextField(max_length=300)
    prof_pic = models.ImageField(upload_to="profile/")

    def __str__(self):
        return self.username + " " + self.bio 
  

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name + " " + self.description
    