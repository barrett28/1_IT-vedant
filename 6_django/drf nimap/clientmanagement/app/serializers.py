from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Client
        fields = "__all__"