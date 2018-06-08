from django.db import models
from .profile import Client, Seller

from .articules import Articule



class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    date_order = models.DateTimeField()
    total = models.IntegerField()

    def __str__(self):
        return '{} {} {}'.format(self.seller,"sells to", self.client)


class OrderDetail(models.Model):
    articule = models.ForeignKey(Articule, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    value = models.IntegerField()

    order= models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{}{}'.format(self.quantity,self.value)
