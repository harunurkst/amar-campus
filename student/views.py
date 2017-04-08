from django.shortcuts import render
from .models import StudentProfile


def all_student_list(request):
    students = StudentProfile.objects.filter(campus=request.user.studentprofile.campus)
    context = {
        'students': students
    }
    return render(request, 'student/all_student_list.html', context)
