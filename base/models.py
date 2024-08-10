from django.db import models

# Create your models here.
class Library(models.Model):
    Name = models.CharField(max_length=100)

    Description = models.TextField()
    Category = models.CharField(max_length=25)
    Author = models.CharField (max_length=50)
    BooksFormat = models.CharField(max_length=50)
