from rest_framework.serializers import Serializer, FileField
from .models import CoreImage

class UploadSerializer(Serializer):
    file_uploaded = FileField()
    class Meta:
        model = CoreImage
        fields = ['file_uploaded']
