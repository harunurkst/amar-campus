from django.db import models
from django.contrib.auth.models import User
from campus.models import CampusInfo, Department


class StudentProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=150)
    campus = models.ForeignKey(CampusInfo)
    department = models.ForeignKey(Department)
    batch = models.IntegerField()

    def __str__(self):
        return self.name
