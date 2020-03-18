from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def student_list(request):
    """
    
    """
    return render(request, "student_register/student_list.html")

def student_form(request):
    """
    Insert and update function
    """
    form = StudentForm()
    return render(request, "student_register/student_form.html", {'form' : form})

def student_delete(request):
    """
    Delete function
    """
    return

