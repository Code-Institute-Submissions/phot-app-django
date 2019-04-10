from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.

class Pictures(models.Model):
    
    picture = models.ImageField(upload_to='img', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now())
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.picture
    

class Categories(models.Model):
    CHOICES = (
        ("nature", "Nature"),
        ("animals", "Animals"),
        ("cars", "Cars"),
        ("cities", "Cities"),
        ("fitness", "Fitness"),
        ("motorcycles", "Motorcycles"),
        ("people", "People"),
        ("space", "Space"),
        ("technology", "Technology"),
        )
    category = models.CharField(max_length=10, choices=CHOICES, default="nature")
    images = models.ForeignKey(Pictures, on_delete=models.SET_NULL, null=True, default="")
    
    def __unicode__(self):
        return self.category
        
        
class CustomUser(AbstractUser):

    full_name = models.CharField(max_length=200, default='')
    profile_picture = models.ImageField(upload_to='img', blank=True, null=True)
    introduction = models.TextField(default='')
    portfolio = models.ForeignKey(Pictures, on_delete=models.SET_NULL, null=True, default="")
    def __unicode__(self):
        return self.email
        
        