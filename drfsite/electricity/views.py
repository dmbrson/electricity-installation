from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import InstallationSerializer


class InstallationAPIView(APIView):
    def get(self, request):
        w = Installation.objects.all()
        return Response({'posts': InstallationSerializer(w, many=True).data})

    def post(self, request):
        serializer = InstallationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Installation.objects.create(
            title = request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id'],
        )
