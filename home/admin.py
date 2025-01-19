from django.contrib import admin
from .models import Student,Teacher,Courses,Enrollments

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Courses)
admin.site.register(Enrollments)
