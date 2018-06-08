from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse_lazy
from django.utils.text import slugify


class Articulo(models.Model):
    CHOICES = (
        ('cassete', 'Cassete'),
        ('lp', 'LP'),
        ('cd', 'CD'),
        ('vhs', 'VHS'),
        ('dvd', 'DVD'),
        ('otros', 'Otros')
    )

    nombre = models.CharField(unique=True, max_length=12)
    descripcion = models.TextField(unique=True, max_length=12)
    tipo = models.CharField(max_length=7, choices=CHOICES, default='otros')
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return '{0} {1}'.format(self.nombre)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Articulo, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('', kwargs={'slug': self.slug})


class Vendedor(User):
    cedula = models.CharField(unique=True, max_length=12)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(Vendedor, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('', kwargs={'slug': self.slug})


class Cliente(models.Model):
    cedula = models.CharField(unique=True, max_length=12)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return '{0} {1}'.format(self.nombre, self.apellido)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Cliente, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('', kwargs={'slug': self.slug})


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return 'Pedido {}'.format(self.cliente.nombre)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.fecha)
        super(Pedido, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('', kwargs={'slug': self.slug})


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    valor = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.pedido

    def save(self, *args, **kwargs):
        self.slug = slugify(self.pedido.fecha)
        super(DetallePedido, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('', kwargs={'slug': self.slug})
