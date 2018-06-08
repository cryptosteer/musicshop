from django.db import models

# Create your models here.

from django.contrib.auth.models import Group, AbstractUser
from django.db import models


# class User(AbstractUser):
#     is_admin = models.BooleanField(default=False)
#     is_agent = models.BooleanField(default=False)
#     is_client = models.BooleanField(default=True)
#
#     def get_admin_profile(self):
#         admin_profile = None
#         if hasattr(self, 'adminprofile'):
#             admin_profile = self.admin_profile
#         return admin_profile
#
#     def get_agent_profile(self):
#         agent_profile = None
#         if hasattr(self, 'agentprofile'):
#             agent_profile = self.developerprofile
#         return agent_profile
#
#     def get_client_profile(self):
#         client_profile = None
#         if hasattr(self, 'clientprofile'):
#             client_profile = self.clientprofile
#         return client_profile
#
#     def save(self, *args, **kwargs):
#         super(User, self).save(*args, **kwargs)
#         if self.is_admin:
#             if len(AdminProfile.objects.filter(user=self)) == 0:
#                 AdminProfile.objects.create(user=self)
#         else:
#             if len(AdminProfile.objects.filter(user=self)) != 0:
#                 AdminProfile.delete(AdminProfile.objects.get(user=self))
#
#     def save(self, *args, **kwargs):
#         super(User, self).save(*args, **kwargs)
#
#         if self.is_agent:
#             if len(AgentProfile.objects.filter(user=self)) == 0:
#                 AgentProfile.objects.create(user=self)
#         else:
#             if len(AgentProfile.objects.filter(user=self)) != 0:
#                 AgentProfile.delete(AgentProfile.objects.get(user=self))
#
#         if self.is_client:
#             if len(ClientProfile.objects.filter(user=self)) == 0:
#                 ClientProfile.objects.create(user=self)
#         else:
#             if len(ClientProfile.objects.filter(user=self)) != 0:
#                 ClientProfile.delete(ClientProfile.objects.get(user=self))
#
#     class Meta:
#         db_table = 'auth_user'


# class AdminProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     cellphone = models.CharField(max_length=10, default="")

    # def __str__(self):
    #     return '{} {}'.format(self.user.first_name, self.user.last_name)


# class AgentProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     github = models.CharField(max_length=60, default="")
#
#     def __str__(self):
#         return '{} {}'.format(self.user.first_name, self.user.last_name)
#
#
# class ClientProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     cellphone = models.CharField(max_length=10, default="")
#
#     def __str__(self):
#         return '{} {}'.format(self.user.first_name, self.user.last_name)


class TipeArticle(models.Model):
    cassete = models.CharField(max_length=50)
    lp = models.CharField(max_length=50)
    cd = models.CharField(max_length=50)
    vhs = models.CharField(max_length=50)
    dvd = models.CharField(max_length=50)
    otros = models.CharField(max_length=50)


class Article(models.Model):
    tipearticle = models.OneToOneField(TipeArticle, on_delete=None)
    genero = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    artista = models.CharField(max_length=50)
    Año = models.CharField(max_length=50)
    Valor = models.CharField(max_length=50)


class Order(models.Model):
    cliente = models.CharField(max_length=50)
    vendedor = models.CharField(max_length=50)
    fecha = models.DateField(blank=True, null=True)
    total = models.FloatField(null=True)


class DetailOrder(models.Model):
    article = models.OneToOneField(Article)
    cantidad = models.IntegerField()
    valor = models.FloatField(null=True)
