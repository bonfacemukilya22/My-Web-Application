from django.db import models


# Create your models here.
class Studentinfo(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Age = models.IntegerField()
    BirthDate = models.DateField()


def __str__(self):
    return self.FirstName
