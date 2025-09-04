from rest_framework import generics, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

# Update order status step by step
class OrderStatusUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        new_status = request.data.get("status")

        # Allowed transitions
        allowed_transitions = {
            "Pending": ["Preparing"],
            "Preparing": ["Ready"],
            "Ready": ["Served"],
            "Served": [],
        }

        if new_status not in allowed_transitions[order.status]:
            return Response(
                {"error": f"Invalid status transition from {order.status} → {new_status}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        order.status = new_status
        order.save()
        return Response(OrderSerializer(order).data, status=status.HTTP_200_OK)
