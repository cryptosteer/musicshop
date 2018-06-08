from django.contrib import admin
from .models import (User, ClientProfile, SellerProfile,
                     TypeArticle, Article, Order, OrderDetail
                     )


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'avatar', 'is_seller', 'is_client',)
    list_filter = ('is_seller', 'is_client')
    fieldsets = [
        ('User information', {
            'fields': ['username',
                       'password',
                       'first_name',
                       'last_name',
                       'email',
                       'avatar',
                       'is_seller',
                       'is_client', ]
        }),
    ]


@admin.register(ClientProfile)
class AdminClient(admin.ModelAdmin):
    list_display = ('id', 'user',)

    def has_add_permission(self, request):
        return False


@admin.register(SellerProfile)
class AdminSeller(admin.ModelAdmin):
    list_display = ('id', 'user',)

    def has_add_permission(self, request):
        return False


@admin.register(TypeArticle)
class AdminTypeArticle(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ('genre', 'typee', 'album', 'artist', 'year', 'value', 'image')
    list_filter = ('genre', 'typee')


class OrderDetailInLine(admin.StackedInline):
    model = OrderDetail
    fields = ('article', 'amount', 'value')
    extra = 1


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ('client', 'seller', 'date', 'total',)
    fieldsets = [
        ('Order Information', {
            'fields': ['client',
                       'seller',
                       'total',
                       ]
        })
    ]
    inlines = [OrderDetailInLine]


@admin.register(OrderDetail)
class AdminOrderDetail(admin.ModelAdmin):
    pass
