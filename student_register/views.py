from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

# Create your views here.
def student_list(request):
    """
    
    """
    context = {'student_list': Student.objects.all()}
    return render(request, "student_register/student_list.html", context)

def student_form(request, id=0):
    """
    Insert and update function
    """
    if request.method == "GET":
        if id==0:
            form = StudentForm()
        else:
            the_id = Student.objects.get(pk=id)
            form = StudentForm(instance=the_id)
        return render(request, "student_register/student_form.html", {'form' : form})
    else:
        if id == 0:
            form = StudentForm(request.POST)
        else:
            the_id = Student.objects.get(pk=id)
            form = StudentForm(request.POST, instance=the_id)
        if form.is_valid():
            form.save()
        return redirect('/list')
def student_delete(request, id):
    """
    Delete function
    """
    the_id = Student.objects.get(pk=id)
    the_id.delete()
    return redirect('/list')
