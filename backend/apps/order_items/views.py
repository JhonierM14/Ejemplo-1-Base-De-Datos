from django.shortcuts import render

# Create your views here.

from rest_framework import generics, status
from rest_framework.response import Response

from .models import Order_Items
from .serializer import Order_ItemsSerializer

class ListCreateOrder_Items(generics.ListAPIView):
  queryset = Order_Items.objects.all()
  serializer_class = Order_ItemsSerializer
  
  def post(self, request, *args, **kwargs):
    data= request.data
    serr = Order_ItemsSerializer(data=data)
    if (serr.is_valid()):
      serr.save()
      return Response(serr.validated_data, status=status.HTTP_200_OK)  
    
    return Response(status=status.HTTP_400_BAD_REQUEST)
    