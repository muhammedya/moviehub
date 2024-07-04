from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

# Categery on Ator Base for fan pupose

# class Actor(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#     slug=models.SlugField(unique=True)
#
#     class Meta:
#         ordering=('-name',)
#
#     def __str__(self):
#         return self.name
#     def get_absolute_url(self):
#         return reverse('story:story_by')


# Create your models here.
class Movie(models.Model):
    # category=models.ForeignKey(Actor, on_delete=models.CASCADE)
    name=models.CharField(max_length=25)
    desc=models.TextField(db_index=True)
    year=models.IntegerField()
    img=models.ImageField(upload_to='gallery')

    # class Meta:
    #     ordering=('-name',)

    def __str__(self):
        return self.name
    # def get_absolute_url(self):
    #     return reverse('MUV:index', args=[self.id,])


 
