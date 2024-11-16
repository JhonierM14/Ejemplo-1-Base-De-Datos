from django.db import models
from apps.product.models import Product
from apps.order.models import Order


# Create your models here.
class Order_Items(models.Model): #oId, pId, qty, warranty, unitPrice
    order_item_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE, db_column='order_id')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE,db_column='product_id')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "order_items"
        
    def __str__(self):
        return str(self.oId)
