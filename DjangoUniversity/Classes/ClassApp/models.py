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

# this is the student names and grade level
class studentNames(models.Model):
   first_name = models.CharField(max_length=30, default="")
   last_name = models.CharField(max_length=30, default="")
   grade = models.IntegerField(max_length=12, default="")



class schedule(models.Model):
   weekdays = models.CharField(max_length=30, default="")
   time = models.IntegerField(max_length=30, default="")
