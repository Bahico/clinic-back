from django.db import models


# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    certificate = models.FileField()
    image = models.ImageField(upload_to='employee/')
    description = models.CharField(max_length=300)
