from django.db import models


# Creating DjangoClasses model.
class DjangoClasses(models.Model):
    Title = models.CharField(max_length=50)
    Course_Number = models.IntegerField()
    Instructor_Name = models.CharField(max_length=50)
    Duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.Title   # Use 'Title' to return the name of the class
