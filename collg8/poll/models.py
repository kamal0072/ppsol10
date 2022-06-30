from django.db import models
class Employee(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField()
    city=models.CharField(max_length=30)
    salary=models.DecimalField(decimal_places=2,max_digits=20)
    emp_code=models.CharField(max_length=10)
    joining_date=models.DateTimeField()
    address=models.TextField()

    # def __str__(self):
    #     return self.name