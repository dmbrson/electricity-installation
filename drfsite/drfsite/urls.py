from django.contrib import admin
from django.urls import path
from electricity.views import InstallationAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
        path('api/v1/installationlust/', InstallationAPIView.as_view()),
]
