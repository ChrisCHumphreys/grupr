from django.db import models

# Create your models here.

class Walk(models.Model):
    name = models.CharField(max_length=200)
    start_place = models.CharField(max_length=200)
    slug = models.SlugField(default="walk_slug")
    
    def __str__(self):
        return self.name

class People(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=25)
    rating = models.IntegerField(default=0)
    slug = models.SlugField(default="people_slug")

    def __str__(self):
        return self.slug
