from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="home"),
    path("add/", views.add_product, name="add_product"),
    path("update/<int:product_id>/", views.update_stock, name="update_stock"),
]
