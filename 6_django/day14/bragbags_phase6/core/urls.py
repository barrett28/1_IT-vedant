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
    path('add_to_cart/<int:id>/', views.add_to_cart, name='addtocart'),
    path('view_cart/', views.view_cart, name='viewcart'),
    path('add_quantity/<int:id>/', views.add_quantity, name='add_quantity'),
    path('del_quantity/<int:id>/', views.delete_quantity, name='del_quantity'),
    path('delete_cart_item/<int:id>/', views.delete_cart_item, name='deletecartitem'),
    # path('summary/', views.summary, name='summary'),
    path('address/', views.address, name='address'),
    path('delete_address/<int:id>', views.delete_address, name='deleteaddress'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment_success/',views.payment_success,name='paymentsuccess'),
    path('payment_failed/',views.payment_failed,name='paymentfailed'),
]
