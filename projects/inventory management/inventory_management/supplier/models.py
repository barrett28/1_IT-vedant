from django.db import models
from core.models import User

class SupplierProduct(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name