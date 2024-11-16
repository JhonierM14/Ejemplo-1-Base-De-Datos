from django.db import models
from apps.manufacturer.models import Manufacturer

class Product(models.Model):
    product_id = models.AutoField(primary_key=True, db_column='product_id')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, db_column='manufacturer_id')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name
