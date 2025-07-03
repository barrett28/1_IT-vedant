from django.urls import path, URLPattern
from api import views

urlpatterns = [
    path("stuinfo/<int:pk>", views.student_details, name="stuinfo"),
    path("stuinfo/", views.student_list, name="stulist"),
]
