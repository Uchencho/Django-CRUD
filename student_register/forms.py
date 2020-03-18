from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("fullname", "faculty", "student_code", "department")
        labels = {
            'fullname': 'Full name',
            'student_code': 'Student Code'
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['department'].empty_label = "Select Department"