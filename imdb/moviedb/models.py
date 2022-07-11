from django.db import models

# Create your models here.

class Movie(models.Model):
    pass

class Actor(models.Model):
    movies = models.ManyToManyField(Movie, through="role", related_name="actors")


class Role(models.Model):
    actor = models.ForeignKey(Actor, null=True, on_delete=models.SET_NULL, related_name="roles")
    movie = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL, related_name="roles")

    class Meta:
        unique_together = (("actor", "movie"))  
