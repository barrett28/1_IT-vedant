from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('suitcategory/', views.suit_category, name="suitcategory"),
    path('backpackcat/', views.backpack_category, name="backpackcat"),
    path('product/<int:id>/', views.product, name='product'),
    path('dufflecat/', views.dufflecat, name='dufflecat'),
    path('briefcasecat/', views.briefcase, name='briefcase'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('changepassword/',views.changepassword, name="changepassword"),
    path('cart/', views.cart, name='cart')
]
