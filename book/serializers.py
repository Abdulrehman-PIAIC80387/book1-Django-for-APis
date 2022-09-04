from dataclasses import field
from rest_framework import serializers

from .models import My_library



class bookserializer(serializers.ModelSerializer):
    class Meta:
        model = My_library
        fields = '__all__'