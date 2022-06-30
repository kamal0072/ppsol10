from django.contrib import admin
from .models import School,Student

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','address','dob','adhar','weight','male','email','news_portal']
    

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','address','dob',]
    
