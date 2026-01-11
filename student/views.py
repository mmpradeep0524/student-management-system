from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course
from django.db.models import Q  # for search

# ---------------------------
# Student List with Search
# ---------------------------
def student_list(request):
    query = request.GET.get('q')
    students = Student.objects.all()
    if query:
        # Search by name or email
        students = students.filter(Q(name__icontains=query) | Q(email__icontains=query))
    return render(request, 'student_list.html', {'students': students})

# ---------------------------
# Add Student
# ---------------------------
def add_student(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        course = Course.objects.get(id=request.POST['course'])
        Student.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            email=request.POST['email'],
            course=course
        )
        return redirect('/')
    return render(request, 'add_student.html', {'courses': courses})

# ---------------------------
# Update Student
# ---------------------------
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    courses = Course.objects.all()
    if request.method == 'POST':
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.email = request.POST['email']
        student.course = Course.objects.get(id=request.POST['course'])
        student.save()
        return redirect('/')
    return render(request, 'update_student.html', {'student': student, 'courses': courses})

# ---------------------------
# Delete Student
# ---------------------------
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('/')

# ---------------------------
# Add Course
# ---------------------------
def add_course(request):
    if request.method == 'POST':
        Course.objects.create(name=request.POST['name'])
        return redirect('/add-course/')
    return render(request, 'add_course.html')
