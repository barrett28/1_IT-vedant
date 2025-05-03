from django.urls import path
from . import views

urlpatterns = [
    path('menu-items/', views.MenuItemListView.as_view(), name='menu_item_list'),
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('orders/place/', views.PlaceOrderView.as_view(), name='place_order'),
    path('orders/update/<int:pk>/', views.UpdateOrderStatusView.as_view(), name='update_order_status'),
    path('sales/average/', views.AverageSalesView.as_view(), name='average_sales'),
]
