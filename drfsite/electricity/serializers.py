from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import *
class InstallationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = Installation
        fields = "__all__"