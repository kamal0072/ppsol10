from django.shortcuts import render
from .models import student,Product
from .serializers import StudentSerializer,ProductSerialize
from rest_framework import viewsets

class Stu_views(viewsets.ModelViewSet):
    queryset=student.objects.all()
    serializer_class=StudentSerializer

class Product_view(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerialize