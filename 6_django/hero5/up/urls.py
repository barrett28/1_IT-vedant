from django.urls import path
from up import views

urlpatterns=[
    path('sky/', views.sky)
]