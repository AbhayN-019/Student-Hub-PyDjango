from django.shortcuts import render,redirect,get_object_or_404
from stdhub_app.models import Student
from stdhub_app.forms import StudentForm
from django.contrib import messages

# Create your views here.
def greet(request):
    return render(request,'greet.html')

def student_create(request):
    
    if request.method == "POST":
        S_form = StudentForm(request.POST,request.FILES)
        
        if S_form.is_valid():
            S_form.save()
            messages.success(request,'Student Details Created Successfully')
            return redirect('student_list')
    
    else:
        S_form = StudentForm()
    return render(request, 'student_form.html', {"S_form": S_form})

def student_list(request):
    data = Student.objects.all()
    return render(request, 'student_list.html', {"students": data})

def view_single_student(request,id):
    std = get_object_or_404(Student,id=id)
    return render(request,'single_student.html',{'std':std})

def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    
    if request.method == "POST":
        S_form = StudentForm(request.POST,request.FILES ,instance=student)
        
        if S_form.is_valid():
            S_form.save()
            return redirect('student_list')
        else:
            messages.error(request,'Please provide valid student details.')
    else:
        S_form = StudentForm(instance=student)
    return render(request, 'update_student.html', {"S_form": S_form})

def student_delete(request,id):
    student = Student.objects.filter(id=id).first()

    if student:
        student.delete()
        messages.success(request, "Student deleted successfully.")
    else:
        messages.error(request, "Student not found. Deletion failed.")

    return redirect('student_list')