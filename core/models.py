from django.db import models
from django.conf import settings
from django.urls import reverse

class Tags(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Ingredients'


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    data_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags, blank=True)
    ingredients = models.ManyToManyField(Ingredients, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='pictures', default='pictures/mypic.jpg')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:detail', args=[self.pk])

    def get_summary(self):
        return self.description[:100] + '...'

    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/media/pictures/mypic.jpg'
