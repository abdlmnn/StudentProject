from django.db import models

# Create your models here.

class Course(models.Model):
    course = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.course
    

class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(max_length=20)
    address = models.TextField()
    contactnumber = models.CharField(max_length=20)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    

class Teacher(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    section = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.section}"
    

class YearLevel(models.Model):
    yearlevel = models.CharField(max_length=50)

    def __str__(self):
        return self.yearlevel


class StudentYearLevel(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    yearlevel_id = models.ForeignKey(YearLevel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student_id} - {self.yearlevel_id}"


class Schedule(models.Model):
    timestart = models.TimeField()
    timeend = models.TimeField()
    days = models.CharField(max_length=50)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject_id} {self.timestart}-{self.timeend}"
    

class Attendance(models.Model):
    status = models.CharField(max_length=50)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    schedule_id = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.student_id} - {self.status} {self.date}"