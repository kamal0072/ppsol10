from django.db import models

class School(models.Model):
    name=models.CharField(max_length=15,null=True,verbose_name="School Name")
    roll=models.IntegerField(default=100,verbose_name="Student Roll No",unique=True)
    address=models.TextField(default="XYZ",verbose_name="School Address")
    dob=models.DateField(verbose_name="Date Of Birth")
    adhar=models.BigIntegerField(unique=True)
    weight=models.FloatField(max_length=10,default=123)
    male=models.BooleanField(default=True)
    email=models.EmailField(default='abc@gmail.com')    
    news_portal=models.URLField(default="https://www.youtube.com/")

class Student(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField()
    address=models.TextField()
    dob=models.DateField()
    adhar=models.BigIntegerField(default=132)
    weight=models.FloatField(max_length=10,default=123)
    male=models.BooleanField(default=True)
    email=models.EmailField(default='')    
    news_portal=models.URLField(default="")
    
