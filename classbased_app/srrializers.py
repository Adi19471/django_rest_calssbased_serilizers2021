from rest_framework import  serializers

from .models import Student

class StudentSerilizers(serializers.Serializer):
    class Meta:
        model = Student
        feilds = ['name','company']