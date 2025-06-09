from django.shortcuts import render
from .models import Client
from .serializers import ClientSerializer
from rest_framework import viewsets , permissions
# Create your views here.


class ClientViewset(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)
