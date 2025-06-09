from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("delete/<int:id>/", views.user_del, name="delete"),
    path("update/<int:id>/", views.user_upt, name="update")
]
