from django.db import models

# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  first_name = models.CharField(max_length=40)
  last_name = models.CharField(max_length=30)
  profile_picture = models.ImageField(upload_to='users/')
  bio = models.TextField(default="I love Awward!")
  pub_date_created = models.DateTimeField(auto_now_add=True, null=True)


