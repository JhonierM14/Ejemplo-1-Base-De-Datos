from django.db import models
from apps.clients.models import Customer

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True, db_column='order_id')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='customer_id')
    #reference = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)  # Equivalente al TIMESTAMP con CURRENT_TIMESTAMP
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = "order"
        
    def __str__(self):
        return str(self.order_id)
