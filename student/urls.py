from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_student, name='add_student'),
    path('<int:id>/', views.show_student, name='show_student'),
    path('update/<int:id>/', views.update_student, name='update_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('verify/<int:id>/', views.verify_student, name='verify_student'),
    path('all/', views.show_all_students, name='show_all_students'),  # New URL for showing all students
]
