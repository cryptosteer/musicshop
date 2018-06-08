from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_cliente = models.BooleanField(default=False)
    is_vendedor = models.BooleanField(default=False)

    def get_cliente_profile(self):
        cliente_profile = None
        if hasattr(self, 'clienteprofile'):
            cliente_profile = self.clienteprofile
        return cliente_profile

    def get_vendedor_profile(self):
        vendedor_profile = None
        if hasattr(self, 'vendedorprofile'):
            vendedor_profile = self.vendedorprofile
        return vendedor_profile

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        if self.is_cliente:
            if len(ClienteProfile.objects.filter(user=self)) == 0:
                ClienteProfile.objects.create(user=self)
        else:
            if len(ClienteProfile.objects.filter(user=self)) != 0:
                ClienteProfile.delete(ClienteProfile.objects.get(user=self))

        if self.is_vendedor:
            if len(VendedorProfile.objects.filter(user=self)) == 0:
                VendedorProfile.objects.create(user=self)
        else:
            if len(VendedorProfile.objects.filter(user=self)) != 0:
                VendedorProfile.delete(VendedorProfile.objects.get(user=self))

    class Meta:
        db_table = 'auth_user'


class ClienteProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


class VendedorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


class TipoArticulo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)



class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    tipo = models.ForeignKey(TipoArticulo, on_delete=models.CASCADE)
    album = models.CharField(max_length=50)
    artista = models.CharField(max_length=50)
    year = models.DateField()
    valor = models.IntegerField()

    @property
    def only_year(self):
        return self.year.strftime('%Y')

    def __str__(self):
        return '{}'.format(self.nombre)


class Pedido(models.Model):
    cliente = models.ForeignKey(ClienteProfile, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(VendedorProfile, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField()

    def __str__(self):
        return 'Cliente {} {}'.format(self.cliente.user.first_name, self.cliente.user.last_name)


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    valor = models.IntegerField()

    def __str__(self):
        return 'Pedido {}'.format(self.pedido)