from django.db import models



class Comment(models.Model):
    name = models.CharField(max_length=50, default="")
    comment = models.TextField(max_length=250, default="")