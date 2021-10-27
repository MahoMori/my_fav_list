from django.db import models
# from django.contrib.auth.models import User

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
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    description= models.TextField(blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name