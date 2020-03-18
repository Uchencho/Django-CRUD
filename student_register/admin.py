from django.contrib import admin

# Register your models here.
from .models import Code, Student

class CodeAdmin(admin.ModelAdmin):
    list_display = ["department_title"] #List_display is a django key-word

class StudentAdmin(admin.ModelAdmin):
    list_display = ["fullname", "student_code", "faculty"] #List_display is a django key-word

admin.site.register(Code, CodeAdmin)
admin.site.register(Student, StudentAdmin)