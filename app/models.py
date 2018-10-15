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
    user = models.OneToOneField(User,null=True,related_name='profile')
    name = models.CharField(max_length=50)
    profile_photo = models.ImageField(upload_to='images/', blank=True,)
    user_name = models.CharField(max_length=50, null=True)
    occupation = models.CharField(max_length=300, null=True)
    bio = models.TextField(blank=True)


    

    def __str__(self):
        return self.first_name


class Post(models.Model):
    uploaded_by = models.ForeignKey(User,null=True,related_name='posts')
    country = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=200, null=True)
    project_image = models.ImageField(upload_to='site-image/',null=True)
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def display_projects(cls):
        Post=cls.objects.all()
        return Posts






class tags(models.Model):
    post = models.ForeignKey(Post, related_name='tags', null=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.CharField(max_length=50, null=True)
