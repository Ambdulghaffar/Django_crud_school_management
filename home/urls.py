
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    # For the students class 
    path('students/', views.students, name='students' ),
    path('students/add_students/', views.add_students, name='add_students' ),
    path('students/update_students/<int:student_id>/', views.update_students, name='update_students' ),
    path('students/delete_students/<int:student_id>/', views.delete_students, name='delete_students'),
    
    # For the teachers class 
    path('teachers/', views.teachers, name='teachers' ),
    path('teachers/add_teachers/', views.add_teachers, name='add_teachers'),
    path('teachers/update_teachers/<int:teacher_id>/', views.update_teachers, name='update_teachers' ),
    path('teachers/delete_teachers/<int:teacher_id>/', views.delete_teachers, name='delete_teachers' ),
    
    # For the courses class  
    path('courses/', views.courses, name='courses' ),
    path('courses/add_courses/', views.add_courses, name='add_courses' ),
    path('courses/update_courses/<int:course_id>/', views.update_courses, name='update_courses' ),
    path('courses/delete_courses/<int:course_id>/', views.delete_courses, name='delete_courses' ),
    
    # For the Enrollments class
    path('enrollments/', views.enrollments, name='enrollments' ),
    path('enrollments/add_enrollments/', views.add_enrollments, name='add_enrollments' ),
    path('enrollments/update_enrollments/<int:enrollment_id>/', views.update_enrollments, name='update_enrollments' ),
    path('enrollments/delete_enrollments/<int:enrollment_id>/', views.delete_enrollments, name='delete_enrollments' ),
     
    
]
