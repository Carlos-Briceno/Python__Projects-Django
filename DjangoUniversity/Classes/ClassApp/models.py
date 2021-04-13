from django.db import models

# this will show in the admin screen and let you add a class with a title, the course number, an instructor, and the duration of the course

class djangoClasses(models.Model):
   title = models.CharField(max_length=60, default="")
   course = models.IntegerField(max_length=60, default="")
   instructor = models.CharField(max_length=60, default="")
   duration = models.FloatField(default=0)

   objects = models.Manager()

def __str__(self):
    return self.title

