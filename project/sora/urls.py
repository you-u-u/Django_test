from django.urls import path
from .views import CustomerList, DetailCustomer, CreateCustomer, UpdateCustomer, DeleteCustomer

app_name = 'sora'

urlpatterns = [
    path('customers', CustomerList.as_view(), name='index'),
    path(
        'customer/<int:pk>/detail/',
        DetailCustomer.as_view(),
        name='detail_customer',
    ),
    path('customer/create/', CreateCustomer.as_view(), name='create'),
    path('customer/<int:pk>/update/', UpdateCustomer.as_view(), name='update'),
    path('customer/<int:pk>/delete/', DeleteCustomer.as_view(), name='delete'),

]
