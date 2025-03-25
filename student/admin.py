from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(YearLevel)
admin.site.register(StudentYearLevel)
admin.site.register(Schedule)
admin.site.register(Attendance)