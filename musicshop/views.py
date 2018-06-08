from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, FormView, ListView, DetailView, DeleteView, UpdateView
from .models import (User, ClientProfile, SellerProfile,
                     TypeArticle, Article, Order, OrderDetail
                     )


# Articles
class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article