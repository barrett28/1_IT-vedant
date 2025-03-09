from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.quantity} kg"
    