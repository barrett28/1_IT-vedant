from django.urls import path
from female import views

urlpatterns=[
    path('girl/', views.girl),
    path('women/', views.women)
]