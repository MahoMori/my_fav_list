# Generated by Django 3.2.8 on 2021-10-26 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myfav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('book', 'Book'), ('anime/manga', 'Anime/Manga'), ('movie', 'Movie'), ('game', 'Game'), ('food', 'Food'), ('other', 'Other')], default='book', max_length=15)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
