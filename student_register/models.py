from django.db import models

class Code(models.Model):
    stud_code = models.CharField(max_length=100)

# Create your models here.
class Student(models.Model):
    fullname = models.CharField(max_length=100)
    student_code = models.CharField(max_length=12)
    faculty = models.CharField(max_length=100)
    #department = models.CharField(max_length=100)
    department = models.ForeignKey(Code, on_delete=models.CASCADE)