from django.db import models

class Books(models.Model):
    name=models.CharField(max_length=20)
    picture=models.ImageField(upload_to="images")
    auther=models.CharField(max_length=20,default="chetan bhagat.")
    email=models.EmailField(default="abc@gmail.com")
    desc=models.TextField(default="Library for books!!!")
    