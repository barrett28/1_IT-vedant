from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dc/', views.Dc),
    path('details/', views.details)
]
