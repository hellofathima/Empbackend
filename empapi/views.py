from django.shortcuts import render,redirect

# Create your views here.
from empapi.serializers import EmpSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet,ModelViewSet
from empapi.models import Employee

class Empview(ModelViewSet):
    
    serializer_class=EmpSerializer
    
    model=Employee
    queryset=Employee.objects.all()