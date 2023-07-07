from django.db import models
from django.contrib.auth.models import User
from store.models import Product


# Create your models here.

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,default='cart')
    
    # @property
    # def quantity(self):
    #     total=self.product.price.quantity
    #     return total

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    options=(
        ('Order Placed','Order Placed'),
        ('Shipped','Shipped'),
        ('Out For Delivery','Out For Delivery'),
        ('Delivered','Delivered'),
        ('Cancel','Cancel')
    )
    status=models.CharField(max_length=100,choices=options,default='Order Placed')
    date=models.DateField(auto_now_add=True)