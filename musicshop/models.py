from django.db import models

# Create your models here.
class Tipoarticulo (models.Model):
    tarticulo=models.CharField(max_length=50)

    def __str__(self):
        return self.tarticulo

class Cliente (models.Model):
    nombre=models.CharField(max_length=40)
    cedula=models.CharField(max_length=10)
    direccion=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Vendedor (models.Model):
    nombre= models.CharField(max_length=40)
    cedula= models.CharField(max_length=10)
    direccion= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Articulo (models.Model):
    genero=models.CharField(max_length=50)
    tipo_articulo=models.ForeignKey(Tipoarticulo,on_delete=models.CASCADE)
    album=models.CharField(max_length=50)
    año=models.CharField(max_length=10)
    valor=models.IntegerField

    def __str__(self):
        return self.tipo_articulo


class Pedido (models.Model):
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
    vendedor=models.ForeignKey(Vendedor,on_delete=models.CASCADE)
    articulo=models.ForeignKey(Articulo,on_delete=models.CASCADE)
    fecha= models.CharField(max_length=10)
    cantidad=models.CharField(max_length=10)
    valor=models.CharField(max_length=10)
    total=models.CharField(max_length=10)











