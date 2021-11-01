from django.db import models

# Create your models here.

class Actor(models.Model):
    # movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movies')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.pk}: {self.name}'

class Movie(models.Model):
    # actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.TextField()

    def __str__(self):
        return f'{self.pk}: {self.title}'


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    actors = models.ManyToManyField(Actor, related_name='reviews')
    title = models.CharField(max_length=100)
    content= models.TextField()
    rank = models.IntegerField()

    def __str__(self):
        return f'{self.pk}: {self.title}'

