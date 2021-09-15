from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail, ResizeToFill

def articles_image_path(instance, filename):
    return f'user_{instance.user.pk}/{filename}'


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # image = models.ImageField(upload_to='images/', blank=True)
    # image = models.ImageField(upload_to='%Y/%m/%d', blank=True)
    # image = models.ImageField(upload_to=articles_image_path, blank=True)
    # image = ProcessedImageField(
    #     blank=True,
    #     processors=[Thumbnail(200,300)],
    #     format='JPEG',
    #     options={'quality': 90},
    # )
    image = models.ImageField(upload_to='origins', blank=True)
    image_thumbnail = ProcessedImageField(
        blank=True,
        processors=[ResizeToFill(100,50)],
        format='JPEG',
        options={'quality': 90},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

