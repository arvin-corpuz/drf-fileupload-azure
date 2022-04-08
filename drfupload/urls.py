from django.urls import path, include
from rest_framework import routers
from django.contrib import admin
from core.views import UploadViewSet

router = routers.DefaultRouter()
router.register(r'upload', UploadViewSet, basename="upload")

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]



