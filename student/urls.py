from django.conf.urls import url
from . import views

app_name='student'
urlpatterns = [
    url(r'^all-student-list', views.all_student_list, name='student-list'),


]