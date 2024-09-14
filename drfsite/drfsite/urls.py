from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from electricity.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/installation', InstallationAPIList.as_view()),
    path('api/v1/installationlist/', InstallationAPIUpdate.as_view()),
    path('api/v1/installationlist/<int:pk>/', InstallationAPIDestroy.as_view()),
]


#для вьюсета
# router = routers.SimpleRouter()
# router.register(r'installation', InstallationViewSet)