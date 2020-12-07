from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    Text = models.CharField(max_length=16384)
    Title = models.CharField(max_length=100)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Time = models.DateTimeField()