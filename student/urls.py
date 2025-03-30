from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('student/',views.student,name='student'),
    path('course/',views.course,name='course'),
    path('subject/',views.subject,name='subject'),
    path('yearlevel/',views.yearlevel,name='yearlevel'),
    path('studentyearlevel/',views.studentyearlevel,name='studentyearlevel'),
    path('teacher/',views.teacher,name='teacher'),
    path('attendance/',views.attendance,name='attendance'),
    path('schedule/',views.schedule,name='schedule'),


    path('student/add',views.add_student,name='add_student')
]