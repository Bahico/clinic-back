from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.


class PartnerModel(models.Model):
    image = models.ImageField(upload_to='partner_image')
    pdf = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
