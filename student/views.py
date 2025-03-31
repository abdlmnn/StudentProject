from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
# Create your views here.

def main(request):
    return render(request,'base.html')





def index(request):
    return render(request,'student/index.html',{'title':'Dashboard'})

def student(request):
    return render(request, 'student/student.html',{'title':'Students','student_data': Student.objects.all(), 'course_data':Course.objects.all()})

def course(request):
    return render(request, 'student/course.html',{'title':'Course','course_data':Course.objects.all()})

def subject(request):
    return render(request, 'student/subject.html',{'title':'Subject','subject_data':Subject.objects.all()})

def yearlevel(request):
    return render(request, 'student/yearlevel.html',{'title':'Year Level','yearlevel_data': YearLevel.objects.all()})

def studentyearlevel(request):
    return render(request, 'student/studentyearlevel.html',{'title':'Student Year Level','studentyearlevel_data':StudentYearLevel.objects.all(),'yearlevel_data': YearLevel.objects.all(),'student_data': Student.objects.all()})

def teacher(request):
    return render(request, 'student/teacher.html',{'title':'Teacher','teacher_data':Teacher.objects.all()})

def attendance(request):
    return render(request, 'student/attendance.html',{'title':'Attendance','attendance_data':Attendance.objects.all(),'student_data': Student.objects.all(),'schedule_data':Schedule.objects.all()})

def schedule(request):
    return render(request, 'student/schedule.html',{'title':'Schedule','schedule_data':Schedule.objects.all(),'subject_data': Subject.objects.all(),'teacher_data':Teacher.objects.all()})





def add_student(request):
    if request.method == 'POST':

        if not request.POST.get('fname').strip():
            return redirect('/student/')
        
        Student(
            firstname=request.POST.get('fname'),
            lastname=request.POST.get('lname'),
            birthday=request.POST.get('birth'),
            gender=request.POST.get('gender'),
            address=request.POST.get('address'),
            contactnumber=request.POST.get('contact'),
            course_id=Course.objects.get(id=request.POST.get('course_id')),
            ).save()
        
        return redirect('/student/')
    else:
        return render(request,'student/student.html')
    
def add_course(request):
    if request.method == 'POST':

        if not request.POST.get('course').strip():
            return redirect('/course/')

        Course(
            course=request.POST.get('course'),
            description=request.POST.get('description'),
        ).save()

        return redirect('/course/')
    else:
        return render(request,'student/course.html')
    
def add_subject(request):
    if request.method == 'POST':
        if not request.POST.get('name').strip():
            return redirect('/subject/')
        Subject(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            section=request.POST.get('section'),
        ).save()
        return redirect('/subject/')
    else:
        return render(request,'student/subject.html')

def add_yearlevel(request):
    if request.method == 'POST':

        if not request.POST.get('yearlevel').strip():
            return redirect('/yearlevel/')
        
        YearLevel(
            yearlevel=request.POST.get('yearlevel')
        ).save()

        return redirect('/yearlevel/')

    else:
        return render(request,'student/yearlevel.html')

def add_studentyearlevel(request):
    if request.method == 'POST':
        StudentYearLevel(
            student_id = Student.objects.get(id=request.POST.get('student_id')),
            yearlevel_id = YearLevel.objects.get(id=request.POST.get('yearlevel_id')),
        ).save()
        return redirect('/studentyearlevel/')
    else:
        return render(request,'student/studentyearlevel.html')

def add_teacher(request):
    if request.method == 'POST':
        if not request.POST.get('fname').strip():
            return redirect('/teacher/')
        Teacher(
            firstname=request.POST.get('fname'),
            lastname=request.POST.get('lname'),
        ).save()
        return redirect('/teacher/')
    else:
        return render(request,'student/teacher.html')
    
def add_attendance(request):
    if request.method == 'POST':
        Attendance(
            status=request.POST['status'],
            student_id=Student.objects.get(id=request.POST.get('student_id')),
            schedule_id=Schedule.objects.get(id=request.POST.get('schedule_id')),
            date=request.POST['date'],
            time=request.POST['time'],
        ).save()
        return redirect('/attendance/')
    else:
        return render(request,'student/attendance.html')

def add_schedule(request):
    if request.method == 'POST':
        Schedule(
            timestart=request.POST['timestart'],
            timeend=request.POST['timeend'],
            days=request.POST['days'],
            subject_id=Subject.objects.get(id=request.POST.get('subject_id')),
            teacher_id=Teacher.objects.get(id=request.POST.get('teacher_id')),
        ).save()
        return redirect('/schedule/')
    else:
        return render(request,'student/schedule.html')
            

def read_student(request,id):
    return render(request,'student/read_student.html',{'title':'Read','student_data':Student.objects.get(id=id)})





def update_student(request,id):
    if request.method == 'POST':

        if not request.POST.get('fname').strip():
            return redirect('/student/')
        data = Student.objects.get(id=id)
        data.firstname = request.POST['fname']
        data.lastname = request.POST['lname']
        data.birthday = request.POST['birth']
        data.gender = request.POST['gender']
        data.contactnumber = request.POST['contact']
        data.course_id = Course.objects.get(id=request.POST.get('course_id'))
        data.save()
        return redirect('/student/')
    else:
        return render(request,'student/update_student.html',{'title':'Update','student':Student.objects.get(id=id),'course':Course.objects.all()})

def update_course(request,id):
    if request.method == 'POST':

        if not request.POST.get('course').strip():
             return redirect('/course/')
        data = Course.objects.get(id=id)
        data.course = request.POST['course']
        data.description = request.POST['description']
        data.save()
        return redirect('/course/')
    else:
        return render(request,'student/update_course.html',{'course':Course.objects.get(id=id)})

def update_subject(request,id):
    if request.method == 'POST':
        if not request.POST.get('name').strip():
            return redirect('/subject/')
        data = Subject.objects.get(id=id)
        data.name = request.POST['name']
        data.description = request.POST['description']
        data.section = request.POST['section']
        data.save()
        return redirect('/subject/')
    else:
        return render(request,'student/update_subject.html',{'data':Subject.objects.get(id=id)})

def update_yearlevel(request,id):
    if request.method == 'POST':

        if not request.POST.get('yearlevel').strip():
            return redirect('/yearlevel/')
        
        data = YearLevel.objects.get(id=id)

        data.yearlevel = request.POST['yearlevel']

        data.save()

        return redirect('/yearlevel/')
    else:
        return render(request,'student/update_yearlevel.html',{'data':YearLevel.objects.get(id=id)})

def update_studentyearlevel(request,id):
    if request.method == 'POST':
        data = StudentYearLevel.objects.get(id=id)
        data.student_id = Student.objects.get(id=request.POST.get('student_id'))
        data.yearlevel_id = YearLevel.objects.get(id=request.POST.get('yearlevel_id'))
        data.save()
        return redirect('/studentyearlevel/')
    else:
        return render(request,'student/update_studentyearlevel.html',{'title':'Update','studentyearlevel_data':StudentYearLevel.objects.get(id=id),'yearlevel_data': YearLevel.objects.all(),'student_data': Student.objects.all()})

def update_teacher(request,id):
    if request.method == 'POST':
        if not request.POST['fname'].strip():
            return redirect('/teacher/')
        data = Teacher.objects.get(id=id)
        data.firstname = request.POST['fname']
        data.lastname = request.POST['lname']
        data.save()
        return redirect('/teacher/')
    else:
        return render(request,'student/update_teacher.html',{'title':'Update','data':Teacher.objects.get(id=id)})

def update_attendance(request,id):
    if request.method == 'POST':
        data = Attendance.objects.get(id=id)
        data.status = request.POST['status']
        data.student_id = Student.objects.get(id=request.POST.get('student_id'))
        data.schedule_id = Schedule.objects.get(id=request.POST.get('schedule_id'))
        data.date = request.POST['date']
        data.time = request.POST['time']
        data.save()
        return redirect('/attendance/')
    else:
        return render(request,'student/update_attendance.html',{'title':'Update','data':Attendance.objects.get(id=id),'student_data': Student.objects.all(),'schedule_data':Schedule.objects.all()})

def update_schedule(request,id):
    if request.method == 'POST':
        data = Schedule.objects.get(id=id)
        data.timestart = request.POST['timestart']
        data.timeend = request.POST['timeend']
        data.days = request.POST['days']
        data.subject_id=Subject.objects.get(id=request.POST.get('subject_id'))
        data.teacher_id=Teacher.objects.get(id=request.POST.get('teacher_id'))
        data.save()
        return redirect('/schedule/')
    else:
        return render(request,'student/update_schedule.html',{'title':'Update','data':Schedule.objects.get(id=id),'subject_data': Subject.objects.all(),'teacher_data':Teacher.objects.all()})



def delete_student(request,id):
    Student.objects.get(id=id).delete()
    return redirect('/student/')

def delete_course(request,id):
    Course.objects.get(id=id).delete()
    return redirect('/course/')

def delete_yearlevel(request,id):
    YearLevel.objects.get(id=id).delete()
    return redirect('/yearlevel/')

def delete_subject(request,id):
    Subject.objects.get(id=id).delete()
    return redirect('/subject/')

def delete_studentyearlevel(request,id):
    StudentYearLevel.objects.get(id=id).delete()
    return redirect('/studentyearlevel/')

def delete_teacher(request,id):
    Teacher.objects.get(id=id).delete()
    return redirect('/teacher/')

def delete_attendance(request,id):
    Attendance.objects.get(id=id).delete()
    return redirect('/attendance/')

def delete_schedule(request,id):
    Schedule.objects.get(id=id).delete()
    return redirect('/schedule/')