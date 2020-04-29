from django.urls import path
from eway.views import *

urlpatterns = [
    path('',home,name = 'home'),
    path('product/',product,name = 'product'),
    path('customer/<str:pk_test>/',customer,name = 'customer'),
    path('create_order/',createOrder, name = 'create_order'),
    path('update_order/<str:pk>/',updateOrder,name = 'update_order'),
    path('delete_order/<str:pk>/',deleteOrder,name = 'delete_order')
]