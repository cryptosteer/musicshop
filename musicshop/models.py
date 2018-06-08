import datetime

from django.db import models

# Create your models here.


class Perfil(models.Model):
    nombre=models.CharField(max_length=100)
    num_tel=models.CharField(max_length=12)
    identificacion=models.CharField(max_length=12)

    def __str__(self):
        return self.nombre

class Vendedor(Perfil):
    codigo=models.CharField(max_length=12)

    def __str__(self):
        return self.nombre

class Cliente(Perfil):
    direccion=models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    STATE = (
        (1, 'Cassete'),
        (2, 'LP'),
        (3, 'CD'),
        (4, 'DVD'),
        (5, 'VHS')
    )
    genero=models.CharField(max_length=100)
    album=models.CharField(max_length=100)
    artista=models.CharField(max_length=100)
    ano=models.DateField(max_length=100)
    valor=models.CharField(max_length=100)
    tipo_articulo= models.IntegerField(choices=STATE)

    def __str__(self):
        return str(self.STATE)#me falto algo aqui



class Pedido(models.Model):
    clt=models.ForeignKey(Cliente, blank=True, null=True, on_delete=models.CASCADE)
    vnd=models.ForeignKey(Vendedor, blank=True, null=True, on_delete=models.CASCADE)
    fecha = models.DateTimeField(blank=True, null=True)
    referencia = models.CharField(max_length=30, blank=True,null=True)

    def __str__(self):
        return str(self.referencia)



class Detalle_p(models.Model):
    r=models.ForeignKey(Pedido, blank=True, null=True, on_delete=models.CASCADE)
    art = models.ForeignKey(Articulo, blank=True, null=True, on_delete=models.CASCADE)
    cant=models.IntegerField()



