from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Preparing', 'Preparing'),
        ('Ready', 'Ready'),
        ('Served', 'Served'),
    ]

    customer_name = models.CharField(max_length=100, default="Guest")
    item_name = models.CharField(max_length=100)   # already there
    price = models.DecimalField(max_digits=10, decimal_places=2)  # already there
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.customer_name} ({self.status})"


class SalesReport(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total_orders = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    top_item = models.CharField(max_length=100)

    def __str__(self):
        return f"Report {self.created_at.date()} - Sales: {self.total_amount}"
