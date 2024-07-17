from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , null=True )
    email = models.CharField(max_length=80 , unique=True , null=True)
    bio = models.TextField(blank=True , null=True)
    profile_img = models.ImageField(upload_to="profile_imgs" , default="user.png" , blank=True , null=True)
    location = models.CharField(max_length=80 , unique=True , null=True)
    GENDER = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )
    gender = models.CharField(max_length=10 , choices=GENDER , blank=True , null=True)