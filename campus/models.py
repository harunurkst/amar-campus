from django.db import models
from location.models import Districts


class CampusInfo(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Districts)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=150)
    sort_name = models.CharField(max_length=25)

    def __str__(self):
        return self.sort_name
