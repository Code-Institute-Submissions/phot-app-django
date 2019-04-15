from django.db import models
from users.models import CustomUser, Pictures

class Comment(models.Model):
    name = models.CharField(max_length=50, default="")
    comment = models.TextField(max_length=250, default="")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    picture = models.ForeignKey(Pictures, on_delete=models.CASCADE, default=1)