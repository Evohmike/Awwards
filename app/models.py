from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
import numpy as np


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Create your models here.

class Profile(models.Model):
    """
    Class that contains Profile details
    """
    user = models.OneToOneField(User,null=True,related_name='profile')
    name = models.CharField(max_length=50)
    profile_photo = models.ImageField(upload_to='images/', blank=True,)
    user_name = models.CharField(max_length=50, null=True)
    occupation = models.CharField(max_length=300, null=True)
    bio = models.TextField(blank=True)

    def save_profile(self):
        self.save()

    def del_profile(self):
        self.delete()

    @classmethod
    def get_by_id(cls, user_id):
            profile = Profile.objects.get(user_id = user_id)
            return profile

    def __str__(self):
        return self.name



class Post(models.Model):
    """
    Class that contains Post details
    """
    title = models.CharField(max_length =60)
    project_image = models.ImageField(upload_to='site-image/',null=True)
    description = models.TextField(blank=True)
    link = models.URLField(max_length = 100)
    uploaded_by = models.ForeignKey(User,null=True,related_name='posts')
    country = models.CharField(max_length=50, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def display_post(cls):
        Post=cls.objects.all()
        return Posts

    @classmethod
    def get_project_by_id(cls, id):
        project = cls.objects.get(id=id)
        return project

    @classmethod
    def get_project_by_user(cls, id):
        project = cls.objects.filter(uploaded_by=id).all()
        return project


    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    def average_design(self):
       all_ratings = list(map(lambda x: x.rating, self.designrating_set.all()))
       return np.mean(all_ratings)

    def average_usability(self):
       all_ratings = list(map(lambda x: x.rating, self.usabilityrating_set.all()))
       return np.mean(all_ratings)

    def average_content(self):
       all_ratings = list(map(lambda x: x.rating, self.contentrating_set.all()))
       return np.mean(all_ratings)


    
class tags(models.Model):
    """
    Class that contains tags details
    """
    post = models.ForeignKey(Post, related_name='tags', null=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.CharField(max_length=50, null=True)


class DesignRating(models.Model):
   RATING_CHOICES = (
       (1, '1'),
       (2, '2'),
       (3, '3'),
       (4, '4'),
       (5, '5'),
       (6, '6'),
       (7, '7'),
       (8, '8'),
       (9, '9'),
       (10, '10')
   )
   project = models.ForeignKey(Post)
   pub_date = models.DateTimeField(auto_now=True)
   profile = models.ForeignKey(Profile)
   rating = models.IntegerField(choices=RATING_CHOICES, default=0)

class ContentRating(models.Model):
   RATING_CHOICES = (
       (1, '1'),
       (2, '2'),
       (3, '3'),
       (4, '4'),
       (5, '5'),
       (6, '6'),
       (7, '7'),
       (8, '8'),
       (9, '9'),
       (10, '10')
   )
   project = models.ForeignKey(Post)
   pub_date = models.DateTimeField(auto_now=True)
   profile = models.ForeignKey(Profile)
   rating = models.IntegerField(choices=RATING_CHOICES, default=0)

class UsabilityRating(models.Model):
   RATING_CHOICES = (
       (1, '1'),
       (2, '2'),
       (3, '3'),
       (4, '4'),
       (5, '5'),
       (6, '6'),
       (7, '7'),
       (8, '8'),
       (9, '9'),
       (10, '10')
   )
   project = models.ForeignKey(Post)
   pub_date = models.DateTimeField(auto_now=True)
   profile = models.ForeignKey(Profile)
   rating = models.IntegerField(choices=RATING_CHOICES, default=0)


class Comment(models.Model):
    comment = models.CharField(max_length =80,null=True)
    user = models.ForeignKey(Profile,null=True)
    post = models.ForeignKey(Post,related_name='comments',blank=True,null=True)
    def __str__(self):
        return self.comment 