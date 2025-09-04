from django.urls import path
from .views import OrderStatusUpdateView

urlpatterns = [
    path('orders/<int:pk>/', OrderStatusUpdateView.as_view(), name='order-status-update'),
]
