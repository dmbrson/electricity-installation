from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import InstallationSerializer

class InstallationAPIList(generics.ListCreateAPIView):
    queryset = Installation.objects.all()
    serializer_class = InstallationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class InstallationAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Installation.objects.all()
    serializer_class = InstallationSerializer
    permission_classes = (IsOwnerOrReadOnly, )

class InstallationAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Installation.objects.all()
    serializer_class = InstallationSerializer
    permission_classes = (IsAdminOrReadOnly, )

# class InstallationViewSet(viewsets.ModelViewSet):
#     queryset = Installation.objects.all()
#     serializer_class = InstallationSerializer


# class InstallationAPIView(APIView):
#     def get(self, request):
#         w = Installation.objects.all()
#         return Response({'posts': InstallationSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = InstallationSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'posts': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         try:
#             instance = Installation.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = InstallationSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
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
