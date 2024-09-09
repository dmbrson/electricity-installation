from rest_framework import serializers
from .models import *

class InstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installation
        fields = ('title', 'cat_id')