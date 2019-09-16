from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from enum import Enum

class CountryEnum(Enum):
    SPAIN = 'SPAIN'
    PORTUGAL = 'PORTUGAL'
    FRANCE = 'FRANCE'
    

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(
            max_length=10,
            choices =[(key, key.value) for key in CountryEnum],
            default=CountryEnum.SPAIN
    )

    @receiver(post_save, sender=User)
    def create_customer(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_customer(sender, instance, **kwargs):
        instance.customer.save()


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

class Order(models.Model):
    createdDate = models.DateTimeField(auto_now_add=True)
    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE)
    isReady = models.BooleanField(default=False)

class OrderLine(models.Model):
    quantity =  models.IntegerField()
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)

