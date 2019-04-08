from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    # add additional fields in here
    
    full_name = models.CharField(max_length=200, default='')
    profile_picture = models.ImageField(upload_to='img', blank=True, null=True)
    introduction = models.TextField(default='')
    
    def __unicode__(self):
        return self.email