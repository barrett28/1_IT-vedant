from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('suitcategory/', views.suit_category, name="suitcategory"),
    path('backpackcat/', views.backpack_category, name="backpackcat"),
    path('product/<int:id>/', views.product, name='product'),
    path('dufflecat/', views.dufflecat, name='dufflecat'),
    path('briefcasecat/', views.briefcase, name='briefcase'),
]
