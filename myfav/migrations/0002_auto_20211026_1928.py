# Generated by Django 3.2.8 on 2021-10-26 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfav', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myfav',
            name='author_or_creator',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='myfav',
            name='genre',
            field=models.CharField(choices=[('book', 'Book'), ('anime/manga', 'Anime/Manga'), ('movie', 'Movie'), ('music', 'Music'), ('game', 'Game'), ('food', 'Food'), ('other', 'Other')], default='book', max_length=15),
        ),
    ]
