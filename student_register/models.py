from django.db import models

class Code(models.Model):
    department_title = models.CharField(max_length=100)

    def __str__(self):
        return self.department_title

# Create your models here.
class Student(models.Model):
    fullname = models.CharField(max_length=100)
    student_code = models.CharField(max_length=12)
    faculty = models.CharField(max_length=100)
    department = models.ForeignKey(Code, on_delete=models.PROTECT)