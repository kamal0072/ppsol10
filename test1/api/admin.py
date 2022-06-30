from django.contrib import admin

# Register your models here.
from .models import student,Product
@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display=["id",'name','roll']
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','user','pro_name']
    
