from django.db import models

class Order(models.Model):
    item_name = models.CharField(max_length=100)   # final field
    price = models.DecimalField(max_digits=10, decimal_places=2)  # final field
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item_name} - {self.price}"


class SalesReport(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total_orders = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    top_item = models.CharField(max_length=100)

    def __str__(self):
        return f"Report {self.created_at.date()} - Sales: {self.total_amount}"
    