from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseNotAllowed
from django.http import HttpRequest
from django.contrib import messages
from django.db import IntegrityError
from .models import Student, Teacher, Courses, Enrollments

# Create your views here.
def index(request):
    return render(request,'home/index.html')
 
# pour la classe etudiant   
def  students(request):
    students=Student.objects.all() 
    return render(request,'home/Students/students.html',{'students': students})

def  add_students(request: HttpRequest):
    if request.method == 'POST':  # Ici, vous pouvez accéder à POST
        # Récupérer les données du formulaire
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        grade_level = request.POST.get('grade_level')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        # Vérifier si l'email est valide (doit finir par @gmail.com)
        if not email.endswith('@gmail.com'):
            messages.error(request, "L'email doit finir par @gmail.com.")
            return render(request, 'home/Students/add_students.html', {
                'form_data': request.POST  # Passer les données du formulaire au template
            })
        
        # Vérifier si le téléphone contient uniquement des chiffres
        if not phone.isdigit():
            messages.error(request, "Le numéro de téléphone doit contenir uniquement des chiffres.")
            return render(request, 'home/Students/add_students.html', {
                'form_data': request.POST  # Passer les données du formulaire au template
            })
        
        # Vérifier si l'email ou le téléphone existe déjà
        if Student.objects.filter(email=email).exists():
            messages.error(request,"L'email est déjà utilisé. Veuillez en saisir un autre.")
            return render(request, 'home/Students/add_students.html', {
                'form_data': request.POST  # Passer les données du formulaire au template
            })
        
        if Student.objects.filter(phone=phone).exists():
            messages.error(request,"Le numéro de téléphone est déjà utilisé. Veuillez en saisir un autre.")

        # Créer un nouvel étudiant et l'enregistrer dans la base de données
        
        try:
            student = Student(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                grade_level=grade_level,
                email=email,
                phone=phone,
                address=address
            )
            student.save()

            # Message de succès
            messages.success(request, "L'étudiant a été ajouté avec succès.")
            # Rediriger vers la page des étudiants après l'ajout
            return redirect('students')
        
        except IntegrityError as e:
            # Gestion de l'exception d'intégrité si un autre problème se produit
            messages.error(request, "")
            return render(request, 'home/Students/add_students.html', {
                'form_data': request.POST  # Passer les données du formulaire au template
            })
   
    return render(request,'home/Students/add_students.html')


def update_students(request: HttpRequest, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        # Récupérer les données du formulaire
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        grade_level = request.POST.get('grade_level')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        # Valider l'email
        if not email.endswith("@gmail.com"):
            messages.error(request, "L'email doit se terminer par '@gmail.com'.")
            return render(request, 'home/Students/update_students.html', {'student': student})
        
        # Valider le numéro de téléphone
        if not phone.isdigit():
            messages.error(request, "Le numéro de téléphone ne doit contenir que des chiffres.")
            return render(request, 'home/Students/update_students.html', {'student': student})

        # Si toutes les validations passent, enregistrer les modifications
        student.first_name = first_name
        student.last_name = last_name
        student.date_of_birth = date_of_birth
        student.grade_level = grade_level
        student.email = email
        student.phone = phone
        student.address = address

        student.save()

        # Ajouter un message de succès et rediriger
        messages.success(request, "Les informations de l'étudiant ont été modifiées avec succès.")
        return redirect('students')

    return render(request, 'home/Students/update_students.html', {'student': student})



def delete_students(request:HttpRequest, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        student.delete()
        messages.success(request, "L'étudiant a été supprimé avec succès.")
        return redirect('students')
    
    return redirect('students')





def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'home/Teachers/teachers.html', {'teachers': teachers})

def add_teachers(request: HttpRequest):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        departement = request.POST.get('departement')
        hire_date = request.POST.get('hire_date')

        # Vérifier si l'email est valide (doit finir par @gmail.com)
        if not email.endswith('@gmail.com'):
            messages.error(request, "L'email doit finir par @gmail.com.")
            return render(request, 'home/Teachers/add_teachers.html', {
                'form_data': request.POST  # Passer les données du formulaire au template
            })

        # Vérifier si le téléphone contient uniquement des chiffres
        if not phone.isdigit():
            messages.error(request, "Le numéro de téléphone doit contenir uniquement des chiffres.")
            return render(request, 'home/Teachers/add_teachers.html', {
                'form_data': request.POST  
            })

        # Check if the email or phone number already exists
        if Teacher.objects.filter(email=email).exists():
            messages.error(request, "L'email est déjà utilisé. Veuillez en saisir un autre.")
            return render(request, 'home/Teachers/add_teachers.html', {
                'form_data': request.POST  
            })

        if Teacher.objects.filter(phone=phone).exists():
            messages.error(request, "Le numéro de téléphone est déjà utilisé. Veuillez en saisir un autre.")
            return render(request, 'home/Teachers/add_teachers.html', {
                'form_data': request.POST  
            })

        # Create a new student and recording in the database
        try:
            teacher = Teacher(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                departement=departement,
                hire_date=hire_date
            )
            teacher.save()

           
            messages.success(request, "L'enseignant a été ajouté avec succès.")
            return redirect('teachers')

        except IntegrityError as e:
            # Gestion de l'exception d'intégrité si un autre problème se produit
            messages.error(request, f"Une erreur s'est produite lors de l'ajout de l'enseignant : {str(e)}")
            return render(request, 'home/Teachers/add_teachers.html', {
                'form_data': request.POST  
            })

    return render(request, 'home/Teachers/add_teachers.html')

def update_teachers(request: HttpRequest, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':
       
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        departement = request.POST.get('departement')
        hire_date = request.POST.get('hire_date')

        
        if not email.endswith("@gmail.com"):
            messages.error(request, "L'email doit se terminer par '@gmail.com'.")
            return render(request, 'home/Teachers/update_teachers.html', {'teacher': teacher})

       
        if not phone.isdigit():
            messages.error(request, "Le numéro de téléphone ne doit contenir que des chiffres.")
            return render(request, 'home/Teachers/update_teachers.html', {'teacher': teacher})

      
        teacher.first_name = first_name
        teacher.last_name = last_name
        teacher.email = email
        teacher.phone = phone
        teacher.departement = departement
        teacher.hire_date = hire_date

        teacher.save()


        messages.success(request, "Les informations de l'enseignant ont été modifiées avec succès.")
        return redirect('teachers')

    return render(request, 'home/Teachers/update_teachers.html', {'teacher': teacher})

def delete_teachers(request: HttpRequest, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.method == 'POST':
        teacher.delete()
        messages.success(request, "L'enseignant a été supprimé avec succès.")
        return redirect('teachers')

    # Renvoyer une réponse HTTP 405 (Méthode non autorisée)
    return HttpResponseNotAllowed(['POST'])



def  courses(request):
    courses=Courses.objects.all()
    return render(request,'home/Courses/courses.html',{'courses':courses})


def add_courses(request:HttpRequest):
    # Récupérer tous les enseignants
    teachers = Teacher.objects.all()

    if request.method == 'POST':
        # Récupérer les données du formulaire
        name = request.POST.get('name')
        description = request.POST.get('description')
        credit_hours = request.POST.get('credit_hours')
        teacher_id = request.POST.get('teacher')
        max_students = request.POST.get('max_students')

        # Validation des données
        if not name or not description or not credit_hours or not max_students or not teacher_id:
            messages.error(request, "Tous les champs obligatoires doivent être remplis.")
            return render(request, 'home/Courses/add_courses.html', {
                'form_data': request.POST,  # Passer les données soumises
                'teachers': teachers  # Passer la liste des enseignants
            })

        try:
            credit_hours = int(credit_hours)
            max_students = int(max_students)
        except ValueError:
            messages.error(request, "Les heures de crédit et le nombre maximal d'étudiants doivent être des nombres valides.")
            return render(request, 'home/Courses/add_courses.html', {
                'form_data': request.POST,  # Passer les données soumises
                'teachers': teachers  # Passer la liste des enseignants
            })

        # Vérifier si l'enseignant existe
        teacher = None
        if teacher_id:
            try:
                teacher = Teacher.objects.get(id=teacher_id)
            except Teacher.DoesNotExist:
                messages.error(request, "L'enseignant sélectionné n'existe pas.")
                return render(request, 'home/Courses/add_courses.html', {
                    'form_data': request.POST,  # Passer les données soumises
                    'teachers': teachers  # Passer la liste des enseignants
                })

        # Créer et enregistrer le cours
        course = Courses(
            name=name,
            description=description,
            credit_hours=credit_hours,
            teacher=teacher,
            max_students=max_students
        )
        course.save()

        messages.success(request, "Le cours a été ajouté avec succès.")
        return redirect('courses')

    # Si la méthode est GET, afficher le formulaire
    return render(request, 'home/Courses/add_courses.html', {'teachers': teachers})



def update_courses(request:HttpRequest, course_id):
    # Récupérer le cours à modifier
    course = get_object_or_404(Courses, id=course_id)
    # Récupérer tous les enseignants
    teachers = Teacher.objects.all()

    if request.method == 'POST':
        # Récupérer les données du formulaire
        name = request.POST.get('name')
        description = request.POST.get('description')
        credit_hours = request.POST.get('credit_hours')
        teacher_id = request.POST.get('teacher')
        max_students = request.POST.get('max_students')
        status = request.POST.get('status') == 'True'  

        # Validation des données
        if not name or not description or not credit_hours or not max_students or not teacher_id:
            messages.error(request, "Tous les champs obligatoires doivent être remplis.")
            return render(request, 'home/Courses/update_courses.html', {
                'course': course,  # Passer le cours à modifier
                'teachers': teachers  # Passer la liste des enseignants
            })

        try:
            credit_hours = int(credit_hours)
            max_students = int(max_students)
        except ValueError:
            messages.error(request, "Les heures de crédit et le nombre maximal d'étudiants doivent être des nombres valides.")
            return render(request, 'home/Courses/update_courses.html', {
                'course': course,  # Passer le cours à modifier
                'teachers': teachers  # Passer la liste des enseignants
            })

        # Vérifier si l'enseignant existe
        teacher = None
        if teacher_id:
            try:
                teacher = Teacher.objects.get(id=teacher_id)
            except Teacher.DoesNotExist:
                messages.error(request, "L'enseignant sélectionné n'existe pas.")
                return render(request, 'home/Courses/update_courses.html', {
                    'course': course,  # Passer le cours à modifier
                    'teachers': teachers  # Passer la liste des enseignants
                })

        # Mettre à jour le cours
        course.name = name
        course.description = description
        course.credit_hours = credit_hours
        course.teacher = teacher
        course.max_students = max_students
        course.status=status
        course.save()

        messages.success(request, "Le cours a été modifié avec succès.")
        return redirect('courses')

    # Si la méthode est GET, afficher le formulaire de modification
    return render(request, 'home/Courses/update_courses.html', {
        'course': course,  # Passer le cours à modifier
        'teachers': teachers  # Passer la liste des enseignants
    })

def delete_courses(request: HttpRequest, course_id):
    course = get_object_or_404(Courses, id=course_id)

    if request.method == 'POST':
        course.delete()
        messages.success(request, "Le cours a été supprimé avec succès.")
        return redirect('courses')

    # Renvoyer une réponse HTTP 405 (Méthode non autorisée)
    return HttpResponseNotAllowed(['POST'])


def  enrollments(request):
    enrollments=Enrollments.objects.all()
    return render(request,'home/Enrollments/enrollments.html',{'enrollments':enrollments})



def add_enrollments(request:HttpRequest):
    
    students = Student.objects.all()
    courses = Courses.objects.all()

    if request.method == 'POST':
        student_id = request.POST.get('student')
        course_id = request.POST.get('course')
        enrollment_date = request.POST.get('enrollment_date')
        grade = request.POST.get('grade')

        if not student_id or not course_id or not enrollment_date:
            messages.error(request, "Tous les champs obligatoires doivent être remplis.")
            return render(request, 'home/Enrollments/add_enrollments.html', {
                'students': students,
                'courses': courses,
                'form_data': request.POST  
            })

        try:
            student = Student.objects.get(id=student_id)
            course = Courses.objects.get(id=course_id)
        except (Student.DoesNotExist, Courses.DoesNotExist):
            messages.error(request, "L'étudiant ou le cours sélectionné n'existe pas.")
            return render(request, 'home/Enrollments/add_enrollments.html', {
                'students': students,
                'courses': courses,
                'form_data': request.POST  
            })
        
                # Vérifier si l'étudiant est déjà inscrit à ce cours
        if Enrollments.objects.filter(student=student, course=course).exists():
            messages.error(request, "Cet étudiant est déjà inscrit à ce cours. Veuillez choisir un autre cours.")
            return render(request, 'home/Enrollments/add_enrollments.html', {
                'students': students,
                'courses': courses,
                'form_data': request.POST  
            })

        enrollment = Enrollments(
            student=student,
            course=course,
            enrollment_date=enrollment_date,
            grade=grade
        )
        enrollment.save()

        messages.success(request, "L'inscription a été ajoutée avec succès.")
        return redirect('enrollments')

    # Si la méthode est GET, afficher le formulaire
    return render(request, 'home/Enrollments/add_enrollments.html', {
        'students': students,
        'courses': courses
    })
    
    
def update_enrollments(request:HttpRequest, enrollment_id):
    enrollment = get_object_or_404(Enrollments, id=enrollment_id)
    courses = Courses.objects.all()

    if request.method == 'POST':
        course_id = request.POST.get('course')
        enrollment_date = request.POST.get('enrollment_date')
        grade = request.POST.get('grade')
        status = request.POST.get('status')

        if not course_id or not enrollment_date or not status:
            messages.error(request, "Tous les champs obligatoires doivent être remplis.")
            return render(request, 'home/Enrollments/update_enrollments.html', {
                'enrollment': enrollment,
                'courses': courses
            })

        try:
            course = Courses.objects.get(id=course_id)
        except Courses.DoesNotExist:
            messages.error(request, "Le cours sélectionné n'existe pas.")
            return render(request, 'home/Enrollments/update_enrollments.html', {
                'enrollment': enrollment,
                'courses': courses
            })



        # Mettre à jour l'inscription
        enrollment.course = course
        enrollment.enrollment_date = enrollment_date
        enrollment.grade = grade
        enrollment.status = status
        enrollment.save()

        messages.success(request, "L'inscription a été modifiée avec succès.")
        return redirect('enrollments')  # Rediriger vers la liste des inscriptions

    # Si la méthode est GET, afficher le formulaire de modification
    return render(request, 'home/Enrollments/update_enrollments.html', {
        'enrollment': enrollment,
        'courses': courses
    })
    
def delete_enrollments(request: HttpRequest, enrollment_id):
    enrollment = get_object_or_404(Enrollments, id=enrollment_id)

    if request.method == 'POST':
        enrollment.delete()
        messages.success(request, "L'inscription a été supprimée avec succès.")
        return redirect('enrollments')

    # Renvoyer une réponse HTTP 405 (Méthode non autorisée)
    return HttpResponseNotAllowed(['POST'])
    


