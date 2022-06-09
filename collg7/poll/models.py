from django.db import models

class School(models.Model):
    name=models.CharField(max_length=15)
    roll=models.IntegerField()
    address=models.TextField()
    dob=models.DateField()
    adhar=models.BigIntegerField()
