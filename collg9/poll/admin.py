from django.contrib import admin
from .models import StudentModel
# Register your models here.
@admin.register(StudentModel)
class StudentModelAdmin(admin.ModelAdmin):
    list_display=['id','name','roll_no','address','email','color','pwd1','pwd2',"state"]
    
