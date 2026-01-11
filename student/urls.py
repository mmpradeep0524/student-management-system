from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),          # Home page → student list
    path('view/', views.student_list, name='view_students'),   # Optional: another URL to view students
    path('add-student/', views.add_student, name='add_student'), # Add Student page
    path('add-course/', views.add_course, name='add_course'),   # Add Course page
    path('update/<int:id>/', views.update_student, name='update_student'), # Update Student
    path('delete/<int:id>/', views.delete_student, name='delete_student'), # Delete Student
]
