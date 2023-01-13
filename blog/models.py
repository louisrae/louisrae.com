from django.db import models
from django.urls import reverse

# Create your models here.
format = (
    ("Kindle", "Kindle"),
    ("Audible", "Audible"),
    ("Both", "Both"),
)  # note this comma here
ratings = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class EssayPost(models.Model):
    title = models.TextField()
    subtitle = models.TextField()
    content = models.TextField()
    create_date = models.DateTimeField()
    slug = models.SlugField(default=title)

    def __str__(self) -> str:
        return self.title


class Devlog(models.Model):
    month = models.DateField()
    content = models.TextField()

    def __str__(self):
        return str(self.month)


class BookList(models.Model):
    book_title = models.TextField()
    author = models.TextField()
    read_again = models.BooleanField()
    notes = models.TextField()
    highlights = models.URLField()
    date_finished = models.DateField()
    rating = models.IntegerField(choices=ratings)
    goodreads_link = models.URLField()
    format_read = models.TextField(choices=format)
    times_read = models.IntegerField()

    def __str__(self) -> str:
        return self.book_title
