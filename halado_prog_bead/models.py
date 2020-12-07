from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    Text = models.CharField(max_length=16384)
    Author = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    Time = models.DateTimeField()