from django.db import models

# Create your models here.


class Cliente (models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=100)
    cedula=models.CharField(max_length=12)

    def __str__(self):
        return self.nombre


class Vendedor (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=12)
    sector=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class TipoArticulo (models.Model):
    tipo=models.CharField(max_length=120,default='OTROS')

    def __str__(self):
        return self.tipo


class Articulo (models.Model):
    nombre=models.CharField(max_length=150)
    genero=models.CharField(max_length=100)
    artista=models.CharField(max_length=50)
    valor=models.IntegerField()
    year=models.DateField()
    tipoArticulo=models.ForeignKey(TipoArticulo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    fecha=models.DateField()
    total=models.FloatField()
    clientePedido=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedorPedido=models.ForeignKey(Vendedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.id