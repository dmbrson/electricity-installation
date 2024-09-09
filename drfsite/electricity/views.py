from rest_framework import generics
from .models import *
from .serializers import InstallationSerializer


class InstallationAPIView(generics.ListAPIView):
    queryset = Installation.objects.all()
    serializer_class = InstallationSerializer
