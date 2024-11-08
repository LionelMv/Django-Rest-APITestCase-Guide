from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=50, unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.code})"


class Order(models.Model):
    item = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return f"Order of {self.item} for {self.price:.2f} by {self.customer.name} at {self.time}"
