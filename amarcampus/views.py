from django.shortcuts import render
from blog.models import Post, Category
from student.models import StudentProfile


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'home/home.html', context)