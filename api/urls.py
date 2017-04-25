from django.conf.urls import url
from . import views


urlpatterns = [
    #url(r'^(?P<id>[0-9]+)/$', views.category_post, name='category-post'),
    url(r'^likes/(?P<pk>[0-9]+)/$', views.LikeView.as_view()),


]
