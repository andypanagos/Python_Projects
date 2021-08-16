from django.db import models


# Create your models here.
class DjangoClasses(models.Model):
    Title = models.CharField(max_length=50)
    Course_Number = models.IntegerField()
    Instructor_Name = models.CharField(max_length=50)
    Duration = models.FloatField()

    objects = models.Manager()



