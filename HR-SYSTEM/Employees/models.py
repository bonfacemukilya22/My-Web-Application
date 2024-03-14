from django.db import models


# Create your models here.
class Employee(models.Model):
    FullName = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Emp_code = models.CharField(max_length=5)
    MobileNumber = models.CharField(max_length=20)
    Position = models.CharField(max_length=50)

    def __str__(self):
        return self.FullName
