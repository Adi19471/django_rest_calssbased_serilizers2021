from django.shortcuts import render

# Create your views here.
from .srrializers import StudentSerilizers
from .models import Student
from rest_framework .response import Response
from  rest_framework.views import APIView

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

class Yes(GenericAPIView,ListModelMixin):
   queryset  = Student.objects.all()
   serializer_class = StudentSerilizers
   def get(self,request):
       return  self.list(request)


