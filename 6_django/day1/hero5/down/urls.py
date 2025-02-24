from django.urls import path
from down import views

urlpatterns=[
    path('ground/', views.ground)
]