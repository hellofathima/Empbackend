from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    age=models.CharField(max_length=30)
    salary=models.CharField(max_length=100)
    email=models.EmailField(null=True)


    def __str__(self):
        return self.name
