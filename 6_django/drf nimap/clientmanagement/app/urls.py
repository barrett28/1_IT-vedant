from .views import ClientViewset
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clients', ClientViewset, basename='client')

urlpatterns = [
    path("api/", include("router.urls"))
]
