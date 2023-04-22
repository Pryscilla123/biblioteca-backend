from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255, null=False)


class Book(models.Model):
    title = models.CharField(max_length=255, null=False)
    editor = models.CharField(max_length=255, null=False)
    photo = models.CharField(max_length=255, null=False)
    author = models.ManyToManyField(Author)
