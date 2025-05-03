from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem, Order, OrderItem
from .serializers import MenuItemSerializer, OrderSerializer
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta

class MenuItemListView(APIView):
    def get(self, request):
        menu_items = MenuItem.objects.filter(availability=True)
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)


class PlaceOrderView(APIView):
    def post(self, request):
        order_items_data = request.data.get('order_items', [])
        menu_items_ids = [item['menu_item']['id'] for item in order_items_data]
        unavailable_items = MenuItem.objects.filter(id__in=menu_items_ids, availability=False)
        
        if unavailable_items.exists():
            return Response({"error": "One or more items are unavailable"}, status=status.HTTP_400_BAD_REQUEST)
        
        order = Order.objects.create(status='pending')
        for item_data in order_items_data:
            menu_item = MenuItem.objects.get(id=item_data['menu_item']['id'])
            OrderItem.objects.create(order=order, menu_item=menu_item, quantity=item_data['quantity'])

        return Response({"message": "Order placed successfully"}, status=status.HTTP_201_CREATED)


class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)



class UpdateOrderStatusView(APIView):
    def put(self, request, pk):
        try:
            order = Order.objects.get(id=pk)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

        status_value = request.data.get('status')
        if status_value not in dict(Order.STATUS_CHOICES).keys():
            return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)

        order.status = status_value
        order.save()
        return Response({"message": "Order status updated successfully"}, status=status.HTTP_200_OK)



class AverageSalesView(APIView):
    def get(self, request):
        today = timezone.now().date()
        weekdays = [today - timedelta(days=i) for i in range(1, 5)]  # Last 4 days

        sales = []
        for day in weekdays:
            completed_orders = Order.objects.filter(timestamp__date=day, status='completed')
            order_items = OrderItem.objects.filter(order__in=completed_orders)

            # (price * quantity)
            total_sales = sum(item.menu_item.price * item.quantity for item in order_items)

            # average sales 
            order_count = completed_orders.count()
            average_sales = total_sales / order_count if order_count > 0 else 0

            sales.append({
                'date': day,
                'total_sales': total_sales,
                'average_sales_per_order': average_sales
            })

        return Response(sales)
