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



    path('student/add_student/',views.add_student,name='add_student'),
    path('course/add_course/',views.add_course,name='add_course'),
    path('yearlevel/add_yearlevel/',views.add_yearlevel,name='add_yearlevel'),
    path('studentyearlevel/add_studentyearlevel/',views.add_studentyearlevel,name='add_studentyearlevel'),
    path('subject/add_subject/',views.add_subject,name='add_subject'),
    path('teacher/add_teacher',views.add_teacher,name='add_teacher'),
    path('attendance/add_attendance',views.add_attendance,name='add_attendance'),
    path('schedule/add_schedule',views.add_schedule,name='add_schedule'),


    path('student/read_student/<int:id>',views.read_student,name='read_student'),


    path('student/update_student/<int:id>',views.update_student,name='update_student'),
    path('course/update_course/<int:id>',views.update_course,name='update_course'),
    path('yearlevel/update_yearlevel/<int:id>',views.update_yearlevel,name='update_yearlevel'),
    path('studentyearlevel/update_studentyearlevel/<int:id>',views.update_studentyearlevel,name='update_studentyearlevel'),
    path('subject/update_subject/<int:id>',views.update_subject,name='update_subject'),
    path('teacher/update_teacher/<int:id>',views.update_teacher,name='update_teacher'),
    path('attendance/update_attendance/<int:id>',views.update_attendance,name='update_attendance'),
    path('schedule/update_schedule/<int:id>',views.update_schedule,name='update_schedule'),


    path('student/delete_student/<int:id>',views.delete_student,name='delete_student'),
    path('course/delete_course/<int:id>',views.delete_course,name='delete_course'),
    path('yearlevel/delete_yearlevel/<int:id>',views.delete_yearlevel,name='delete_yearlevel'),
    path('studentyearlevel/delete_studentyearlevel/<int:id>',views.delete_studentyearlevel,name='delete_studentyearlevel'),
    path('subject/delete_subject/<int:id>',views.delete_subject,name='delete_subject'),
    path('teacher/delete_teacher/<int:id>',views.delete_teacher,name='delete_teacher'),
    path('attendance/delete_attendance/<int:id>',views.delete_attendance,name='delete_attendance'),
    path('schedule/delete_schedule/<int:id>',views.delete_schedule,name='delete_schedule'),
]