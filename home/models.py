from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    grade_level = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Teacher(models.Model):
    first_name=models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    departement=models.CharField(max_length=20)
    hire_date=models.DateField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Courses(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField() 
    credit_hours = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)] )
    teacher = models.ForeignKey(
        'Teacher',  
        on_delete=models.SET_NULL,  # Keep the course if the teacher is deleted
        null=True,  # Permettre une valeur NULL dans la base de données
        blank=True,  # Permettre une valeur vide dans les formulaires
        )
    max_students = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name  

    class Meta:
        verbose_name = "Cours"
        verbose_name_plural = "Cours"
        

class Enrollments(models.Model):
    student = models.ForeignKey(
        'Student',
        on_delete=models.SET_NULL,
        null=True,  
        blank=True  
    )
    course = models.ForeignKey(
        'Courses',
        on_delete=models.SET_NULL,
        null=True,  
        blank=True  
    )
    enrollment_date = models.DateField(auto_now_add=True)  # Date d'inscription automatique
    grade = models.CharField(max_length=10, blank=True, null=True)  # Note (optionnelle)
    STATUS_CHOICES = [
        ('ENROLLED', 'Enrolled'),
        ('COMPLETED', 'Completed'),
        ('DROPPED', 'Dropped'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='ENROLLED')

    def __str__(self):
        return f"{self.student} - {self.course} ({self.status})"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'course'],  # Combinaison unique étudiant + cours
                name='unique_enrollment'  # Nom de la contrainte
            )
        ]
    