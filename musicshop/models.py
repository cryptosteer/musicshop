import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_cliente = models.BooleanField(default=False)
    is_vendendor = models.BooleanField(default=False)

    def get_vendedor_profile(self):
        vendedor_profile = None
        if hasattr(self, 'vendedorprofile'):
            vendedor_profile = self.vendedorprofile
        return vendedor_profile

    def get_client_profile(self):
        client_profile = None
        if hasattr(self, 'clientprofile'):
            client_profile = self.clientprofile
        return client_profile

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        if self.is_vendendor:
            if len(VendedorProfile.objects.filter(user=self)) == 0:
                VendedorProfile.objects.create(user=self)
        else:
            if len(VendedorProfile.objects.filter(user=self)) != 0:
                VendedorProfile.delete(VendedorProfile.objects.get(user=self))

        if self.is_cliente:
            if len(ClientProfile.objects.filter(user=self)) == 0:
                ClientProfile.objects.create(user=self)
        else:
            if len(ClientProfile.objects.filter(user=self)) != 0:
                ClientProfile.delete(ClientProfile.objects.get(user=self))

    class Meta:
        db_table = 'auth_user'


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class VendedorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class TipoArticulo(models.Model):
    nombre = models.CharField(max_length=50, blank=False)


class Articulo(models.Model):
    genero = models.CharField(max_length=100, blank=False)
    tipoarticulo = models.ForeignKey(TipoArticulo, on_delete=models.CASCADE)
    album = models.CharField(max_length=100, blank=False)
    artista = models.CharField(max_length=100, blank=False)
    anio = models.DateField(default=datetime.date.today)
    valor = models.BigIntegerField(default=0, blank=False)


class Pedido(models.Model):
    cliente = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, null=True, blank=True)
    vendedor = models.ForeignKey(VendedorProfile, on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateField(default=datetime.date.today)
    total = models.BigIntegerField(default=0, blank=False)


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0, blank=False)
    valor = models.BigIntegerField(default=0, blank=False)

    def save(self, *args, **kwargs):
        self.valor = self.articulo.valor*self.cantidad
        super(DetallePedido, self).save(*args, **kwargs)