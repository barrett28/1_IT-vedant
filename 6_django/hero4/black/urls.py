from django.urls import path
from black import views

urlpatterns=[
    path('tile/', views.tile),
    path('powder/', views.powder)
]