from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

# Create your views here.
def student_list(request):
    """
    
    """
    context = {'student_list': Student.objects.all()}
    return render(request, "student_register/student_list.html", context)

def student_form(request):
    """
    Insert and update function
    """
    if request.method == "GET":
        form = StudentForm()
        return render(request, "student_register/student_form.html", {'form' : form})
    else:
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/list')
def student_delete(request):
    """
    Delete function
    """
    return
