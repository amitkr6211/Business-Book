from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class MyList2(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    spending=models.IntegerField()
    date_posted=models.DateTimeField(default=timezone.now)
    des=models.CharField(max_length=500)
