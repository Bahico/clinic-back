from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

from django.core.exceptions import ValidationError


def file_size(value):  # add this to some file where you can import it from
    limit = 10 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(validators=[FileExtensionValidator(['jpeg', 'png', 'mpeg'])])
    price = models.IntegerField()
    pdf = models.FileField(validators=[FileExtensionValidator(['pdf'])])

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'


class Video(models.Model):
    video = models.TextField()
