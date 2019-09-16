from django.contrib import admin
from .models import Customer, Order, OrderLine, Product

modelsPack = [Customer, Order, OrderLine, Product]

admin.site.register(modelsPack)
