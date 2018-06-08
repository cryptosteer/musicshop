from django.conf.urls import url
from musicshop.views import (UserRegister, index, Login, Logout, dashboard, OrderCreateView,
                             TArticleCreateView, ArticleCreateView, OrderView, ArticleView)
app_name = 'musicshop'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^order/create/$', OrderCreateView.as_view(), name='create_order'),
    url(r'^order/$', OrderView.as_view(), name='view_orders'),
    url(r'^article/$', ArticleView.as_view(), name='view_article'),
    url(r'^tarticle/create/$', TArticleCreateView.as_view(), name='create_tarticle'),
    url(r'^article/create/$', ArticleCreateView.as_view(), name='create_article'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^register/$', UserRegister.as_view(), name='register'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout')
]