from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    # email=models.EmailField()

class Extra(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    age=models.IntegerField()
    business=models.CharField(max_length=500)
