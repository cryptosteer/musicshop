from django.conf.urls import url, include

from musicshop import admin, views
from musicshop.views import inicio

urlpatterns = [
    url(r'^incio', views.inicio,name='inicio'),


]
