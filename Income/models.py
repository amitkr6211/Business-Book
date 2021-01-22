from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class MyList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    income=models.IntegerField()
    date_posted=models.DateTimeField(default=timezone.now)
    des=models.CharField(max_length=500)

    def __str__(self):
        return self.des


