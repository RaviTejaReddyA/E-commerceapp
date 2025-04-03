from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Product(models.Model):
    proname = models.CharField(max_length=20)
    proprice = models.IntegerField(default=0)
    image = models.ImageField(upload_to='image/')
    def _str_(self):
        return self.proname
        return self.proprice

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def subtotal(self):
        return self.product.proprice * self.quantity

class OrdersItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def subtotal(self):
        return self.product.proprice * self.quantity