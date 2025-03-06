from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('product/', views.product),
    path('suitcat/', views.suitcategory),
]
