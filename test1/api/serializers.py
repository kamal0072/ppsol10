from rest_framework import serializers
from .models import student,Product

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=['id','name','roll']

class ProductSerialize(serializers.ModelSerializer):
    # retrieved_time = serializers.SerializerMethodField()
    # @classmethod
    # def get_retrieved_time(self, object):
    #     """getter method to add field retrieved_time"""
    #     return "Some Value will be here"
    # size=serializers.ReadOnlyField(source="New pizze")
    class Meta:
        model=Product
        fields=('id','user','pro_name')