from django import template

register = template.Library()

@register.filter(name="is_liked")
def is_liked(user):
    post_id = request.POST.get('id', None)
    post = get_object_or_404(Post, pk=post_id)
    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user)
        is_liked = False
    else:
        post.likes.add(user)
        is_liked = True
    return is_liked
