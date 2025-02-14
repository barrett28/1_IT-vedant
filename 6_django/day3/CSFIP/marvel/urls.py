from django.urls import path
from . import views

urlpatterns = [
    path('', views.ironman),
    path('spiderman/', views.spiderman)
]
