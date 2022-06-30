from django.db import models
from django.contrib.auth.models import User
class student(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField()

class Product(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,)
    pro_name=models.CharField(max_length=20)
