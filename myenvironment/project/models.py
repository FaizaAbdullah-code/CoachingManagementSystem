from django.db import models

# Create your models here.
class Student(models.Model):
    First_name= models.CharField(max_length=200, null=True)
    Last_Name= models.CharField(max_length=200, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    ID_Number=models.IntegerField(max_length=200, null=True)
    attendence=models.CharField(max_length=10, null=True)
    def __str__(self):
         return self.First_name

class Teacher(models.Model):
    # Teacher_First_name= models.CharField(max_length=200, null=True)
    # Teacher_Last_Name= models.CharField(max_length=200, null=True)
    # created=models.DateTimeField(auto_now_add=True, null=True)
    # updated=models.DateTimeField(auto_now=True, null=True)
    # ID_Number=models.IntegerField(max_length=200, null=True)
    # attendence=models.CharField(max_length=10, null=True)

    contactnumber= models.IntegerField(max_length=10, null=True)
    teachersub=models.CharField(max_length=200, null=True)
    contactnumber= models.IntegerField(max_length=10, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    # teaching=models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)