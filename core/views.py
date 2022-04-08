from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .serializers import UploadSerializer
from .models import CoreImage

class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    @csrf_exempt
    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type

        ci = CoreImage()
        ci.file_uploaded = file_uploaded
        ci.save()
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)
