from statistics import mode
from unicodedata import name
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Register(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    def __str__(self):
        return self.email

class BlogModel(models.Model):
    org_name = models.TextField(max_length=255, null=False, default=" ")
    title = models.CharField(max_length=255)
    venue = models.CharField(max_length=255, default="manahari")
    content = FroalaField()
    # content = models.TextField(max_length=10000000)
    # slug = models.SlugField(max_length=1000, null=False, blank=False)
    user = models.ForeignKey(Register, blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now=True)
    event_date = models.DateTimeField(null=False)

    def __str__(self):
        return self.title