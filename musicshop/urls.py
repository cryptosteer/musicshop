from django.conf.urls import url
from .views import CreateOrder,CreateOrderDetail,ArticuleListView,login,index

app_name = "musicshop"
urlpatterns = [
    url(r'^create_order/$', CreateOrder.as_view(), name='create_order'),
    url(r'^create_order_detail/$', CreateOrderDetail.as_view(), name='create_order_detail'),
    url(r'^list_articule/$', ArticuleListView.as_view(), name='list_order'),
    url(r'^login/$', login.as_view(), name='login'),
    url(r'^index/$', index, name='index')

]