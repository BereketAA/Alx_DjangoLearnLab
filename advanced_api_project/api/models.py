from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the author")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255, help_text="Title of the book")
    publication_year = models.IntegerField(help_text="Year the book was published")
    author = models.ForeignKey(
        Author, 
        related_name='books', 
        on_delete=models.CASCADE,
        help_text="Author of the book"
    )

    def __str__(self):
        return self.title