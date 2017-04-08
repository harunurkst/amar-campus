from django.shortcuts import render
from blog.models import Post, Category
from student.models import StudentProfile
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'home/home.html', context)

@login_required()
def capmus_post(request):
    posts = Post.objects.filter(author__studentprofile__campus=request.user.studentprofile.campus)
    context = {
        'posts': posts
    }
    return render(request, 'home/campus_post.html', context)


@login_required()
def batch_post(request):
    student_profile = request.user.studentprofile
    posts = Post.objects.filter(
        Q(author__studentprofile__campus=student_profile.campus),
        Q(author__studentprofile__department=student_profile.department),
        Q(author__studentprofile__batch=student_profile.batch)
    )
    context = {
        'posts': posts
    }
    return render(request, 'home/batch_post.html', context)
