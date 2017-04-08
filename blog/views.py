from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

def category_post(request, id):
    posts = Post.objects.filter(category__pk=id)
    context={
        'posts':posts
    }
    return render(request, 'blog/category_post.html')


def like(request):
    return HttpResponse('OK')
