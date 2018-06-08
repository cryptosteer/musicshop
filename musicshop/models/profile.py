from django.db import models
from django.contrib.auth.models import User

class Client(User):

    cellphone = models.IntegerField()
    address = models.CharField(max_length=25)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Seller(User):

    cellphone = models.IntegerField()
    address = models.CharField(max_length=25)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
