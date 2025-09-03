from celery import shared_task
from django.db.models import Sum, Count
from .models import Order, SalesReport

@shared_task
def generate_sales_report():
    total_orders = Order.objects.count()
    total_sales = Order.objects.aggregate(total=Sum("price"))["total"] or 0
    top_item = (
        Order.objects.values("item_name")
        .annotate(count=Count("id"))
        .order_by("-count")
        .first()
    )
    top_item_name = top_item["item_name"] if top_item else "N/A"

    report = SalesReport.objects.create(
        total_orders=total_orders,
        total_amount=total_sales,
        top_item=top_item_name,
    )
    return {
        "date": str(report.created_at.date()),
        "total_orders": total_orders,
        "total_sales": float(total_sales),
        "top_item": top_item_name,
    }
