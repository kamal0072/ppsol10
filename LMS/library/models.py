from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Books(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    auther_name=models.CharField(max_length=20)
    uploaded_at=models.DateField(auto_now=True)
    books_img=models.ImageField(upload_to="book_images",blank=True)
    book_copy=models.FileField(upload_to='books',blank=True)
