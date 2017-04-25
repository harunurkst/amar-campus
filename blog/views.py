from django.shortcuts import render
from django.http import HttpResponse
import json
from django.shortcuts import get_object_or_404
from blog.models import Post


def category_post(request, id):
    posts = Post.objects.filter(category__pk=id)
    context={
        'posts': posts
    }
    return render(request, 'blog/category_post.html')


def like(request):
    if request.method=='POST':
        user = request.user
        post_id = request.POST.get('id', None)
        post = get_object_or_404(Post, pk=post_id)
        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
            is_liked = False
        else:
            post.likes.add(user)
            is_liked = True
        ctx = {'like_count': post.total_likes, 'is_liked': is_liked}
    return HttpResponse(json.dumps(ctx), content_type='application/json')
