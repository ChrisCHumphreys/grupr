from django.db import models
from django.urls import reverse
# Create your models here.

class Walk(models.Model):
    name = models.CharField(max_length=200)
    start_place = models.CharField(max_length=200)
    slug = models.SlugField(default="walk_slug")
    
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail',
                       kwargs={'slug':self.slug})

class People(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=25)
    rating = models.IntegerField(default=0)
    walk = models.ForeignKey(Walk, on_delete=models.CASCADE)
    slug = models.SlugField(default="people_slug")

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('person_detail',
                       kwargs={'slug':self.slug})
