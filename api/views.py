from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from blog.models import Post


class LikeView(APIView):
    def get(self, request, pk):
        user = request.user
        post = get_object_or_404(Post, pk=pk)
        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
            is_liked = False
        else:
            post.likes.add(user)
            is_liked = True
        ctx = {'like_count': post.total_likes, 'is_liked': is_liked}
        return Response(ctx)
