from django.db import models

# Create your models here.
class Review(models.Model):
    movie_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    rank = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.movie_title
