from rest_framework import viewsets
from .models import Customer, Order, OrderLine, Product
from .serializers import CustomerSerializer, ProductSerializer

class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
