from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('product/', views.product, name="product"),
    path('suitcat/', views.suitcategory, name="suitcategory"),
]
