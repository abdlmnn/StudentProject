from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
# Create your views here.

def main(request):
    return render(request,'base.html')

def index(request):
    return render(request,'student/index.html',{'title':'Dashboard'})

def student(request):
    return render(request, 'student/student.html',{'title':'Students','student_data': Student.objects.all(), 'course_data':Course.objects.all()})

def course(request):
    return render(request, 'student/course.html',{'title':'Course'})

def subject(request):
    return render(request, 'student/subject.html',{'title':'Subject'})

def yearlevel(request):
    return render(request, 'student/yearlevel.html',{'title':'Year Level'})

def studentyearlevel(request):
    return render(request, 'student/studentyearlevel.html',{'title':'Student Year Level'})

def teacher(request):
    return render(request, 'student/teacher.html',{'title':'Teacher'})

def attendance(request):
    return render(request, 'student/attendance.html',{'title':'Attendance'})

def schedule(request):
    return render(request, 'student/schedule.html',{'title':'Schedule'})






def add_student(request):
    if request.method == 'POST':
        
        Student(firstname=request.POST.get('fname'),
                lastname=request.POST.get('lname'),
                birthday=request.POST.get('birth'),
                gender=request.POST.get('gender'),
                address=request.POST.get('address'),
                contactnumber=request.POST.get('contact'),
                course_id= Course.objects.get(course=request.POST.get('course_id')),
                ).save()
        redirect('student/')
    else:
        return render(request,'student/student.html')