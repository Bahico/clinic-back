from rest_framework import serializers

from account.models import SiteAbout
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        about = SiteAbout.objects.get(id=1)
        about.employee += 1
        about.save()
        return Employee.objects.create(**validated_data)

    class Meta:
        model = Employee
        fields = '__all__'
