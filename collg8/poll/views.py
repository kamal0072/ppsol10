from django.shortcuts import render
from django.db.models import Q,Count
from .models import Employee
def home(request):
    stu_data=Employee.objects.all().annotate(Count('roll'))
    print(stu_data)
    return render(request,'home.html',{"data":stu_data})