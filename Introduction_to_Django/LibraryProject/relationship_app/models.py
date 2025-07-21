from django.db import models

# Create your models here.
class Author(models.Models):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Models):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.Book
class Library(models.Models):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book)
    def __str__(self):
        return self.Library
class Libralian(models.Models):
    name = models.CharField(max_length=50)
    library = models.OneToManyField(Library)
    def __str__(self):
        return self.Libralian