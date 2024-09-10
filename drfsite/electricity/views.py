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
        serializer.save()

        return Response({'posts': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = Installation.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = InstallationSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
    # def delete(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None)
    #     if not pk:
    #         return Response({"error": "Method Delete not allowed"})
    #     try:
    #         instance = Installation.objects.get(pk=pk)
    #     except:
    #         return Response({"error": "Object does not exists"})
    #
    #     instance.delete()
    #     return Response({"ok": "you deleted " + str(pk)})
