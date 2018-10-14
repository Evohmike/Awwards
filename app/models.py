from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  first_name = models.CharField(max_length=40)
  last_name = models.CharField(max_length=30)
  profile_picture = models.ImageField(upload_to='users/')
  bio = models.TextField(default="I love Awward!")
  pub_date_created = models.DateTimeField(auto_now_add=True, null=True)

  def __str__(self):
        return self.first_name


class Profile(models.Model):
    user = models.OneToOneField(User,null=True,related_name='profile')
    name = models.CharField(max_length=50)
    profile_photo = models.ImageField(upload_to='images/', blank=True,)
    user_name = models.CharField(max_length=50, null=True)
    occupation = models.CharField(max_length=300, null=True)
    bio = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.first_name

    