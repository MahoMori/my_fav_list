from django.db import models

# Create your models here.


class Myfav(models.Model):

    genre_choices = (
        ('book', 'Book'),
        ('anime/manga', 'Anime/Manga'),
        ('movie', 'Movie'),
        ('music', 'Music'),
        ('game', 'Game'),
        ('food', 'Food'),
        ('other', 'Other')
    )

    name= models.CharField(max_length=100)
    author_or_creator= models.CharField(max_length=100, blank=True)
    genre= models.CharField(max_length=15, choices=genre_choices, default='book')
    # image= models.ImageField(upload_to='images')
    description= models.TextField(blank=True)

    def __str__(self):
        return self.name