from django.contrib import admin
from .models import Articule,Seller,Client,OrderDetail,Order


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'cellphone', 'email', 'address',)



@admin.register(Client)
class SellerAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'cellphone', 'email', 'address',)


@admin.register(Articule)
class SellerAdmin(admin.ModelAdmin):

    list_display = ('album', 'genere', 'artist', 'year', 'value',)


@admin.register(OrderDetail)
class SellerAdmin(admin.ModelAdmin):

    list_display = ('articule','order','value',)



class DetailInLine(admin.StackedInline):
    model = OrderDetail
    extra = 1


@admin.register(Order)
class SellerAdmin(admin.ModelAdmin):

    list_display = ('client', 'seller','date_order', 'total',)

    inlines = [DetailInLine]

