from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_client = models.BooleanField(default=True)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='users/', null=True, blank=True)

    class Meta:
        db_table = 'auth_user'

    def get_seller_profile(self):
        seller_profile = None
        if hasattr(self, 'sellerprofile'):
            developer_profile = self.developerprofile
        return developer_profile

    def get_client_profile(self):
        client_profile = None
        if hasattr(self, 'clientprofile'):
            client_profile = self.clientprofile
        return client_profile

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

        if self.is_seller:
            if len(SellerProfile.objects.filter(user=self)) == 0:
                SellerProfile.objects.create(user=self)
        else:
            if len(SellerProfile.objects.filter(user=self)) != 0:
                SellerProfile.delete(SellerProfile.objects.get(user=self))

        if self.is_client:
            if len(ClientProfile.objects.filter(user=self)) == 0:
                ClientProfile.objects.create(user=self)
        else:
            if len(ClientProfile.objects.filter(user=self)) != 0:
                ClientProfile.delete(ClientProfile.objects.get(user=self))

    def __str__(self):
        return '{} {} - {}'.format(self.first_name, self.last_name, self.username)


class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='sellerprofile')

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='clientprofile')

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


class TypeArticle(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    GENRE = (
        ('Clasic_Miusic', 'Clasic Miusic'),
        ('Blues', 'Blues'),
        ('Jazz', 'Jazz'),
        ('Rock_and_Roll', 'Rock and Roll'),
        ('Gospel', 'Gospel'),
        ('Soul', 'Soul'),
        ('Country', 'Country'),
        ('Disco', 'Disco'),
    )
    # attributes
    genre = models.CharField(max_length=100, choices=GENRE)
    typee = models.ForeignKey(TypeArticle, on_delete=models.SET_NULL, null=True, related_name='typearticle')
    album = models.CharField(max_length=150)
    artist = models.CharField(max_length=150)
    year = models.DateField(auto_now=False)
    value = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.artist, self.album)


class Order(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name='orders')
    seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE, related_name='orders')
    date = models.DateField(auto_now_add=True)
    total = models.DecimalField(decimal_places=3, max_digits=20)


class OrderDetail(models.Model):
    article = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders')
    amount = models.IntegerField()
    value = models.DecimalField(decimal_places=3, max_digits=20)
