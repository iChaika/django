from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='blog/images')

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
