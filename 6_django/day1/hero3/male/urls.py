from django.urls import path
from male import views

urlpatterns=[
    path('', views.boy),
    path('men/',views.men)
]