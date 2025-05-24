from rest_framework import serializers
from .models import Company, Employee

# creating serializers here 

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    comp_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = "__all__"
        
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"