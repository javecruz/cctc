from datetime import datetime
from enum import Enum
import csv
import pdb
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.mail import EmailMessage

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

    # Returns total amount to pay in whole order
    def get_total_order(self):
        lines = OrderLine.objects.filter(orderId=self.id)[0]
        return sum([line.get_total_order_line() for line in lines])

class OrderLine(models.Model):
    quantity =  models.IntegerField()
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    # Returns total amount to pay in line
    def get_total_order_line(self):
        return Product.objects.get(pk=self.productId.id).price * self.quantity

# Checks when order is ready in order to notify by email
# Should've used post_save but updated fields are None when being updated through django admin
@receiver(pre_save, sender=Order)
def save_order(*args, **kwargs):
    # Check either object is created or being created
    if kwargs['instance'].id != None:
        old = Order.objects.get(pk=kwargs['instance'].id).isReady
        new = kwargs['instance'].isReady
        if new and old != new:
            # Send email to itself for test purposes
            email = EmailMessage(
                    'Your order has been processed',
                    'This is Cecotec',
                    settings.EMAIL_HOST_USER,
                    [settings.EMAIL_HOST_USER]
            )
            # Create file name using epoch time
            filename = str(int(datetime.timestamp(datetime.now()))) + '.csv'
            # Create csv given a filename and orderId
            create_csv_file(filename, kwargs['instance'].id)
            email.attach_file(filename)
            
            # TODO: Fix sending messages, google policy may be changed
            #email.send()

def create_csv_file(filename, order):
    lines = OrderLine.objects.filter(orderId=order)
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['product', 'price', 'quantity', 'total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for line in lines:
            product = line.productId.name
            price = line.productId.price
            quantity = line.quantity
            total = line.get_total_order_line()

            writer.writerow({
                'product': product,
                'price': price,
                'quantity': quantity,
                'total': total
            })

