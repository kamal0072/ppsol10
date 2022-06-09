from django.contrib import admin

# Register your models here.
from .models import Books

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display=['id','user','title','auther_name','uploaded_at','books_img','book_copy']
    
