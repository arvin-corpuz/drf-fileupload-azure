from django.db import models
from drfupload.azure_storage import PrivateAzureStorage
# Create your models here.

class CoreImage(models.Model):
    file_uploaded = models.FileField(storage=PrivateAzureStorage(), blank=True, null=True)
