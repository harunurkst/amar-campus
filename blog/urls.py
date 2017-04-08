from django.conf.urls import url
from . import views

app_name='blog'
urlpatterns = [
    url(r'^(?P<id>[0-9]+)/$', views.category_post, name='category-post'),


]
