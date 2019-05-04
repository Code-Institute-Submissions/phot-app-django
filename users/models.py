from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):

    full_name = models.CharField(max_length=200, default='')
    profile_picture = models.ImageField(upload_to='media/img', blank=True, null=True)
    introduction = models.TextField(default='')
    def __unicode__(self):
        return self.email
        
        
class Pictures(models.Model):
    
    picture = models.ImageField(upload_to='img', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now())
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    
    CHOICES = (
        ("nature", "Nature"),
        ("animals", "Animals"),
        ("cars", "Cars"),
        ("cities", "Cities"),
        ("fitness", "Fitness"),
        ("motorcycle", "Motorcycle"),
        ("people", "People"),
        ("space", "Space"),
        ("technology", "Technology"),
        )
    category = models.CharField(max_length=10, choices=CHOICES, default="nature")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    
    def __unicode__(self):
        return self.picture