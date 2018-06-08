from django.conf.urls import url
from musicshop.views import UserRegister, index, Login, Logout, dashboard
app_name = 'musicshop'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^register/$', UserRegister.as_view(), name='register'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout')
]