from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class History(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    search = models.CharField( max_length=500)
    date = models.DateTimeField(  auto_now_add=True)