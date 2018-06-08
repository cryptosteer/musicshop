from django.conf.urls import url
from .views import ArticleListView, ArticleDetailView


app_name = 'musicshop'
urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='articles'),
    url(r'^(?P<pk>[0-9]+)/$', ArticleDetailView.as_view(), name='detail_article'),
]
