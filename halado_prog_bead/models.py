from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class Post(models.Model):
    Text = models.CharField(max_length=16384)
    Author = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    Time = models.DateTimeField()


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()

