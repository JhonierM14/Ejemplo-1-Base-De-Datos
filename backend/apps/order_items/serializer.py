from rest_framework import serializers
from .models import Order_Items

class Order_ItemsSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Order_Items
    fields = '__all__'