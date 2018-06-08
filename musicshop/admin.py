from django.contrib import admin
from django.contrib import admin
from django.db.models import Sum
from django.forms import Textarea
from django.db import models
from .models import TipeArticle, Article, Order, DetailOrder #User, AdminProfile, AgentProfile, ClientProfile,



# Register your models here.


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#
#     list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'is_project_manager',
#                        'is_developer', 'is_client')
#     list_filter = ('is_project_manager', 'is_developer', 'is_client')
#     fieldsets = [
#         ('User information', {
#             'fields': ['username',
#                        'password',
#                        'first_name',
#                        'last_name',
#                        'email',
#                        'is_project_manager',
#                        'is_developer',
#                        'is_client',]
#         }),
#     ]


# @admin.register(AdminProfile)
# class AdminProfileAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         return False
#
#
# @admin.register(AgentProfile)
# class AgentProfileAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         return False
#
#
# @admin.register(ClientProfile)
# class ClientProfileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user')
#
#     def has_add_permission(self, request):
#         return False


#@admin.register(TipeArticle)
#class AdminTipeArticle (admin.ModelAdmin):
#    list_display = ('id')
#    list_filter = (')


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ('id', 'tipearticle', 'genero', 'album', 'artista', 'Valor')
    list_filter = ('id', 'tipearticle', 'genero', 'artista')


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'vendedor', 'fecha', 'total')
    list_filter = ('id', 'cliente', 'vendedor')


@admin.register(DetailOrder)
class AdminDetailOrder(admin.ModelAdmin):
    list_display = ('id', 'article', 'cantidad', 'valor')
    list_filter = ('id', 'article', )



