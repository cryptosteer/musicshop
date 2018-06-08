from django.db import models

# Create your models here.


class Employee(models.model):
    identifier = models.Charfield(unique=True, max_length=11)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Client(models.model):
    identifier = models.Charfield(unique=True, max_length=11)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name




class Article(models.Model):
    gender = (
        (ROCK, 'Rock'),
        (COUNTRY, 'Country'),
        (POP, 'Pop'),
        (ElECTRO, 'Electro'),
    )
    type_of_music = (
        (CASSETE, 'Cassete'),
        (LP, 'LP'),
        (CD, 'CD'),
        (VHS, 'VHS'),
        (DVD, 'DVD'),
        (OTHER, 'Other')
    )
    title = models.Charfield(max_length=50)
    album = models.Charfield(max_length=50)
    artist = models.Charfield(max_length=50)
    YEAR_CHOICES = [(r, r) for r in range(1920, datetime.date.today().year + 1)]
    year = models.IntegerField(_('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    amount = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Order(models.Model):
    client = models.ForeingKey(Client, on_delete=models.CASCADE) # one to many | a la orden se le puede asignar a un cliente
    employee = models.ForeingKey(Employee, on_delete=models.CASCADE) # one to many | a la orden se le puede asignar a un empleado
    date = models.DateField()
    total_price = models.PositiveIntegerField()
    article = models.ManyToManyField(Article, through='OrderDetails')  # relation many to many


class OrderDetails(models.Model): # tabla intermedia: detalles del pedido
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    amount = models.ForeignKey(Article.amount, on_delete=models.CASCADE)
    price = models.ForeignKey(Article.price, on_delete=models.CASCADE)
    
    def __str__(self):
       return str(self.note)
