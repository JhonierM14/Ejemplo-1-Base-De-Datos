from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    manufacturer_id = models.AutoField(primary_key=True, db_column='manufacturer_id')
    name = models.CharField(max_length=100)
    contact_info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'manufacturer'

    def __str__(self):
        return self.name
