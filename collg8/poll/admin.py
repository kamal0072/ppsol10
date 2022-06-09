from django.contrib import admin
from .models import Employee
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city','salary','emp_code','joining_date','address']
    

