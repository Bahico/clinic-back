from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.


class NewModel(models.Model):
    title = models.CharField(max_length=240)
    description = models.TextField()
    image = models.ImageField(upload_to='new_image', blank=True, null=True)
    video = models.TextField()
    pdf = models.FileField(upload_to='new_pdf', blank=True, null=True, validators=[
        FileExtensionValidator(allowed_extensions=['pdf'])
    ])
    create_date = models.DateField(auto_now=True, auto_created=True)
