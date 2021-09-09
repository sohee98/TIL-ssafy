from django.db import models

# Create your models here.
class Burgerking(models.Model):
    menu = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    content = models.TextField(max_length=100)
    image = models.ImageField(upload_to='images/',blank=True,)
    updated_at = models.DateTimeField(auto_now=True)