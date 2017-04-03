from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Post(models.Model):
    description = models.TextField()
    category = models.ForeignKey(Category)
    author = models.ForeignKey(User)

    def __str__(self):
        return str(self.pk)
