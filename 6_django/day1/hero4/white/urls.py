from django.urls import path
from white import views

urlpatterns=[
    path('milk/', views.milk),
    path('sugar', views.sugar)
]