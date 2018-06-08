from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    TYPES = (
        ("Seller", "Vendedor"),
        ("Client", "Cliente")
    )
    user_type = models.CharField(max_length=10, choices=TYPES, default='Client')


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.IntegerField(unique=True, auto_created=True)

    def __str__(self):
        return self.user.username


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    credit = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class TArticle(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Article(models.Model):
    name = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    year = models.DateField()
    value = models.BigIntegerField()
    art_type = models.OneToOneField(TArticle, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Seller, on_delete=models.CASCADE)
    date_order = models.DateTimeField(auto_now_add=True, editable=False)
    total = models.BigIntegerField()

    def __str__(self):
        return self.vendor.user.username


class ODetailt(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    cant = models.IntegerField()
    valor = models.BigIntegerField()
    order = models.OneToOneField(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.article.name