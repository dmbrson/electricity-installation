from django.contrib import admin
from django.urls import path
from electricity.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/installationlist/', InstallationAPIList.as_view()),
    path('api/v1/installationlist/<int:pk>/', InstallationAPIUpdate.as_view()),
]
