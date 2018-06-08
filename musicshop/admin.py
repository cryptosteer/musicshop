from django.contrib import admin
from musicshop.models import User, Seller, Client, Article, TArticle, Order, ODetailt
from musicshop.forms import UserCreationForm

# Register your models here.
@admin.register(User)
class UserRegister(admin.ModelAdmin):
    form = UserCreationForm

class OrderInline(admin.StackedInline):
    model = ODetailt
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderInline]

class ArticleInline(admin.StackedInline):
    model = Article
    extra = 1

class TArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]

admin.site.register(TArticle, TArticleAdmin)
admin.site.register(Order, OrderAdmin)
