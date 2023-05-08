from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='product/')
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'


class Video(models.Model):
    video = models.FileField()
