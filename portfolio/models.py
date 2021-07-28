from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='portfolio/images')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'